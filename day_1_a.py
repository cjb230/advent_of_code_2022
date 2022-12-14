SOURCE_FILE = 'day_1_input.txt'


def main():
    with open(SOURCE_FILE) as f:
        lines = f.readlines()

    individual_sums = []
    individual_total = 0
    for s in lines:
        if s == '\n':
            individual_sums.append(individual_total)
            individual_total = 0
        else:
            individual_total += int(s)
    
    print(max(individual_sums))


if __name__ == "__main__":
    main()
