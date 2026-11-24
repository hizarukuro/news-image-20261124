#!/usr/bin/env python3
"""Render news-image-20261124 entry.png — PIL only, all art drawn by hand.

All numbering (heroes, grid, briefs) is generated programmatically from the
single ordered STORIES list below, so numbers can never drift apart.
"""
import math
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (253, 252, 247)
INK = (17, 17, 17)
MUTED = (90, 88, 80)
RULE = (200, 196, 184)
RED = (185, 28, 28)
NAVY = (30, 58, 95)
DARK = (24, 24, 24)

FD = "/usr/share/fonts/truetype/dejavu/"


def font(path, size):
    return ImageFont.truetype(path, size)


SERIF_B = lambda s: font(FD + "DejaVuSerif-Bold.ttf", s)
SANS_B = lambda s: font(FD + "DejaVuSans-Bold.ttf", s)
SANS = lambda s: font(FD + "DejaVuSans.ttf", s)

# ---------------------------------------------------------------- stories
# One ordered list drives every number on the page.
# Each item: (section, kicker, headline, deck, chip or None)
# section: "hero" | "grid" | "brief"
STORIES = [
    ("hero", "GAZA  ·  CONFLICT",
     "Strikes kill Hamas security chief",
     "Abu Nahel and six others killed; the IDF confirms a senior militant "
     "was hit. Strikes also hit Khan Younis and the Netzarim corridor.",
     "7 KILLED TUESDAY"),
    ("hero", "RUSSIA  ·  NATO",
     "Moscow warns Estonia: on the verge of open war",
     "Russian jets enter South Korea's air-defence zone; a strike on "
     "Zaporizhzhia kills 2. Latvia sees a tipping point.",
     "2 KILLED IN ZAPORIZHZHIA"),
    ("hero", "USA  ·  ECONOMY",
     "Confidence jumps; tariffs loom; China pauses curbs",
     "Confidence hits 103.3, its best since January 2025. Section 301 "
     "tariff findings expected Tue/Wed; Beijing extends its gallium pause.",
     "NIKKEI +3.91% · SEOUL +6%"),
    ("grid", "UNITED NATIONS",
     "47,000 women killed by partners or family in 2025",
     "Five every hour, 129 a day; Africa highest at 22,100."),
    ("grid", "DRC",
     "Fighting traps Ebola teams near Ituri hospital",
     "Responders under cover for 24+ hours as clashes rage."),
    ("grid", "NEPAL",
     "5.6 quake strikes Koshi near China border",
     "Tremor hits the eastern province on Tuesday."),
    ("grid", "SENEGAL",
     "\u2248175 migrants missing after boat loses contact",
     "Europe-bound boat left Dakar about two weeks ago."),
    ("grid", "USA",
     "Oregon, Virginia sue SpaceX over Grok images",
     "States allege AI-generated child sexual-abuse images."),
    ("grid", "IRAQ",
     "PM takes federal control of Kurdish-area oilfields",
     "Move follows an oil-smuggling probe; four provinces named."),
    ("grid", "SWEDEN",
     "Vote set on Kristersson staying prime minister",
     "Speaker schedules 30 Nov vote to end post-election gridlock."),
    ("grid", "BRAZIL",
     "Lula backs second fiscal package",
     "Aims to curb mandatory spending; first package passed."),
    ("grid", "SOUTH KOREA",
     "Rewards up to $375,000 to catch AI exam cheats",
     "Up to $75,000 per tipster; fair exams \u201cmust be protected\u201d."),
    ("grid", "US\u2013IRAN",
     "US eyes Iran in ship cyberattacks \u2014 WSJ",
     "Dozens of attacks reported; attribution not confirmed."),
    ("grid", "COLOMBIA",
     "Car bomb destroys buildings in Villavicencio",
     "No confirmed victims, the president says."),
    ("grid", "MEXICO",
     "\u2018El Chapo Isidro\u2019 to be tried in Mexico",
     "US extradition request set aside, for now."),
    ("grid", "FOOTBALL",
     "Dortmund 4-0 Villarreal; Juventus 2-0 Benfica",
     "Guirassy double; Thuram and McKennie score."),
    ("grid", "USA",
     "Trump: China to buy 250 more Boeing planes",
     "Also offers to work with Democrats on a card-rate cap."),
    ("grid", "EU",
     "EU proposes banning Russian symbols at sports events",
     "Part of a new Russia sanctions package."),
    ("grid", "CHINA",
     "Tiangong opens to first foreign astronaut",
     "Pakistan\u2019s Zeeshan Ali to join Shenzhou-24 mission."),
    ("grid", "ECB",
     "Hern\u00e1ndez de Cos tipped to succeed Lagarde",
     "Spaniard seen as the next ECB president."),
    ("grid", "TECH",
     "Microsoft: Azure zero-day stole customer credentials",
     "Firm confirms the exploit; PHP and Java flaws also flagged."),
    ("grid", "USA",
     "Army to detonate degrading explosives in Iowa",
     "Blast set for Wednesday after a court rejects a stay."),
    ("grid", "BANGLADESH",
     "Hasina plans return on 16 Dec, aide says",
     "Dhaka: she \u201cwill be brought back in handcuffs\u201d."),
    ("grid", "JAPAN",
     "Takaichi: Japan to pay full 2027 ICC contribution",
     "Payment to be made by the end of this year."),
    ("grid", "ETHIOPIA",
     "Amnesty: Tigray strikes may be war crimes",
     "Artillery on urban areas should be investigated."),
    ("grid", "US\u2013SYRIA",
     "US discusses training Syrian soldiers in demining",
     "Multinational mission faces US legal hurdles."),
    ("grid", "US\u2013ISRAEL",
     "Huckabee doubts $3.8bn aid to Israel will end",
     "Trump said aid would end by year\u2019s end."),
    ("grid", "HEALTH · SCIENCE",
     "FDA approves first limb-girdle dystrophy drug",
     "BridgeBio's treatment is the first for this disease."),
    ("grid", "HEALTH",
     "US measles cases reach 5,838 in 2026",
     "CDC count to 19 Nov; Michigan reports 37 cases."),
    ("grid", "CLIMATE",
     "EU to seek overhaul of UN climate decisions",
     "Move follows the COP31 failure; consensus rule in focus."),
    ("brief", "SCIENCE",
     "Most distant glowing black hole found",
     "A quasar shining from the infant universe."),
    ("brief", "FOOTBALL",
     "Women\u2019s UCL: Chelsea 1-0 PSG; City 2-0 H\u00e4cken",
     "Buurman 87\u2032; Real Madrid 3-1 Inter; Juve 2-0 Leuven."),
    ("brief", "MARKETS",
     "Brazil real strengthens 2% after first package passes",
     "Congress approval lifts the currency on Tuesday."),
]

