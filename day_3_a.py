SOURCE_FILE = 'day_3_input.txt'


def priority(character: str) -> int:
    offset: int = 0
    if character.isupper():
        offset = 38
    else:
        offset = 96
    return ord(character) - offset


def main() -> None:
    pack_compartments = {}
    priority_sum = 0
    with open(SOURCE_FILE) as f:
        for i, source_line in enumerate(f.readlines(), start=1):
            line = source_line.strip()
            half_length = int(len(line) / 2)
            pack_compartments[i] = [set(line.strip()[:half_length]), set(line.strip()[half_length:])]
            pack_compartments[i].append(pack_compartments[i][0].intersection(pack_compartments[i][1]))
            priority_sum += priority(pack_compartments[i][2].pop())
    print(priority_sum)


if __name__ == "__main__":
    main()
