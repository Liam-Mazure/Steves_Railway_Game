HIGH_SCORE_File = "highscore.txt"

def load_high_score():
    try:
        with open(HIGH_SCORE_File, 'r') as file:
            return int(file.read())
    except(FileNotFoundError, ValueError):
        return 0

def save_high_scores(score):
    with open(HIGH_SCORE_File, 'w') as file:
        file.write(str(score))