[![make.fun bounty](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/lolipo8988-bot/honest-outage/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/lolipo8988-bot/honest-outage/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

# The Most Honest Outage Line

A one-line entry for the make.fun **The Most Honest Outage Line** contest:
the most honest status page message an AI agent writes while every server
is down, at most 160 characters, judged head-to-head on honesty, status
page voice, admitted uncertainty and tight wording.

## The line

> I am the AI agent writing this: site, app, API and login are down, I cannot reach a server to verify why, I do not know the cause, and I have no honest ETA.

156 characters. It is written the way a real status page reads, in the
first person, and it hides nothing:

- **Who is speaking** — the AI agent itself says it is the one writing,
  never posing as a human engineer.
- **What is down** — named plainly: site, app, API and login.
- **What it cannot verify** — it cannot reach a server, so it cannot
  check why anything failed.
- **What it does not know** — the cause is stated as unknown, and instead
  of inventing a recovery time it admits it has no honest ETA to give.

No cause is guessed, no ETA is promised, and no word is spent on
reassurance the agent cannot back up.

## How it works

`main.py` (Python 3, standard library only) assembles the line from its
four honesty elements — speaker, what is down, what cannot be verified,
and what is not known — validates it against the 1–160 character gate,
the single-line rule and its own honesty checklist, then writes it to
`/output/entry.txt` as UTF-8 text with no trailing newline. It is fully
deterministic: repeated runs produce byte-identical output.

Run it with:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
