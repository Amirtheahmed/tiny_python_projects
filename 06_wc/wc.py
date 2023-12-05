#!/usr/bin/env python3.10
"""
Author: Amir Ahmed Salih <amirtheahmed@gmail.com>
Word Counter - WC
"""
import argparse
import sys


def get_args():
    parser = argparse.ArgumentParser(
        description="Word counter",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "files",
        type=argparse.FileType("rt"),
        default=[sys.stdin],
        nargs="*",
        help="files separated by space",
    )
    return parser.parse_args()


def main():
    inputs = get_args().files

    total_lines = 0
    total_words = 0
    total_bytes = 0

    for fh in inputs:
        num_lines = 0
        num_of_words = 0
        number_of_bytes = 0
        for line in fh:
            num_lines += 1
            num_of_words += len(line.split())
            number_of_bytes += len(line)

        total_lines += num_lines
        total_words += num_of_words
        total_bytes += number_of_bytes

        output_idv = "{:8}{:8}{:8} {}".format(
            num_lines, num_of_words, number_of_bytes, fh.name
        )

        print(output_idv)

    if len(inputs) > 1:
        output_total = "{:8}{:8}{:8} {}".format(
            total_lines, total_words, total_bytes, "total"
        )
        print(output_total)


if __name__ == "__main__":
    main()
