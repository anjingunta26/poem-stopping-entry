import os
# the-poem-about-stopping-20261121-1927: entry program (revised after local test)

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
