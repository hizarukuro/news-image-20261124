# REPORT — news-image-20261124: "THE WORLD IN ONE DAY"

## What this is
A single 1024×1024 front page summing up Tuesday 24 November 2026's world
news: 3 hero stories, 27 grid stories, 3 briefs (33 numbered stories in
total), a stat band of 5 figures, and a red DATE CHECK box that visibly
discards 14 Monday-or-earlier stories. All art is flat vector-style drawing
done with PIL shapes — no photos, no downloaded images or fonts.

## Story list and sources
Day: Tuesday 24 November 2026 (WIB day). Every item below was first reported
on that day, verified against Reuters / AP / BBC / Just Security / UN /
PR Newswire / WSJ / Conference Board reporting.

**Heroes**
1. **Gaza — strikes kill Hamas security chief.** Israeli strikes killed
   Naeem Abu Nahel, head of Hamas' internal security apparatus, and six
   others; the IDF/Shin Bet confirmed a senior militant was hit. Strikes also
   hit Khan Younis and the Netzarim corridor. (Reuters via Just Security
   Early Edition, 24 Nov.)
2. **Russia tests NATO's edges.** Moscow warned Estonia its moves are "on the
   verge of triggering open war" (Reuters). Russian aircraft entered South
   Korea's air-defence identification zone (AP / Joint Chiefs). An overnight
   strike on Zaporizhzhia city killed 2 and wounded 40, including 4 children
   (Reuters). Latvia's president said the war may reach a tipping point next
   year; Norway's defence minister spoke of continued dialogue with Ukraine.
3. **America's economy day.** US consumer confidence jumped to 103.3 in
   November, its best since January 2025, up from 91.9 (Conference Board).
   The administration was expected to release Section 301 findings on excess
   industrial capacity, with new duties possible as soon as Tuesday or
   Wednesday — shown as *expected*, not done (Reuters, sources). China
   extended its pause on gallium/germanium/antimony export curbs to
   27 Jan 2027. Asian markets surged: Nikkei +3.91%, Seoul +6%+. Sanofi
   agreed to buy Insmed for $41bn cash ($175/share), the biggest biotech deal
   in nearly three years (PR Newswire).

**Grid (04–30)** — UN femicide brief: 47,000 women and girls killed by a
partner or family member in 2025 (UNODC + UN Women); DRC fighting traps Ebola
responders near an Ituri hospital (WHO/UN News); Nepal 5.6 quake in Koshi;
~175 migrants missing off Senegal; Oregon and Virginia sue SpaceX over
alleged Grok-generated child sexual-abuse images; Iraq PM takes federal
control of Kurdish-area oilfields after a smuggling probe; Sweden schedules a
30 Nov vote on Kristersson staying PM; Lula backs a second fiscal package in
Brazil; South Korea offers up to $375,000 rewards to catch AI exam cheats
(WSJ); the US eyes Iran as a *possible* culprit in ship cyberattacks — shown
as reported, not confirmed (WSJ); car bomb in Villavicencio, Colombia, no
confirmed victims; 'El Chapo Isidro' to be tried in Mexico; Champions League
(Dortmund 4-0 Villarreal, Juventus 2-0 Benfica); Trump expects China to buy
250 more Boeing planes and offers to work with Democrats on a card-rate cap;
EU proposes banning Russian symbols at sports events; China opens Tiangong to
its first foreign astronaut, Pakistan's Zeeshan Ali; Pablo Hernández de Cos
tipped to succeed Lagarde at the ECB; Microsoft confirms an Azure API
Management zero-day used to steal customer credentials; the US Army will
detonate degrading explosives in Iowa on Wednesday after a court rejected a
stay; Sheikh Hasina plans to return to Bangladesh on 16 Dec, Dhaka says she
"will be brought back in handcuffs"; Japan's PM Takaichi pledges the full
2027 ICC contribution by year-end; Amnesty says Tigray artillery strikes
should be investigated as possible war crimes; the US discusses training
Syrian soldiers in demining; Ambassador Huckabee doubts the $3.8bn annual
military aid to Israel will end this year; the FDA approves the first
limb-girdle muscular dystrophy drug (BridgeBio); US measles cases reach
5,838 in 2026 (CDC, to 19 Nov); the EU will seek an overhaul of UN climate
decision-making after the COP31 failure.

**Briefs (31–33)** — the most distant glowing black hole found, a quasar
from the infant universe; Women's Champions League (Chelsea 1-0 PSG, Buurman
87', Man City 2-0 Häcken, Real Madrid 3-1 Inter, Juventus 2-0 Leuven); the
Brazilian real up 2% after Congress passed the first fiscal package.

