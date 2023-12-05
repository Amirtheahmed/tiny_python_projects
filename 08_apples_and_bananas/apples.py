#!/usr/bin/env python3.10
"""
Apples
"""
import argparse
import os.path


def get_args():
    parser = argparse.ArgumentParser(
        description="Apples", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "input",
        help="Any text",
    )

    parser.add_argument(
        "--vowel",
        "-v",
        default="a",
        help="Enter substitution vowel",
        type=str,
        choices=list("aeiou"),
    )

    return parser.parse_args()


def main():
    vowels = ["a", "e", "i", "o", "u", "y"]
    text = get_args().input
    input_text = text

    if os.path.isfile(text):
        fh = open(text, "rt")
        input_text = fh.read().rstrip()

    vowel = get_args().vowel
    new_text = []

    for char in input_text:
        if char in "aeiou":
            new_text.append(vowel.lower())
        elif char in "AEIOU":
            new_text.append(vowel.upper())
        else:
            new_text.append(char)

    print("".join(new_text))


if __name__ == "__main__":
    main()
