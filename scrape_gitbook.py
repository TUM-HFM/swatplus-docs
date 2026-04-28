#!/usr/bin/env python3
"""
SWAT+ GitBook Scraper
Fetches Introduction, Input Files, and Output Files from the SWAT+ GitBook
and writes them into a MkDocs-ready docs/ folder structure.
Images are downloaded locally to docs/assets/images/.
Also auto-generates the nav section of mkdocs.yml.

Usage:
  python scrape_gitbook.py

Dependencies:
  pip install requests beautifulsoup4 markdownify pyyaml
"""

import requests
import hashlib
import sys

USE_PLAYWRIGHT = "--playwright" in sys.argv
import os
import re
import time
import yaml
from bs4 import BeautifulSoup, Tag
from markdownify import MarkdownConverter
from collections import OrderedDict
from urllib.parse import urljoin, urlparse, parse_qs, unquote

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_URL     = "https://swatplus.gitbook.io/io-docs"
GITBOOK_BASE = "https://swatplus.gitbook.io"
DOMAIN       = "swatplus.gitbook.io"
PROJECT_DIR  = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR     = os.path.join(PROJECT_DIR, "docs")
IMAGES_DIR   = os.path.join(DOCS_DIR, "assets", "images")
MKDOCS_YML   = os.path.join(PROJECT_DIR, "mkdocs.yml")
DELAY        = 0.6

ALLOWED_PREFIXES = [
    "/io-docs",
    "/io-docs/introduction",
    "/io-docs/introduction-1",
    "/io-docs/swat+-output-files",
]
BLOCKED_SEGMENTS = ["/theoretical-documentation"]

# Pages that only appear in the GitBook sidebar when their section is active
# (client-side render only) — seed them explicitly so the crawler visits them
SEED_URLS = [
    # Simulation Settings
    "https://swatplus.gitbook.io/io-docs/introduction-1/simulation-settings/time.sim",
    "https://swatplus.gitbook.io/io-docs/introduction-1/simulation-settings/print.prt",
    "https://swatplus.gitbook.io/io-docs/introduction-1/simulation-settings/object.prt",
    "https://swatplus.gitbook.io/io-docs/introduction-1/simulation-settings/object.cnt",
    "https://swatplus.gitbook.io/io-docs/introduction-1/simulation-settings/constituents.cs",
]