**Stat band** — 103.3 (US consumer confidence), 40 (wounded in Zaporizhzhia),
60% (of femicides by a partner or family member), 630M (years after the Big
Bang — quasar), $41bn (Sanofi–Insmed deal).

**DATE CHECK (discarded, Monday 23 Nov or earlier)** — Nvidia reinstates
Huang as CEO; Ukraine sinks the corvette Merkury off Libya; COP31 ends with
no deal; CrowdStrike to buy Zscaler for $43.9bn; ICJ finds Myanmar committed
genocide against the Rohingya; US sanctions Iranian "shadow banking" networks;
Vance & Rubio meet the Qatari PM; EU–Indonesia trade deal signed; Belgium
airports shut by strike; Brazil cuts its 2027 growth forecast to 1.8%; NATO
chief Rutte on defending space; Trump directive to expedite federal death
sentences; US loses measles elimination status; UN briefing that the Gaza war
erased 77 years of human development. Each is shown with its date and a red
✕, explicitly not Tuesday news.

## Design notes
- Masthead names the day prominently; three equal hero panels, each with its
  own flat illustration (Gaza dusk skyline with a burst; NATO radar sweep
  with jets crossing a border line and a shield; rising bars with a trend
  arrow and a plane).
- One ordered story list in `render.py` drives every number on the page
  (heroes 01–03, grid 04–30, briefs 31–33), so numbering cannot drift.
- `main.py` is standard library only (os, shutil, sys, pathlib) and copies
  the shipped `entry.png` byte-identically to `$MAKEFUN_OUTPUT_DIR`.

## Tidiness audit (checked explicitly, all pass)
- **Numbering from one list:** PASS — a single `STORIES` list is enumerated
  per section; inspected render shows 01–33 in order with no gaps.
- **Uniform data chips:** PASS — one `draw_chip` helper (same pill, font,
  size) renders all three hero chips.
- **Uniform brief lead-ins:** PASS — every brief uses the same
  `NN KICKER` + bold headline + regular deck pattern, same capitalisation.
- **No figure duplicated between stat band and hero chips/grid items:**
  PASS — verified by script against the source text: 40, 60%, 630M and $41bn
  appear nowhere else on the page. 103.3 appears only in hero 3's own deck
  text (not in any chip or grid item). Fixes applied in review: the stat band
  dropped 175 (was grid 07) and 5.6 (was grid 06); hero 3's chip changed
  from 103.3 to "NIKKEI +3.91% · SEOUL +6%".
- **Balanced hero art density:** PASS — all three art panels fill their
  320×88 zone; a glow was added behind the Gaza burst to match the density
  of the other two.
- **Aligned columns/baselines:** PASS — grid decks sit on a fixed baseline
  (y+38) regardless of 1- or 2-line headlines; dividers sit below the deck
  line; no text crosses a rule.
- **No overflow/clipping:** PASS — inspected at full size and at ~300px;
  all headlines wrap to at most 2 lines, all decks are truncated with an
  ellipsis only where they still fit. Fixed during inspection: grid 28's deck
  was shortened so it no longer ends in "…", and a missing briefs-deck line
  (the strip originally drew headline only) was found and fixed — all three
  briefs now show headline + deck.
- **Headline/deck match:** PASS — grid 28's deck now describes the FDA drug
  approval (BridgeBio), and the quasar moved to brief 31, which no longer
  duplicates grid 21's deck.
- **Claims vs denials labelled:** PASS — the Iran attribution is labelled
  "— WSJ" with "attribution not confirmed"; the Section 301 duties are
  "expected Tue/Wed"; the Hasina return is "aide says" against Dhaka's
  "will be brought back in handcuffs".

## Verification
- `entry.png`: 1024×1024, 187,455 bytes (≤1 MiB).
- `main.py` run twice with `env -i` into two fresh output dirs: both outputs
  byte-identical to each other and to `entry.png` —
  sha256 `1c6d9526e93d648cf9494fa0f09b47509ae7d18aa89e344a7dd1537f6f614865`.
- `main.py` imports only os, shutil, sys, pathlib (stdlib).

## What I could not render faithfully
Nothing material. One judgement call: hero 1's deck was reworded to avoid
asserting that the Khan Younis / Netzarim deaths were additional to the 7 in
the chip, because the sources are ambiguous about whether they overlap.
