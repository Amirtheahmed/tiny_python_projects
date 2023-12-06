#!/usr/bin/env python3.10
"""
Telephone: Text mutator
"""
import argparse
import os.path
import random
import string


def get_args():
    parser = argparse.ArgumentParser(description="String mutator")

    parser.add_argument(
        "text",
        help="Message string or input file",
    )

    parser.add_argument(
        "--mutations",
        "-m",
        help="Mutations percentage",
        type=float,
        metavar="float",
        default=0.1,
    )

    parser.add_argument("--seed", "-s", help="Seed number", type=int, default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    if args.mutations < 0 or args.mutations > 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return args


def main():
    args = get_args()
    seed = args.seed
    mutations = args.mutations
    text = args.text
    alpha = "".join(sorted(string.ascii_letters + string.punctuation))

    random.seed(seed)
    mutation_count = round(len(text) * (mutations))

    indexes = random.sample(range(len(text)), mutation_count)
    new_string = text
    for i in indexes:
        new_char = random.choice(alpha.replace(text[i], ""))
        new_string = new_string[:i] + new_char + new_string[i + 1 :]

    print(f'You said: "{args.text}"')
    print(f'I heard : "{new_string}"')


if __name__ == "__main__":
    main()
