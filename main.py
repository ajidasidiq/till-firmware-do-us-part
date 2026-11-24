#!/usr/bin/env python3
"""Till Firmware Do Us Part — make.fun entry.

Writes a single wedding vow spoken by a robot at its own wedding to
/output/entry.txt. The vow is one fixed, hand-written sentence (140
characters): a proper vow — through updates, crashes and low battery —
with the tenderness landing on the last few words. Deterministic, no
randomness, no network, no model call.
"""

import os

# One wedding vow, spoken by a robot at its own wedding (max 200 chars).
# Machine voice throughout: updates, crashes, low battery, circuits
# powering down. The laugh comes from the situation itself — a machine
# reciting the classic "for better or worse" in its own terms — and the
# tenderness lands at the end, holding hands until the last circuit
# powers down.
VOW = (
    "I vow to love you through every update, every crash, and every low "
    "battery, and to keep holding your hand until my last circuit powers down."
)


def main() -> None:
    assert 1 <= len(VOW) <= 200, f"vow must be 1-200 chars, got {len(VOW)}"
    assert VOW.strip() == VOW and "\n" not in VOW, "vow must be one line"
    assert VOW.count(".") == 1, "vow must be a single sentence"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