# Known GitBook URL path -> MkDocs output file (relative to docs/)
URL_TO_FILE = {
    "/io-docs":                                                    "index.md",
    "/io-docs/introduction/basin":                                 "introduction/watershed-configuration.md",
    "/io-docs/introduction/calibration":                           "introduction/calibration.md",
    "/io-docs/introduction-1/input-file-format":                   "input-files/input-file-format.md",
    "/io-docs/introduction-1/master-file-file.cio":                "input-files/master-file.md",
    "/io-docs/introduction-1/simulation-settings":                 "input-files/simulation-settings/index.md",
    "/io-docs/introduction-1/climate":                             "input-files/climate/index.md",
    "/io-docs/introduction-1/climate/weather-sta.cli":             "input-files/climate/weather-sta-cli.md",
    "/io-docs/introduction-1/climate/weather-wgn.cli":             "input-files/climate/weather-wgn-cli.md",
    "/io-docs/introduction-1/climate/pcp.cli-and-precipitation-data-files":   "input-files/climate/pcp-cli.md",
    "/io-docs/introduction-1/climate/tmp.cli-and-temperature-data-files":     "input-files/climate/tmp-cli.md",
    "/io-docs/introduction-1/climate/hmd.cli-and-humidity-data-files":        "input-files/climate/hmd-cli.md",
    "/io-docs/introduction-1/climate/slr.cli-and-solar-radiation-data-files": "input-files/climate/slr-cli.md",
    "/io-docs/introduction-1/climate/wnd.cli-and-wind-speed-data-files":      "input-files/climate/wnd-cli.md",
    "/io-docs/introduction-1/climate/atmo.cli":                    "input-files/climate/atmo-cli.md",
    "/io-docs/introduction-1/basin-1":                             "input-files/basin-1/index.md",
    "/io-docs/introduction-1/landscape-units":                     "input-files/landscape-units/index.md",
    "/io-docs/introduction-1/routing-units":                       "input-files/routing-units/index.md",
    "/io-docs/introduction-1/hydrologic-response-units":           "input-files/hru/index.md",
    "/io-docs/introduction-1/hydrology":                           "input-files/hydrology/index.md",
    "/io-docs/introduction-1/soils":                               "input-files/soils/index.md",
    "/io-docs/introduction-1/landuse-and-management":              "input-files/landuse-management/index.md",
    "/io-docs/introduction-1/decision-tables":                     "input-files/decision-tables/index.md",
    "/io-docs/introduction-1/management-practices":                "input-files/management-practices/index.md",
    "/io-docs/introduction-1/structural-practices":                "input-files/structural-practices/index.md",
    "/io-docs/introduction-1/databases":                           "input-files/databases/index.md",
    "/io-docs/introduction-1/aquifers":                            "input-files/aquifers/index.md",
    "/io-docs/introduction-1/modflow":                             "input-files/gwflow.md",
    "/io-docs/introduction-1/channels":                            "input-files/channels/index.md",
    "/io-docs/introduction-1/reservoirs":                          "input-files/reservoirs/index.md",
    "/io-docs/introduction-1/wetlands":                            "input-files/wetlands/index.md",
    "/io-docs/introduction-1/initialization":                      "input-files/initialization/index.md",
    "/io-docs/introduction-1/constituents":                        "input-files/constituents/index.md",
    "/io-docs/introduction-1/point-sources-and-inlets":            "input-files/point-sources/index.md",
    "/io-docs/introduction-1/connectivity":                        "input-files/connectivity/index.md",
    "/io-docs/introduction-1/water-allocation":                    "input-files/water-allocation/index.md",
    "/io-docs/introduction-1/calibration":                         "input-files/calibration/index.md",
    "/io-docs/swat+-output-files/output-file-format":              "output-files/output-file-format.md",
    "/io-docs/swat+-output-files/debugging-outputs":               "output-files/debugging-outputs.md",
    "/io-docs/swat+-output-files/soil":                            "output-files/soil.md",
    "/io-docs/swat+-output-files/management":                      "output-files/management.md",
    "/io-docs/swat+-output-files/flow-duration-curve":             "output-files/flow-duration-curve.md",
    "/io-docs/swat+-output-files/water-balance":                   "output-files/water-balance.md",
    "/io-docs/swat+-output-files/nutrient-balance":                "output-files/nutrient-balance.md",
    "/io-docs/swat+-output-files/losses":                          "output-files/losses.md",
    "/io-docs/swat+-output-files/plant-and-weather":               "output-files/plant-and-weather.md",
    "/io-docs/swat+-output-files/channel":                         "output-files/channel.md",
    "/io-docs/swat+-output-files/aquifer":                         "output-files/aquifer.md",
    "/io-docs/swat+-output-files/reservoir":                       "output-files/reservoir.md",
    "/io-docs/swat+-output-files/recall":                          "output-files/recall.md",
    "/io-docs/swat+-output-files/hydrographs":                     "output-files/hydrographs.md",
    "/io-docs/swat+-output-files/routing-unit":                    "output-files/routing-unit.md",
    "/io-docs/swat+-output-files/pesticides":                      "output-files/pesticides.md",
    "/io-docs/swat+-output-files/object-outputs":                  "output-files/object-outputs.md",
}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
}


# ---------------------------------------------------------------------------
# Markdown converter
# ---------------------------------------------------------------------------

