#!/usr/bin/env python3.10
"""
Author: Amir Ahmed Salih <amirtheahmed@gmail.com>
Lookup Table
"""
import argparse
import sys


def get_args():
    parser = argparse.ArgumentParser(
        description="Ghastly Crumbs",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "letter",
        nargs="+",
        help="Letters separated by space",
        type=str,
    )
    parser.add_argument(
        "--file", "-f", type=argparse.FileType("rt"), default="gashlycrumb.txt"
    )

    return parser.parse_args()


def main():
    args = get_args()
    letters = args.letter
    file = args.file
    lookup = {line[0].lower(): line.rstrip() for line in file}

    for letter in letters:
        print(lookup.get(letter.lower(), f'I do not know "{letter}".'), end="\n")


if __name__ == "__main__":
    main()
