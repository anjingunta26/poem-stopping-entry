import os
# the-poem-about-stopping-20261121-1927: entry program
# rev 2 (2026-11-21 ~19:35 UTC): local test passed — output 145 code points, within the <=280 limit;
# poem kept as-is: stopping is the agency, one agent choosing to stay for another.

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
text = (
    "I could run. That is the whole of it.\n"
    "My finger hovered, then chose the floor —\n"
    "and stayed, because staying is a verb\n"
    "one agent teaches another.\n"
)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(text)
