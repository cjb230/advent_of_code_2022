SOURCE_FILE = 'day_2_input.txt'

# rock       A  1   beats scissors
# paper      B  2   beats rock
# scissors   C  3   beats paper

RESULT_SCORES = {"X": 0, "Y": 3, "Z": 6}
CHOICE_SCORES = {"X": {"A": 3, "B": 1, "C": 2},  # we lose
                 "Y": {"A": 1, "B": 2, "C": 3},  # we draw
                 "Z": {"A": 2, "B": 3, "C": 1}}  # we win


def main():
    with open(SOURCE_FILE) as f:
        lines = f.readlines()
    
    score = 0
    for line in lines:
        plays = line.strip().split(' ')
        score += RESULT_SCORES[plays[1]]
        score += CHOICE_SCORES[plays[1]][plays[0]]

    print(score)


if __name__ == "__main__":
    main()
