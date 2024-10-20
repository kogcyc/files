#!/usr/bin/python3

# ANSI escape codes for bright colors
colors = {
    # Bright colors
    "Bright Red": "\033[91m",
    "Bright Green": "\033[92m",
    "Bright Yellow": "\033[93m",
    "Bright Blue": "\033[94m",
    "Bright Magenta": "\033[95m",
    "Bright Cyan": "\033[96m",
    "Bright White": "\033[97m",

    "Reset": "\033[0m"  # Reset color to default
}

text = "Hello, colorful world!"

# Print the text in different bright colors
for color_name, color_code in colors.items():
    if color_name != "Reset":
        print(f"{color_code}{color_name}: {text}{colors['Reset']}")
