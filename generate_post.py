#!/usr/bin/env python3
"""
Simple template for drafting The Arkansas Echo Buffer posts.

Usage:
    python generate_post.py

Edit the TOPIC, KEY_FACTS, and SOURCES sections below,
then run to get a clean post ready to paste into Buffer.
"""

TOPIC = "Elizabeth Eckford walked to Central High alone"

KEY_FACTS = [
    "September 4, 1957",
    "Fifteen-year-old Elizabeth Eckford arrived alone",
    "The meeting place changed the night before",
    "The Eckford family had no phone",
    "She was turned away twice by the National Guard",
    "A hostile crowd surrounded her",
    "She sat on a bus bench until a city bus took her to her mother's job",
]

SOURCES = [
    "https://www.nps.gov/people/the-little-rock-nine.htm",
    "https://encyclopediaofarkansas.net/entries/elizabeth-ann-eckford-721/",
]

HASHTAGS = "#ElizabethEckford #LittleRockNine #CivilRights #ArkansasBlackHistory #BlackHistory #ArkansasHistory #BlackHeritage #TheArkansasEcho"

def build_post():
    lines = [TOPIC, ""]
    lines.append("\n".join(f"• {fact}" for fact in KEY_FACTS))
    lines.append("")
    lines.append(HASHTAGS)
    lines.append("")
    lines.append("Sources:")
    lines.extend(SOURCES)
    return "\n".join(lines)

if __name__ == "__main__":
    print(build_post())
