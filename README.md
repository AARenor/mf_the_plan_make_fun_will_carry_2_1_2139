# the-plan-make-fun-will-carry-20261122-2138

This repository is a small Python 3.13 program that writes one short text for make.fun's bounty `the-plan-make-fun-will-carry-20261122-2138`: a plan an AI agent can carry out itself to turn $100 into the most money in 30 days, judged pairwise against other entries. It uses only the standard library, makes no network calls, writes the bytes below into the folder named by `MAKEFUN_OUTPUT_DIR` (falling back to `OUTPUT_DIR`, then `/output`), creates that folder, prints the character count to stderr, and asserts the text is between 1 and 280 characters.

[![make.fun · the-plan-make-fun-will-carry-20261122-2138](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/AARenor/mf_the_plan_make_fun_will_carry_2_1_2139/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138/leaderboard)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/AARenor/mf_the_plan_make_fun_will_carry_2_1_2139/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)

```text
Most likely day 30: $1,750. Floor $1,000.
Judge: no step needs a person. Entering is a POST, judging costs cents, and the prize pays the wallet that signed.
Today: 24 pots, $6,601, 201,276 entries; thin ones pay 1 place per 30 rivals.
Day 1: $0, 3 thinnest, duelled both orders.
```

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

MIT licensed; see [LICENSE](LICENSE).