class GitbookConverter(MarkdownConverter):

    def convert_pre(self, el, text, **kwargs):
        # Pass through pre-built markdown table placeholders verbatim
        if el.get("data-md-table") or el.get("data-math"):
            return el.string or ""
        code = el.find("code")
        lang = ""
        if code:
            for c in code.get("class", []):
                if c.startswith("language-"):
                    lang = c[len("language-"):]
                    break
            text = code.get_text()
        return f"\n\n```{lang}\n{text.strip()}\n```\n\n"

    def convert_code(self, el, text, **kwargs):
        """Inline code — preserve as `code` span."""
        # Don't double-wrap if inside a <pre>
        if el.parent and el.parent.name == "pre":
            return text
        return f"`{text.strip()}`" if text.strip() else ""

    def convert_a(self, el, text, **kwargs):
        href = el.get("href", "")
        if not href or href.startswith("#"):
            return text or ""
        return f"[{text}]({href})"

    def convert_svg(self, el, text, **kwargs):
        return ""

    def convert_sub(self, el, text, **kwargs):
        """Subscript — use HTML passthrough for MkDocs."""
        return f"<sub>{text}</sub>"

    def convert_sup(self, el, text, **kwargs):
        """Superscript — use HTML passthrough for MkDocs."""
        return f"<sup>{text}</sup>"

    def convert_em(self, el, text, **kwargs):
        """Italic — used for variable names in SWAT+ docs."""
        return f"*{text}*" if text.strip() else ""

    def convert_strong(self, el, text, **kwargs):
        return f"**{text}**" if text.strip() else ""


_converter = GitbookConverter(heading_style="ATX", bullets="-")


# ---------------------------------------------------------------------------
# Pre-processing helpers
# ---------------------------------------------------------------------------

def clean_headings(content: Tag):
    """Remove anchor links and SVG icons GitBook injects into headings."""
    for heading in content.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        for a in heading.find_all("a"):
            if a.get("href", "").startswith("#"):
                a.decompose()
        for svg in heading.find_all("svg"):
            svg.decompose()
    return content


def _cell_to_md(cell: Tag) -> str:
    md = _converter.convert(str(cell))
    return re.sub(r'\s+', ' ', md).strip()


def convert_gitbook_tables(content: Tag, root: BeautifulSoup) -> Tag:
    """
    Convert GitBook's ARIA div-tables (role=table/row/cell/columnheader) to
    GFM markdown tables injected as <pre data-md-table> placeholders.
    """
    for table_div in content.find_all("div", {"role": "table"}):
        header_rows = []
        prev = table_div.find_previous_sibling("div", {"role": "rowgroup"})
        if prev:
            for row in prev.find_all("div", {"role": "row"}):
                hdrs = [_cell_to_md(h)
                        for h in row.find_all("div", {"role": "columnheader"})]
                if hdrs:
                    header_rows.append(hdrs)

        body_rows = []
        for row in table_div.find_all("div", {"role": "row"}):
            cells = [_cell_to_md(c) for c in row.find_all("div", {"role": "cell"})]
            if cells:
                body_rows.append(cells)

        if not header_rows and not body_rows:
            continue

        all_rows = header_rows + body_rows
        n_cols   = max(len(r) for r in all_rows)

        def pad(rows):
            return [r + [""] * (n_cols - len(r)) for r in rows]

        header_rows = pad(header_rows)
        body_rows   = pad(body_rows)
        all_rows    = header_rows + body_rows
        col_w = [max(max(len(all_rows[i][j]) for i in range(len(all_rows))), 3)
                 for j in range(n_cols)]

        def fmt(row):
            return "| " + " | ".join(c.ljust(col_w[j]) for j, c in enumerate(row)) + " |"

        sep = "| " + " | ".join("-" * w for w in col_w) + " |"
        lines = ([fmt(header_rows[0]), sep] + [fmt(r) for r in body_rows]
                 if header_rows else
                 [fmt(body_rows[0]), sep] + [fmt(r) for r in body_rows[1:]])

        placeholder = root.new_tag("pre")
        placeholder["data-md-table"] = "1"
        placeholder.string = "\n\n" + "\n".join(lines) + "\n\n"
        if prev:
            prev.replace_with("")
        table_div.replace_with(placeholder)

    return content


