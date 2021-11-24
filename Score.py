from pathlib import Path


def add_score(difficulty):
    POINTS_OF_WINNING = str((difficulty * 3) + 5)
    try:
        score_file = open(Path("Scores.txt"), "r")
        score = open(Path("Scores.txt"), "a")
        score.write(f" ,{POINTS_OF_WINNING}")
    except FileNotFoundError:
        score = open(Path("Scores.txt"), "x")
        score.write(POINTS_OF_WINNING)