STATS = [
    ("103.3", "US CONSUMER CONFIDENCE"),
    ("40", "WOUNDED IN ZAPORIZHZHIA"),
    ("60%", "OF FEMICIDES BY PARTNER OR FAMILY"),
    ("630M", "YEARS AFTER THE BIG BANG — QUASAR"),
    ("$41bn", "SANOFI\u2013INSMED DEAL"),
]

# Date-check: earlier stories, visibly discarded (never Tuesday news).
DISCARDED = [
    ("Nvidia reinstates Huang as CEO", "Mon 23 Nov"),
    ("Ukraine sinks corvette Merkury off Libya", "Mon 23 Nov"),
    ("COP31 ends with NO deal in Antalya", "Sun 22 Nov"),
    ("CrowdStrike to buy Zscaler, $43.9bn", "Mon 23 Nov"),
    ("ICJ: Myanmar committed Rohingya genocide", "Thu 19 Nov"),
    ("US sanctions Iranian \u201cshadow banking\u201d", "Mon 23 Nov"),
    ("Vance & Rubio meet Qatari PM", "Mon 23 Nov"),
    ("EU\u2013Indonesia trade deal signed", "Mon 23 Nov"),
    ("Belgium airports shut by strike", "Mon 23 Nov"),
    ("Brazil cuts 2027 growth forecast to 1.8%", "Mon 23 Nov"),
    ("NATO chief: alliance will defend space", "Mon 23 Nov"),
    ("Trump: expedite federal death sentences", "Mon 23 Nov"),
    ("US loses measles elimination status", "17 Nov"),
    ("UN: Gaza war erased 77 years of development", "Mon 23 Nov"),
]

