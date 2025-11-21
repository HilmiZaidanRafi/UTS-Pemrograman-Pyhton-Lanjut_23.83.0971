import time
import sys
import random

# ============================
#   ANSI COLOR CYCLING
# ============================
COLORS = [
    "\033[91m",  # Red
    "\033[93m",  # Yellow
    "\033[92m",  # Green
    "\033[96m",  # Cyan
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
]

RESET = "\033[0m"


# ============================
#   ASCII BLOCK FONT DATABASE
# ============================
FONT = {
    "A": ["  ██   ", " ██ ██ ", "███████", "██   ██", "██   ██"],
    "B": ["█████  ", "██  ██ ", "█████  ", "██  ██ ", "█████  "],
    "C": [" █████ ", "██     ", "██     ", "██     ", " █████ "],
    "D": ["█████  ", "██  ██ ", "██  ██ ", "██  ██ ", "█████  "],
    "E": ["██████", "██    ", "████  ", "██    ", "██████"],
    "F": ["██████", "██    ", "████  ", "██    ", "██    "],
    "G": [" █████ ", "██     ", "██  ███", "██   ██", " █████ "],
    "H": ["██   ██", "██   ██", "███████", "██   ██", "██   ██"],
    "I": ["█████", "  ██ ", "  ██ ", "  ██ ", "█████"],
    "J": ["██████", "   ██ ", "   ██ ", "██ ██ ", " ███  "],
    "K": ["██  ██", "██ ██ ", "████  ", "██ ██ ", "██  ██"],
    "L": ["██    ", "██    ", "██    ", "██    ", "██████"],
    "M": ["███ ███", "██ █ ██", "██   ██", "██   ██", "██   ██"],
    "N": ["███  ██", "███  ██", "██ ██ █", "██  ███", "██  ███"],
    "O": [" █████ ", "██   ██", "██   ██", "██   ██", " █████ "],
    "P": ["█████ ", "██  ██", "█████ ", "██    ", "██    "],
    "Q": [" █████ ", "██   ██", "██   ██", "██ ████", " ███ ██"],
    "R": ["█████ ", "██  ██", "█████ ", "██ ██ ", "██  ██"],
    "S": [" █████ ", "██     ", " █████ ", "     ██", "█████  "],
    "T": ["███████", "   ██  ", "   ██  ", "   ██  ", "   ██  "],
    "U": ["██   ██", "██   ██", "██   ██", "██   ██", " █████ "],
    "V": ["██   ██", "██   ██", "██   ██", " ████  ", "  ██   "],
    "W": ["██   ██", "██   ██", "██ █ ██", "██ █ ██", " ████  "],
    "X": ["██   ██", " ██ ██ ", "  ███  ", " ██ ██ ", "██   ██"],
    "Y": ["██   ██", " ██ ██ ", "  ███  ", "  ██   ", "  ██   "],
    "Z": ["██████", "    ██", "  ███ ", " ██   ", "██████"],
    " ": ["   ", "   ", "   ", "   ", "   "]
}


# ============================
#   BUILD ASCII TEXT
# ============================
def build_ascii(text):
    text = text.upper()
    lines = ["", "", "", "", ""]
    
    for char in text:
        pattern = FONT.get(char, FONT[" "])
        for i in range(5):
            lines[i] += pattern[i] + "  "

    return lines


# ============================
#  EARTHQUAKE SHAKER EFFECT
# ============================
def apply_earthquake(lines):
    # shake horizontal ±1–3
    shake_x = random.randint(-2, 2)
    # shake vertical shift (line wobble)
    shake_y = random.randint(0, 1)

    shaken = []

    for i, line in enumerate(lines):
        if i + shake_y < len(lines):
            final_line = lines[i + shake_y]
        else:
            final_line = lines[i]

        if shake_x >= 0:
            shaken.append(" " * shake_x + final_line)
        else:
            shaken.append(final_line[abs(shake_x):] if abs(shake_x) < len(final_line) else final_line)

    return shaken


# ============================
#   ANIMATE WITH COLOR + SHAKE
# ============================
def animate_bounce(ascii_lines):
    indent = 0
    increasing = True
    color_idx = 0

    while True:
        color = COLORS[color_idx]

        # Apply earthquake shake
        shaken_lines = apply_earthquake(ascii_lines)

        for line in shaken_lines:
            print(color + (" " * indent) + line + RESET)
        print()

        time.sleep(0.06)

        # bounce left-right
        if increasing:
            indent += 1
            if indent == 20:
                increasing = False
        else:
            indent -= 1
            if indent == 0:
                increasing = True

        # next color
        color_idx = (color_idx + 1) % len(COLORS)


# ============================
#             MAIN
# ============================
def main():
    print("=== ASCII BIG TEXT + COLOR + EARTHQUAKE SHAKE ===")
    text = input("Masukkan teks: ")

    print("\nMembuat ASCII...\n")
    ascii_art = build_ascii(text)

    for line in ascii_art:
        print(line)

    print("\nMemulai animasi Earthquake Shaker...\nCTRL + C untuk berhenti.\n")

    try:
        animate_bounce(ascii_art)
    except KeyboardInterrupt:
        sys.exit()


main()