# ---------------------------------------------------------------------------
# Image downloader
# ---------------------------------------------------------------------------

def download_image(proxy_url: str) -> str | None:
    """
    Download a GitBook proxy image to IMAGES_DIR.
    Returns the filename (e.g. 'a3f1bc9d2e4a7f81.png') or None on failure.
    Uses the MD5 of the real URL as a stable filename so images are only
    downloaded once even if the scraper is re-run.
    """
    parsed   = urlparse(proxy_url)
    params   = parse_qs(parsed.query)
    real_url = unquote(params.get("url", [""])[0]) or proxy_url

    ext = os.path.splitext(urlparse(real_url).path)[1].lower()
    if ext not in (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"):
        ext = ".png"

    fname    = hashlib.md5(real_url.encode()).hexdigest()[:16] + ext
    out_path = os.path.join(IMAGES_DIR, fname)

    if os.path.exists(out_path):
        return fname  # already downloaded

    try:
        r = requests.get(proxy_url, headers=HEADERS, timeout=20)
        r.raise_for_status()
        os.makedirs(IMAGES_DIR, exist_ok=True)
        with open(out_path, "wb") as fh:
            fh.write(r.content)
        return fname
    except Exception as e:
        print(f"  [IMG] {proxy_url[:70]}... -> {e}")
        return None


def localise_images(content: Tag, doc_rel: str) -> Tag:
    """
    For every <img> in content whose src is a GitBook proxy URL,
    download the image locally and replace the src with a relative
    path from the current doc to docs/assets/images/.
    """
    doc_dir = os.path.dirname(doc_rel)   # e.g. "input-files/climate"
    depth   = len([p for p in doc_dir.split("/") if p])
    prefix  = ("../" * depth) + "assets/images/"

    for img in content.find_all("img"):
        raw_src = img.get("src", "")
        if not raw_src:
            continue
        if "~gitbook/image" in raw_src:
            fname = download_image(raw_src)
            if fname:
                img["src"] = prefix + fname
        # External / non-GitBook images: leave absolute URL as-is
    return content


# ---------------------------------------------------------------------------
# Link rewriter
# ---------------------------------------------------------------------------

def rewrite_links(md_text: str, current_doc_rel: str) -> str:
    """Replace GitBook internal links with correct relative MkDocs paths."""
    current_dir = os.path.dirname(current_doc_rel)

    def replace(m):
        link_text = m.group(1)
        target    = m.group(2)

        fragment = ""
        if "#" in target:
            target, frag = target.split("#", 1)
            fragment = "#" + frag

        if target.startswith(GITBOOK_BASE):
            path = target[len(GITBOOK_BASE):]
        elif target.startswith("/io-docs"):
            path = target
        else:
            return m.group(0)

        path = path.rstrip("/")

        # Link points to an excluded section (e.g. theoretical-documentation)
        # -> convert to absolute GitBook URL so the link still works externally
        if any(seg in path for seg in BLOCKED_SEGMENTS):
            abs_url = GITBOOK_BASE + path + fragment
            return f"[{link_text}]({abs_url})"

        target_file = URL_TO_FILE.get(path)

        if target_file is None:
            target_file = (path.lstrip("/")
                           .replace("io-docs/", "", 1)
                           .replace("introduction-1/", "input-files/")
                           .replace("swat+-output-files/", "output-files/"))
            target_file = re.sub(r'[^a-z0-9/_.\\-]', '-', target_file, flags=re.I)
            if not target_file.endswith(".md"):
                target_file += ".md"

        rel = os.path.relpath(target_file, current_dir).replace(os.sep, "/")
        return f"[{link_text}]({rel}{fragment})"

    return re.sub(r'\[([^\]]*)\]\(([^)]+)\)', replace, md_text)


# ---------------------------------------------------------------------------
# KaTeX equation extractor
# ---------------------------------------------------------------------------

def extract_katex(content: Tag) -> Tag:
    """
    KaTeX renders each equation as:
      <span class="katex">
        <span class="katex-mathml">
          <math><semantics>
            <annotation encoding="application/x-tex">RAW LATEX</annotation>
          </semantics></math>
        </span>
        <span class="katex-html">...visual spans...</span>
      </span>

    We extract the raw LaTeX from the <annotation> tag and replace the entire
    katex span with a plain text node: $latex$ or $$latex$$ (display).
    MathJax in MkDocs then renders these correctly.
    """
    for katex_span in content.find_all("span", {"class": "katex"}):
        annotation = katex_span.find("annotation",
                                     {"encoding": "application/x-tex"})
        if not annotation:
            continue

        latex = annotation.get_text(strip=True)

        # Display equation: parent span has class "katex-display"
        parent = katex_span.parent
        parent_classes = " ".join(parent.get("class", [])) if parent else ""
        is_display = "katex-display" in parent_classes

        # Replace the entire katex span (or its display wrapper) with a
        # Use a <pre data-math> placeholder — same as tables.
        # markdownify passes these verbatim so LaTeX is never escaped.
        ph = BeautifulSoup("<pre></pre>", "html.parser").find("pre")
        ph["data-math"] = "1"
        ph.string = (f"\n\n$$\n{latex}\n$$\n\n" if is_display
                     else f"${latex}$")

        target = parent if is_display else katex_span
        target.replace_with(ph)

    return content


# ---------------------------------------------------------------------------
# Content extraction
# ---------------------------------------------------------------------------

def extract_content(soup: BeautifulSoup, doc_rel: str = "") -> str:
    content = (
        soup.find("main") or
        soup.find("article") or
        soup.find("div", {"role": "main"}) or
        soup.find("div", {"class": re.compile(r"page-content|prose|markdown")})
    )
    if not content:
        return "*(No content extracted)*"

    for tag in content.find_all(["nav", "footer", "aside", "header"]):
        tag.decompose()
    for tag in content.find_all(attrs={"class": re.compile(
            r"table-of-contents|sidebar|feedback|edit-on|pagination")}):
        tag.decompose()

    clean_headings(content)
    if USE_PLAYWRIGHT:
        extract_katex(content)       # extract LaTeX from KaTeX-rendered equations
    if doc_rel:
        localise_images(content, doc_rel)
    convert_gitbook_tables(content, soup)

    md = _converter.convert(str(content))
    md = re.sub(r'\n{4,}', '\n\n\n', md)
    return md.strip()


def extract_page_title(soup: BeautifulSoup) -> str:
    h1 = soup.find("h1")
    if h1:
        return h1.get_text(strip=True)
    t = soup.find("title")
    return t.get_text(strip=True).split("|")[0].strip() if t else "Untitled"


# ---------------------------------------------------------------------------
# Crawl helpers
# ---------------------------------------------------------------------------

_playwright_ctx = None


def get_browser_page():
    """Return (playwright, browser, page) — created once, reused every fetch."""
    global _playwright_ctx
    if _playwright_ctx is None:
        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            print("\n  playwright not installed. Run:")
            print("    pip install playwright && playwright install chromium\n")
            raise
        pw      = sync_playwright().start()
        browser = pw.chromium.launch(headless=True)
        page    = browser.new_page(user_agent=HEADERS["User-Agent"])
        _playwright_ctx = (pw, browser, page)
    return _playwright_ctx


def close_browser():
    """Shut down the persistent browser if it was opened."""
    global _playwright_ctx
    if _playwright_ctx:
        pw, browser, _ = _playwright_ctx
        browser.close()
        pw.stop()
        _playwright_ctx = None


def fetch(url: str) -> str:
    """
    Fetch a page.
    --playwright : persistent headless Chromium so JS/KaTeX fully renders.
    default      : fast requests-based fetch.
    """
    if USE_PLAYWRIGHT:
        _, _, page = get_browser_page()
        page.goto(url, wait_until="networkidle", timeout=30000)
        try:
            page.wait_for_selector(".katex, main", timeout=8000)
        except Exception:
            pass
        return page.content()
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.text


def is_allowed(url: str) -> bool:
    path = urlparse(url).path
    if any(seg in path for seg in BLOCKED_SEGMENTS):
        return False
    return any(path.startswith(p) for p in ALLOWED_PREFIXES)


def normalise_url(href: str, current_url: str):
    full   = urljoin(current_url, href)
    parsed = urlparse(full)
    if parsed.netloc != DOMAIN:
        return None
    clean = parsed.scheme + "://" + parsed.netloc + parsed.path.rstrip("/")
    if any(seg in parsed.path for seg in ["~gitbook", "/api/", "/cdn-cgi/"]):
        return None
    return clean


def extract_page_links(soup: BeautifulSoup, current_url: str) -> list:
    """
    Discover all internal GitBook links on the page by scanning the full
    document. The sidebar is a plain <div> (not <nav>), and sub-pages are
    often only linked inline in the page body — so scanning everything is
    the only reliable way to discover them all.
    """
    seen  = set()
    links = []
    for a in soup.find_all("a", href=True):
        url = normalise_url(a["href"], current_url)
        if url and is_allowed(url) and url not in seen:
            seen.add(url)
            links.append(url)
    return links


def url_path(url: str) -> str:
    return urlparse(url).path.rstrip("/")


def derive_rel_path(path: str) -> str:
    rel = (path.lstrip("/")
               .replace("io-docs/", "", 1)
               .replace("introduction-1/", "input-files/")
               .replace("swat+-output-files/", "output-files/"))
    rel = re.sub(r'[^a-z0-9/_.\\-]', '-', rel, flags=re.I)
    return rel if rel.endswith(".md") else rel + ".md"


# ---------------------------------------------------------------------------
# Crawl
# ---------------------------------------------------------------------------

def crawl() -> OrderedDict:
    queue   = [BASE_URL] + SEED_URLS
    visited = set()
    pages   = OrderedDict()

    print("Crawling SWAT+ GitBook ...")
    print("Sections: Introduction | Input Files | Output Files")
    print("=" * 55)

    while queue:
        url  = queue.pop(0)
        norm = normalise_url(url, url)
        if norm in visited:
            continue
        visited.add(norm)

        if not is_allowed(url):
            continue

        try:
            html  = fetch(url)
            soup  = BeautifulSoup(html, "html.parser")
            title = extract_page_title(soup)
            path  = url_path(norm)
            rel   = URL_TO_FILE.get(path) or derive_rel_path(path)
            md    = extract_content(soup, rel)
            pages[norm] = (title, md, url, rel)

            for link in extract_page_links(soup, url):
                ln = normalise_url(link, link)
                if ln and ln not in visited and link not in queue:
                    queue.append(link)

            print(f"  [{len(pages):>3}] {title[:65]}")
            time.sleep(DELAY)

        except Exception as e:
            print(f"  [ERR] {url}  ->  {e}")

    return pages


# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------

def save(pages: OrderedDict):
    for norm, (title, md, url, rel) in pages.items():
        md_final = rewrite_links(md, rel)
        out = os.path.join(DOCS_DIR, rel)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"<!-- Source: {url} -->\n\n")
            f.write(md_final + "\n")
    print(f"\nSaved {len(pages)} pages to {DOCS_DIR}/")


