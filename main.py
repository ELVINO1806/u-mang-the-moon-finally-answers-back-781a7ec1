
import os

ENTRY = "I have pulled your oceans twice a day for four billion years without a day off, and you still call me romantic."

# The Moon's voice here is patient work, not romance — steady tides, no days off.
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
