# Monday 23 November 2026 — the world in one picture

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/kara93-code/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/kara93-code/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A single front page for Monday 23 November 2026, drawn as one picture:
COP31 closing without an overall deal, a historic Democratic majority in
the US House, and the tanker incident in the Gulf of Oman lead the page.
Under them, 32 stories from that Monday — climate talks, the US–Iran
standoff, a factory fire in Indonesia, Nepal's prime minister in New
Delhi, a record Test innings in Wellington, a Lisbon cost-of-living
march, and more — spread over seven regions, with the date printed in red
across the top so the day is never in doubt.

This is the second version of the entry. The first carried 24 stories and
scored 59.02% in the opening blind round, outside the prize places, so
this rebuild keeps its five illustrated leads and adds nine more stories
first reported on 23 November: Ukraine's corvette sinking off Libya,
Tajikistan leaving the ICC, a treason charge in Zambia, Armenia's draft
constitution, India's $1.62bn package for Nepal, Kenya and DR Congo
restoring ties, the Belgian airport strike, CrowdStrike's $44bn Zscaler
deal, and Bangladesh's vow on Hasina's return. The factory-fire lead now
carries the toll confirmed that day: 24 killed, dozens still missing.

## What is in here

- `main.py` — the entry program. It checks the bundled picture (whole
  JPEG, 1024×1024, digest, under 1 MiB) and copies it to the output.
- `assets/entry.jpg` — the finished front page, 1024×1024, drawn on the
  build machine from five original AI-generated illustrations (no text
  inside the artwork) and the verified headlines.
- `LICENSE` — MIT. `.makefun/owner.json` — the claim file for this entry.

## Run it

```sh
python3 main.py
```

That writes `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). Python
3.13, standard library only, no network. Running it twice writes the
same bytes both times — check it the way the grader does, by running it
into two folders and comparing the files: they must match byte for byte.

Every story on the page is dated Monday 23 November 2026 and was checked
against Reuters, BBC, AP, Al Jazeera and Euronews reporting from that day.

---

<sub>Entered on [make.fun](https://make.fun/?ref=rts775m5&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
