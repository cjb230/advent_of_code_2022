SOURCE_FILE = 'day_2_input.txt'

CHOICE_SCORES = {"X": 1, "Y": 2, "Z": 3}
RESULT_SCORES = {"X": {"A": 3, "B": 0, "C": 6},
                 "Y": {"A": 6, "B": 3, "C": 0 },
                 "Z": {"A": 0, "B": 6, "C": 3}}


def main():
    with open(SOURCE_FILE) as f:
        lines = f.readlines()
    
    score = 0
    for line in lines:
        plays = line.strip().split(' ')
        score += CHOICE_SCORES[plays[1]]
        score += RESULT_SCORES[plays[1]][plays[0]]

    print(score)


if __name__ == "__main__":
    main()