# ---------------------------------------------------------------- helpers
_PROBE = ImageDraw.Draw(Image.new("RGB", (1, 1)))


def text_w(text, fnt):
    return _PROBE.textlength(text, font=fnt)


def wrap(text, fnt, max_w):
    """Greedy word wrap to a pixel width."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        if not words:
            lines.append("")
            continue
        cur = words[0]
        for w in words[1:]:
            if text_w(cur + " " + w, fnt) <= max_w:
                cur += " " + w
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def fit_one_line(text, fnt, max_w):
    """Truncate to one line with an ellipsis if it does not fit."""
    if text_w(text, fnt) <= max_w:
        return text
    while text and text_w(text + "\u2026", fnt) > max_w:
        text = text[:-1].rstrip()
    return text + "\u2026"


def draw_chip(d, x, y, text, fill=RED):
    """Uniform data chip: same pill, font and size everywhere."""
    fnt = SANS_B(11)
    tw = text_w(text, fnt)
    pad_x = 8
    d.rounded_rectangle([x, y, x + tw + 2 * pad_x, y + 19],
                        radius=9, fill=fill)
    d.text((x + pad_x, y + 3), text, font=fnt, fill=(255, 255, 255))
    return tw + 2 * pad_x


def kicker_line(d, x, y, num, kicker, color=RED, kicker_color=None):
    fnt = SANS_B(11)
    d.text((x, y), f"{num:02d}", font=fnt, fill=color)
    nw = text_w(f"{num:02d}", fnt)
    d.text((x + nw + 7, y), kicker, font=fnt,
           fill=kicker_color if kicker_color else INK)


# ---------------------------------------------------------------- hero art
def art_gaza(d, x, y, w, h):
    """Dusk sky, skyline, thin smoke wisps, one burst — flat shapes only."""
    d.rectangle([x, y, x + w, y + h], fill=(38, 44, 66))
    d.rectangle([x, y + h - 30, x + w, y + h], fill=(22, 24, 34))
    d.ellipse([x + w - 62, y + 10, x + w - 26, y + 46], fill=(232, 150, 60))
    rnd = random.Random(7)
    bx = x + 6
    while bx < x + w - 20:
        bw = rnd.randint(18, 34)
        bh = rnd.randint(26, 58)
        d.rectangle([bx, y + h - 30 - bh, bx + bw, y + h - 30], fill=(52, 58, 82))
        for wy in range(y + h - 26 - bh, y + h - 36, 12):
            for wx in range(bx + 4, bx + bw - 5, 10):
                if rnd.random() < 0.5:
                    d.rectangle([wx, wy, wx + 4, wy + 5], fill=(240, 200, 90))
        bx += bw + 5
    # thin smoke wisps rising from two rooftops
    for sx in (x + 60, x + 190):
        for i, (dx, r) in enumerate(((0, 4), (3, 5), (6, 6))):
            d.ellipse([sx + dx - r, y + 10 + i * 10, sx + dx + r,
                       y + 10 + i * 10 + 2 * r], fill=(95, 94, 90))
    # burst, with a soft glow behind it so the panel reads denser
    cx, cy = x + 150, y + 24
    d.ellipse([cx - 20, cy - 20, cx + 20, cy + 20], fill=(120, 70, 30))
    for ang in range(0, 360, 30):
        ex = cx + 24 * math.cos(math.radians(ang))
        ey = cy + 24 * math.sin(math.radians(ang))
        d.line([cx, cy, ex, ey], fill=(245, 180, 60), width=3)
    d.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], fill=(250, 205, 80))


def art_nato(d, x, y, w, h):
    """Radar sweep, jets crossing a border line, shield outline."""
    d.rectangle([x, y, x + w, y + h], fill=(24, 52, 84))
    cx, cy = x + 62, y + h - 8
    for r in (30, 55, 80):
        d.arc([cx - r, cy - r, cx + r, cy + r], start=270, end=360,
              fill=(120, 180, 220), width=2)
    d.line([cx, cy, cx + 78, y + 14], fill=(140, 200, 240), width=2)
    d.line([x + 150, y + 6, x + 150, y + h - 6], fill=(245, 200, 60), width=2)
    for jx, jy, col in ((x + 168, y + 30, (235, 235, 235)),
                        (x + 205, y + 62, (200, 210, 225)),
                        (x + 240, y + 22, (235, 235, 235))):
        d.polygon([(jx, jy), (jx + 34, jy + 7), (jx, jy + 14)], fill=col)
        d.polygon([(jx + 8, jy + 2), (jx + 20, jy + 7), (jx + 8, jy + 12)],
                  fill=(245, 200, 60))
    sx, sy = x + 268, y + 52
    d.polygon([(sx, sy), (sx + 34, sy + 8), (sx + 34, sy + 30),
               (sx + 17, sy + 44), (sx, sy + 30)], outline=(255, 255, 255), width=3)
    d.text((sx + 12, sy + 14), "\u2713", font=SANS_B(16), fill=(255, 255, 255))
    d.text((x + 8, y + 6), "KALININGRAD \u00b7 ESTONIA \u00b7 KOREA ADIZ",
           font=SANS_B(9), fill=(170, 205, 235))


def art_economy(d, x, y, w, h):
    """Rising bars, trend arrow, plane silhouette."""
    d.rectangle([x, y, x + w, y + h], fill=(16, 84, 74))
    base = y + h - 16
    vals = [22, 34, 30, 48, 44, 62, 78]
    bw, gap = 26, 8
    bx = x + 14
    for v in vals:
        d.rectangle([bx, base - v, bx + bw, base], fill=(245, 200, 60))
        bx += bw + gap
    d.line([x + 14, base - 20, x + 120, base - 46, x + 210, base - 66,
            x + 288, base - 80], fill=(255, 255, 255), width=4)
    d.polygon([(x + 288, base - 80), (x + 270, base - 80), (x + 288, base - 62)],
              fill=(255, 255, 255))
    px, py = x + 210, y + 16
    d.polygon([(px, py), (px + 46, py + 6), (px, py + 12)], fill=(235, 235, 235))
    d.polygon([(px + 12, py + 2), (px + 26, py + 6), (px + 12, py + 10)],
              fill=(200, 220, 235))
    d.text((x + 10, y + 6), "$  \u2191  CONFIDENCE 103.3", font=SANS_B(10),
           fill=(255, 255, 255))


ART = {0: art_gaza, 1: art_nato, 2: art_economy}

# ---------------------------------------------------------------- render
def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    heroes = [s for s in STORIES if s[0] == "hero"]
    grid = [s for s in STORIES if s[0] == "grid"]
    briefs = [s for s in STORIES if s[0] == "brief"]
    gap = 8
    hw = 320

    # ---- masthead
    d.text((24, 10), "THE WORLD IN ONE DAY", font=SERIF_B(44), fill=INK)
    d.text((24, 58), "TUESDAY 24 NOVEMBER 2026  ·  33 STORIES FROM EVERY REGION",
           font=SANS_B(13), fill=RED)
    d.text((W - 24 - text_w("ONE IMAGE · ONE DAY", SANS_B(11)), 60),
           "ONE IMAGE · ONE DAY", font=SANS_B(11), fill=MUTED)
    d.line([24, 80, W - 24, 80], fill=INK, width=2)

    # ---- heroes: 3 equal columns, 232 high
    hx0, hy0, hh = 24, 88, 232
    for i, s in enumerate(heroes):
        num = i + 1
        x = hx0 + i * (hw + gap)
        d.rectangle([x, hy0, x + hw, hy0 + hh], outline=RULE, width=1)
        d.rectangle([x, hy0, x + hw, hy0 + 26], fill=NAVY)
        kicker_line(d, x + 10, hy0 + 7, num, s[1], color=(245, 200, 60),
                    kicker_color=(255, 255, 255))
        ART[i](d, x + 1, hy0 + 27, hw - 2, 88)
        y = hy0 + 124
        for ln in wrap(s[2], SERIF_B(16), hw - 20)[:2]:
            d.text((x + 10, y), ln, font=SERIF_B(16), fill=INK)
            y += 20
        for ln in wrap(s[3], SANS(10), hw - 20)[:3]:
            d.text((x + 10, y), ln, font=SANS(10), fill=MUTED)
            y += 13
        draw_chip(d, x + 10, hy0 + hh - 28, s[4])

    # ---- stat band
    sy = 328
    d.rectangle([24, sy, W - 24, sy + 54], fill=DARK)
    seg_w = (W - 48) / len(STATS)
    for i, (fig, label) in enumerate(STATS):
        cx = 24 + seg_w * i + seg_w / 2
        fw = text_w(fig, SERIF_B(22))
        d.text((cx - fw / 2, sy + 5), fig, font=SERIF_B(22), fill=(245, 200, 60))
        lw = text_w(label, SANS_B(8))
        d.text((cx - lw / 2, sy + 33), label, font=SANS_B(8), fill=(220, 220, 220))
        if i:
            d.line([24 + seg_w * i, sy + 9, 24 + seg_w * i, sy + 45],
                   fill=(90, 90, 90), width=1)

    # ---- grid: 3 columns x 9 rows, numbered 04..30, 52px rows
    gx0, gy0, row_h = 24, 392, 52
    for idx, s in enumerate(grid):
        num = 4 + idx
        col, row = idx % 3, idx // 3
        x = gx0 + col * (hw + gap)
        y = gy0 + row * row_h
        kicker_line(d, x, y, num, s[1])
        hy = y + 14
        for ln in wrap(s[2], SERIF_B(12), hw)[:2]:
            d.text((x, hy), ln, font=SERIF_B(12), fill=INK)
            hy += 13
        # deck pinned to a fixed baseline so a 1- or 2-line headline
        # can never push it into the next row
        d.text((x, y + 38), fit_one_line(s[3], SANS(10), hw), font=SANS(10),
               fill=MUTED)
        if row < 8:
            d.line([x, y + row_h - 1, x + hw, y + row_h - 1], fill=RULE, width=1)

    # ---- briefs strip: numbered 31..33, each with kicker, headline, deck
    by = 864
    d.rectangle([24, by, W - 24, by + 58], fill=(238, 236, 228))
    d.text((34, by + 4), "BRIEFS", font=SANS_B(11), fill=RED)
    bw3 = (W - 48 - 20) / 3
    for i, s in enumerate(briefs):
        num = 31 + i
        x = 34 + i * (bw3 + 10)
        d.text((x, by + 19), f"{num:02d}", font=SANS_B(11), fill=RED)
        d.text((x + 26, by + 19), s[1], font=SANS_B(11), fill=INK)
        d.text((x, by + 32), fit_one_line(s[2], SANS_B(10), bw3 - 10),
               font=SANS_B(10), fill=INK)
        d.text((x, by + 44), fit_one_line(s[3], SANS(10), bw3 - 10),
               font=SANS(10), fill=MUTED)

    # ---- date check: 3 columns x 5 rows, red box, discarded
    dy = 928
    d.rectangle([24, dy, W - 24, H - 14], outline=RED, width=2)
    d.rectangle([24, dy, W - 24, dy + 20], fill=RED)
    d.text((34, dy + 3), "DATE CHECK \u2014 DISCARDED: NOT TUESDAY 24 NOVEMBER",
           font=SANS_B(12), fill=(255, 255, 255))
    col_w = 300
    for i, (title, when) in enumerate(DISCARDED):
        col, row = i // 5, i % 5
        x = 34 + col * (col_w + 20)
        y = dy + 28 + row * 11
        d.text((x, y), "\u2715", font=SANS_B(9), fill=RED)
        d.text((x + 12, y), fit_one_line(title, SANS(9), col_w - 70),
               font=SANS(9), fill=(110, 105, 95))
        tw = text_w(when, SANS_B(9))
        d.text((x + col_w - tw, y), when, font=SANS_B(9), fill=RED)

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
