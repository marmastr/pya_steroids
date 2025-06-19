from argparse import Namespace
from high_score import WINNER, HIGHEST_SCORE
from sys import exit


def scorer(score: int, args: Namespace):
    if score > HIGHEST_SCORE:
        if not args.no_save or args.cheater:
            with open("high_score.py", "w") as file:
                _ = file.write("WINNER = " + repr(args.name.upper()) + "\n")
                _ = file.write("HIGHEST_SCORE = " + repr(score) + "\n")
        print(f"!!! {args.name.upper()} has the new high score: {score} !!!")
    else:
        print(f"Your score is {score}")
        print(f"{WINNER} has the current high score of {HIGHEST_SCORE}")
    exit(0)
