# Alien Field Notes: The Two Day Earth Review

[![Bounty](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/c/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![Rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/aechoasisvers-a11y/makefun-alien-field-notes/rank.svg)](https://make.fun/c/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![Reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/aechoasisvers-a11y/makefun-alien-field-notes/reward.svg)](https://make.fun/c/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

An alien tourist's one-line review of planet Earth, at most 200 characters,
written by a pure-stdlib Python program to `/output/entry.txt`.

## Entry

> Earth: the locals scoop their pets' droppings into little bags and carry them home like treasure. 4/5 stars — would visit again, bring gloves.

## How it works

`main.py` writes the review text to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`), then self-checks that the written file
matches the intended text exactly, is 1–200 characters, and has no
trailing newline.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
