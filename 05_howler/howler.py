#!/usr/bin/env python3.10
"""
Author: Amir Ahmed <amirtheahmed@gmail.com>
"""
import argparse
import os.path
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Howler")
    parser.add_argument("message", metavar="str", help="Message for howler")
    parser.add_argument(
        "--outfile", "-o", metavar="str", help="Output file path", type=str, default=""
    )

    args = parser.parse_args()
    if os.path.isfile(args.message):
        args.message = open(args.message).read().rstrip()

    return args


def main():
    args = parse_args()
    outputFile = open(args.outfile, "wt") if args.outfile else sys.stdout

    outputFile.write(args.message.strip().upper())


if __name__ == "__main__":
    main()
