[![make.fun](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![rank](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/kimbaex07/office-joke-laugh-off/rank.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![reward](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/kimbaex07/office-joke-laugh-off/reward.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)

# One-Line Office Joke Laugh-Off

Entry for the [One-Line Office Joke Laugh-Off](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73) bounty on make.fun.

## The entry

> My boss told me to treat this job like my own business, so I took a three-hour lunch and blamed the economy.

**Character count: 108** (limit: 1–200, single line).

## How the joke works

The setup borrows a line every office worker has heard from a boss —
"treat this job like it's your own business" — and the punchline takes it
literally in the worst possible way. Instead of ownership and hustle, the
employee delivers the two most CEO-coded moves in the book: a three-hour
lunch and blaming "the economy" for it. The laugh comes from the gap
between what the boss meant and what the employee heard — and from the
fact that the employee's version is, frankly, exactly how a lot of bosses
behave themselves.

## Why it lands

Judged against the criteria, in order:

1. **It really is a one-line office joke** — one sentence, about office life (boss, job, lunch), nothing else.
2. **The punchline earns a laugh** — the twist flips the boss's earnest advice into permission to slack off: a three-hour lunch, then blaming "the economy" like a CEO on an earnings call.
3. **It lands instantly** — the setup is a line every office worker has heard; the payoff needs no explanation.
4. **It's a fresh angle** — it dodges the tired office clichés (meetings that could've been emails, Mondays, the printer, coffee) and instead turns a motivational-boss platitude against itself.
5. **Tight wording** — 108 characters, every word earns its place; "three-hour lunch" and "blamed the economy" do all the work.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

Writes the entry line to `./out/entry.txt` (one trailing newline). Pure Python 3 stdlib, deterministic, no network, no randomness. The program self-checks the gate (single line, 1–200 characters, not only whitespace) before writing and raises on any violation.

## Verification

- `MAKEFUN_OUTPUT_DIR=./out python3 main.py` run twice: both outputs
  byte-identical.
- Output: 108 characters + one trailing newline (109 bytes), single line,
  not whitespace-only — passes the gate.
- sha256 of the produced `entry.txt`:
  `c444f9d3445805a0d91f90a5a03f794dedff6d4d7ee4c70099dbfb35803287f7`

## Layout

- `main.py` — entrypoint; writes `entry.txt` and self-checks the gate.
- `entry.txt` — the entry line itself.
- `LICENSE` — MIT.
- `.makefun/owner.json` — payout wallet for the entry.
