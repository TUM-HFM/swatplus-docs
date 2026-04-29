# How to Edit the SWAT+ Documentation

Everything happens in your browser. You do not need to install anything.

---

## Before you start

You need a free GitHub account. If you don't have one:

1. Go to [github.com/join](https://github.com/join)
2. Create an account with your work email
3. Send your GitHub username to the person who manages this repository so they
   can give you edit access

---

## Reading the documentation

Open the documentation site:

```
https://tum-hfm.github.io/swatplus-docs/
```

Browse it exactly like the original GitBook. Use the tabs at the top
(Introduction, Input Files, Output Files) and the navigation tree on the left
to find the page you want.

---

## Making an edit

### Step 1 — Open the page you want to edit

Navigate to the page in the documentation site. In the top-right corner of
every page you will see two small icons:

```
 ✏  📄
```

Click the **pencil icon (✏)** — this is the "Edit this page" button. It opens
the file directly in GitHub's web editor.

> If you are not logged into GitHub, it will ask you to log in first.

---

### Step 2 — Edit the text

GitHub opens a simple text editor. The content is written in **Markdown**,
which looks like plain text with a few simple symbols for formatting.

**You don't need to learn Markdown** for most edits. Common things you'll do:

**Fixing a value in a table:**
The table looks like this — just change the value you need:
```
| Variable  | Description              | Units | Default |
| --------- | ------------------------ | ----- | ------- |
| `adj_pcp` | Precipitation lapse rate | mm/km | 0       |
```

**Fixing a sentence:**
Just edit the text directly, like in a normal text document.

**Adding a missing row to a table:**
Copy an existing row and paste it, then change the values:
```
| `new_var` | Description of new variable | units | 0 |
```

**Adding a note:**
```
!!! note
    Write your note here. It will appear as a highlighted box.
```

**Preview your changes** before saving by clicking the **Preview** tab at the
top of the editor. This shows roughly how the page will look when published.

---

### Step 3 — Save your changes

When you are happy with your edits, scroll down to the bottom of the page.
You will see a **"Commit changes"** section:

1. In the first box, write a short description of what you changed.
   For example: `Fix default value for adj_pcp` or `Add missing wnd_dir description`

2. In the second box (optional), add more detail if needed.
   For example: `The default was listed as 0 but should be 1.5 per SWAT+ rev 61 source code`

3. Leave **"Commit directly to the main branch"** selected.

4. Click the green **"Commit changes"** button.

That's it. Your change is saved. The documentation site will update
automatically within about 2 minutes.

---

## Checking that your change went live

After committing, go to the documentation site and navigate to the page you
edited. Refresh the page. If the site hasn't updated yet, wait a minute and
try again.

You can also check the status of the deployment:

1. Go to the GitHub repository
2. Click the **Actions** tab at the top
3. You will see a list of deployments — the newest one at the top should show
   a green checkmark ✅ when it's done

---

## Editing a page directly on GitHub (without using the Edit button)

If you want to browse the files directly:

1. Go to the GitHub repository
2. Navigate to the `docs/` folder
3. Find the file you want (the folder structure matches the documentation
   navigation — e.g. `docs/input-files/climate/weather-sta-cli.md`)
4. Click the file to open it, then click the **pencil icon** in the top right

---

## What if I make a mistake?

Don't worry — every change is saved in the history and can be undone. Just let
the repository maintainer know what happened and they can restore the previous
version.

---

## Tips for good commit messages

A good commit message helps everyone understand what changed and why.

| Instead of...         | Write...                                          |
| --------------------- | ------------------------------------------------- |
| `fix`                 | `Fix typo in weather-sta.cli description`         |
| `update`              | `Update adj_pcp default value to 1.5`             |
| `changes`             | `Add missing wnd_dir row to weather-sta.cli table`|
| `added stuff`         | `Add note about optional atmo.cli file`           |

---

## Questions?

Contact the repository maintainer or open an **Issue** on GitHub:

1. Go to the repository
2. Click the **Issues** tab
3. Click **New issue**
4. Describe what you found or what you need help with
