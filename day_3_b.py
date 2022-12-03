SOURCE_FILE = 'day_3_input.txt'


def priority(character: str) -> int:
    offset: int = 96
    if character.isupper():
        offset = 38
    return ord(character) - offset


def main() -> None:
    pack_compartments = {}
    priority_sum = 0
    with open(SOURCE_FILE) as f:
        for i, source_line in enumerate(f.readlines(), start=1):
            pack_compartments[i] = set(source_line.strip())

    for j in range(1, int((i / 3)) + 1):
        index = j * 3
        badge = pack_compartments[index].intersection(pack_compartments[index - 1]).intersection(pack_compartments[index - 2]).pop()
        priority_sum += priority(badge)

    print(priority_sum)


if __name__ == "__main__":
    main()