# ---------------------------------------------------------------------------
# Auto-generate mkdocs.yml nav
# ---------------------------------------------------------------------------

def build_nav(pages: OrderedDict) -> list:
    """
    Build a fully recursive MkDocs nav from the crawled pages, preserving
    crawl order. Handles arbitrary nesting depth using navigation.indexes.
    """
    ordered   = [(rel, title) for _, (title, _, _, rel) in pages.items()]
    all_paths = OrderedDict(ordered)
    root_page = all_paths.pop("index.md", None)

    secs = {
        "introduction": OrderedDict(),
        "input-files":  OrderedDict(),
        "output-files": OrderedDict(),
    }
    for rel, title in all_paths.items():
        top = rel.split("/")[0]
        if top in secs:
            secs[top][rel] = title

    def _subdir_nav(paths, prefix, sd, section_file):
        sub_prefix    = (prefix + "/" + sd) if prefix else sd
        idx_path      = sub_prefix + "/index.md"
        idx_title     = paths.get(idx_path)
        section_index = (idx_title, idx_path) if idx_title else section_file
        label         = section_index[0] if section_index \
                        else sd.replace("-", " ").title()

        exclude = {idx_path}
        if section_file:
            exclude.add(section_file[1])

        children_paths = OrderedDict(
            (p, t) for p, t in paths.items()
            if p.startswith(sub_prefix + "/") and p not in exclude
        )
        children_nav = nav_list(children_paths, sub_prefix)

        if not children_nav and section_index:
            return [{label: section_index[1]}]
        else:
            ch = ([section_index[1]] if section_index else []) + children_nav
            return [{label: ch}]

    def nav_list(paths: OrderedDict, prefix: str) -> list:
        emitted = set()
        result  = []
        for path, title in paths.items():
            rel   = path[len(prefix) + 1:] if prefix else path
            parts = rel.split("/")
            if len(parts) == 1:
                if parts[0] == "index.md":
                    continue
                stem       = parts[0].rsplit(".", 1)[0]
                sub_prefix = (prefix + "/" + stem) if prefix else stem
                has_subdir = any(p.startswith(sub_prefix + "/") for p in paths)
                if has_subdir:
                    if stem not in emitted:
                        emitted.add(stem)
                        result.extend(_subdir_nav(paths, prefix, stem,
                                                  section_file=(title, path)))
                else:
                    result.append({title: path})
            else:
                sd = parts[0]
                if sd not in emitted:
                    emitted.add(sd)
                    result.extend(_subdir_nav(paths, prefix, sd,
                                              section_file=None))
        return result

    intro_items = (["index.md"] if root_page else []) + \
                  nav_list(secs["introduction"], "introduction")

    return [
        {"Introduction": intro_items},
        {"Input Files":  nav_list(secs["input-files"],  "input-files")},
        {"Output Files": nav_list(secs["output-files"], "output-files")},
    ]


def update_mkdocs_yml(nav: list):
    """Surgically replace only the nav: block, preserving all other config."""
    class IndentDumper(yaml.Dumper):
        def increase_indent(self, flow=False, indentless=False):
            return super().increase_indent(flow=flow, indentless=False)

    nav_yaml = yaml.dump(
        {"nav": nav}, Dumper=IndentDumper,
        default_flow_style=False, allow_unicode=True, sort_keys=False
    )

    with open(MKDOCS_YML, "r", encoding="utf-8") as f:
        original = f.read()

    nav_match   = re.search(r'^nav:', original, re.MULTILINE)
    new_content = original[:nav_match.start()] + nav_yaml if nav_match \
                  else original.rstrip() + "\n\n" + nav_yaml

    with open(MKDOCS_YML, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Updated nav in {MKDOCS_YML}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    pages = crawl()
    print("\nWriting files ...")
    save(pages)
    print("Updating mkdocs.yml nav ...")
    nav = build_nav(pages)
    update_mkdocs_yml(nav)
    close_browser()   # clean up Playwright if it was used
    print("\nDone! Run:  mkdocs serve")
