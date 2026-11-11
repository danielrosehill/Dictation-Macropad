"""Render the 4x4 voice-control layout mockup to layout-4x4.svg (same folder).

Run: python3 layouts/voice-control-16/render_mockup.py   (stdlib only)
Edit KEYS to change the layout; README.md in this folder is the authoritative table.
"""
from pathlib import Path

# (label, sublabel, group, has_led)
KEYS = [
    ("GAIN −1", "−1 %", "gain", False), ("GAIN +1", "+1 %", "gain", False),
    ("GAIN −10", "−10 %", "gain", False), ("GAIN +10", "+10 %", "gain", False),
    ("MUTE", "toggle", "input", True), ("INPUT", "next source", "input", False),
    ("AGC", "toggle", "chain", True), ("ASR CHAIN", "bypass", "chain", True),
    ("NOISE", "removal", "chain", True), ("VAD", "toggle", "chain", True),
    ("POST-PROC", "toggle", "chain", True), ("MODEL", "cycle", "dict", False),
    ("REC", "start/stop", "dict", True), ("PAUSE", "resume", "dict", True),
    ("RETAKE", "discard+rec", "dict", False), ("ENTER", "send text", "dict", False),
]
COLORS = {"gain": "#3b6ea5", "input": "#a53b3b", "chain": "#5a8a3a", "dict": "#8a5aa5"}
NAMES = {"gain": "Gain", "input": "Input", "chain": "Processing toggles", "dict": "Dictation"}

K, GAP, PAD = 110, 14, 40
W = PAD * 2 + 4 * K + 3 * GAP
H = PAD * 2 + 4 * K + 3 * GAP + 90
out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" font-family="sans-serif">',
       f'<rect width="{W}" height="{H}" rx="24" fill="#1e1f22"/>']
for i, (label, sub, grp, led) in enumerate(KEYS):
    x = PAD + (i % 4) * (K + GAP)
    y = PAD + (i // 4) * (K + GAP)
    c = COLORS[grp]
    out.append(f'<rect x="{x}" y="{y}" width="{K}" height="{K}" rx="12" fill="#2c2e33" stroke="{c}" stroke-width="4"/>')
    out.append(f'<text x="{x+K/2}" y="{y+K/2}" fill="#eee" font-size="15" font-weight="bold" text-anchor="middle">{label}</text>')
    out.append(f'<text x="{x+K/2}" y="{y+K/2+20}" fill="#aaa" font-size="12" text-anchor="middle">{sub}</text>')
    if led:
        out.append(f'<circle cx="{x+K-16}" cy="{y+16}" r="7" fill="#ffcc33" stroke="#000" stroke-width="1"/>')
ly = PAD + 4 * K + 3 * GAP + 30
for j, g in enumerate(COLORS):
    lx = PAD + j * 125
    out.append(f'<rect x="{lx}" y="{ly}" width="16" height="16" rx="3" fill="{COLORS[g]}"/>')
    out.append(f'<text x="{lx+22}" y="{ly+13}" fill="#ddd" font-size="12">{NAMES[g]}</text>')
out.append(f'<circle cx="{PAD+8}" cy="{ly+44}" r="7" fill="#ffcc33"/>')
out.append(f'<text x="{PAD+22}" y="{ly+49}" fill="#ddd" font-size="12">State LED (lit = on / active), driven by the host</text>')
out.append("</svg>")
dest = Path(__file__).resolve().parent / "layout-4x4.svg"
dest.write_text("\n".join(out))
print(dest)
