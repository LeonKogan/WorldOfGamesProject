from pathlib import Path

SCORES_FILE_NAME = open(Path("Scores.txt"), "x")

BAD_RETURN_CODE = int(401)



def _screen_cleaner():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
