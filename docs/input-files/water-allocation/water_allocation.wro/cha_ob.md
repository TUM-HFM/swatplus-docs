# cha_ob

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/water-allocation/water_allocation.wro/cha_ob -->

| Option | Description        |
| ------ | ------------------ |
| yes    | One channel object |
| no     | No channel object  |

There cannot be more than one channel object per water allocation table.

If one of the source objects is a channel, the water allocation module is called from the channel control subroutine when the simulation reaches the ID of the source channel. Otherwise, the water allocation module is called from the time control subroutine. This is important, because during a model run, there is more variability in the availability of water in a channel than in a reservoir or aquifer. Therefore, the model needs to know the current availability of water in the source channel on the day a demand is triggered.

Last updated 1 year ago
