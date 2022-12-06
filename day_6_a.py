SOURCE_FILE = 'day_6_input.txt'


def main() -> None:
    with open(SOURCE_FILE) as f:
        source_line = list(f.readlines()[0])

    for p in range(3, len(source_line)):
        uniques = set(source_line[p])
        uniques.add(source_line[p-1])
        uniques.add(source_line[p-2])
        uniques.add(source_line[p-3])
        if len(uniques) != 4:
            continue
        print(p+1)
        break


if __name__ == "__main__":
    main()
