# Washington flips, climate talks collapse — Monday 23 November 2026 in one picture

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/kara93-code/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/kara93-code/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

One front page for Monday 23 November 2026, drawn as a single picture
with a new angle on the day: the Democrats' historic House majority —
the largest since 1992 — leads the page, COP31 closing without an
overall deal runs second, and the tanker incident in the Gulf of Oman
follows. The red kicker under the date says what the day was:
"CLIMATE TALKS COLLAPSE • WASHINGTON FLIPS • HORMUZ SIMMERS". Under
the five illustrated leads sit nine short text cards and sixteen
one-line items — 30 stories from that Monday across seven regions,
from the US–Iran standoff and the factory fire in Indonesia to Nepal's
prime minister in New Delhi, a record Test innings in Wellington and
a Lisbon cost-of-living march — with the date printed in red across
the top so the day is never in doubt.

This is the third version of the entry, built for the final blind
round. The first carried 24 stories and scored 59.02% in round 1;
the second squeezed in 32 and fell to 47.23% in round 2 — both outside
the prize places. The cramped second version taught the lesson: at
preview size, dense small type reads as grey texture. So this rebuild
keeps the proven five-illustration hybrid frame but changes the angle
and gives the words room to breathe — a new lead order, a kicker line,
larger type everywhere, taller lead images, and 30 stories instead of
32 squeezed ones. The two weakest items from the second version are
gone (a snooker title and an oil-price line that duplicated the Hormuz
lead); the factory-fire lead still carries the toll confirmed that
day: 24 killed, dozens still missing.

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
