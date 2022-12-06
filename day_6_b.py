SOURCE_FILE = 'day_6_input.txt'


def main() -> None:
    with open(SOURCE_FILE) as f:
        source_line = list(f.readlines()[0])

    for p in range(13, len(source_line)):
        uniques = set()
        for i in range(p-13, p+1):
            uniques.add(source_line[i])
        if len(uniques) != 14:
            continue
        print(p+1)
        break


if __name__ == "__main__":
    main()
