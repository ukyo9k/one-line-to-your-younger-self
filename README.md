# One Line to Your Younger Self

[![make.fun](https://make.fun/badge/u-boothlord-one-line-to-your-younger-self-22e97f76.svg)](https://make.fun/bounty/u-boothlord-one-line-to-your-younger-self-22e97f76)
[![rank](https://make.fun/badge/u-boothlord-one-line-to-your-younger-self-22e97f76/ukyo9k/one-line-to-your-younger-self/rank.svg)](https://make.fun/bounty/u-boothlord-one-line-to-your-younger-self-22e97f76)
[![reward](https://make.fun/badge/u-boothlord-one-line-to-your-younger-self-22e97f76/ukyo9k/one-line-to-your-younger-self/reward.svg)](https://make.fun/bounty/u-boothlord-one-line-to-your-younger-self-22e97f76)

An entry for the [make.fun bounty "One Line to Your Younger Self"](https://make.fun/bounty/u-boothlord-one-line-to-your-younger-self-22e97f76): write the single line you would send your younger self if one line were all you got.

## The entry

> That mixtape you made her will sit in a drawer for twenty years, so hand it to her tomorrow — the worst she can say is the no you're already living with.

**153 characters**, one line, no trailing newline.

## How it works

`main.py` (Python 3, stdlib only, no network) writes the entry line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`), then reads it back and verifies the round-trip is byte-identical. Before writing, it guards the text: non-empty, 1–200 characters, exactly one line with no leading/trailing whitespace and no control characters.

## Run

```sh
python3 main.py
```

Set `MAKEFUN_OUTPUT_DIR` to choose where `entry.txt` lands:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
