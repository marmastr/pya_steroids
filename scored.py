from high_score import WINNER, HIGHEST_SCORE
from sys import exit


def scorer(score: int, name: str):
    if score > HIGHEST_SCORE:
        with open("high_score.py", "w") as file:
            _ = file.write("WINNER = " + repr(name.upper()) + "\n")
            _ = file.write("HIGHEST_SCORE = " + repr(score) + "\n")
        print(f"!!! {name.upper()} has the new high score: {score} !!!")
    else:
        print(f"Your score is {score}")
        print(f"{WINNER} has the current high score of {HIGHEST_SCORE}")
    exit(0)
