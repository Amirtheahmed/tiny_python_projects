#!/usr/bin/env python3.10
"""
Abusive insults
"""
import argparse
import os.path
import random


def get_args():
    parser = argparse.ArgumentParser(
        description="Abuse", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "--adjectives",
        "-a",
        metavar="adjectives",
        help="Number of adjectives",
        type=int,
        default=2,
    )

    parser.add_argument(
        "--number",
        "-n",
        metavar="insults",
        help="Number of insults",
        type=int,
        default=3,
    )

    parser.add_argument(
        "--seed",
        "-s",
        metavar="insults",
        help="Random seed",
        type=int,
        default=None,
    )

    args = parser.parse_args()
    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    return args


def main():
    args = get_args()
    adjective = args.adjectives
    number_of_insults = args.number
    random.seed(args.seed)

    adjectives = """
        "bankrupt base caterwauling corrupt cullionly detestable dishonest false filthsome filthy foolish 
        "foul gross heedless indistinguishable infected insatiate irksome lascivious lecherous loathsome 
        "lubbery old peevish rascaly rotten ruinous scurilous scurvy slanderous sodden-witted thin-faced 
        "toad-spotted unmannered vile wall-eyed
        """.split()
    nouns = (
        "Judas Satan ape ass barbermonger beggar block boy braggart butt carbuncle coward coxcomb cur dandy "
        "degenerate fiend fishmonger fool gull harpy jack jolthead knave liar lunatic maw milksop minion "
        "ratcatcher recreant rogue scold slave swine traitor varlet villain worm"
    ).split()

    insults = [
        "You {} {}!\n".format(
            ", ".join(random.sample(adjectives, adjective)),
            random.choice(nouns),
        )
        for _ in range(number_of_insults)
    ]
    print("".join(insults))


if __name__ == "__main__":
    main()
