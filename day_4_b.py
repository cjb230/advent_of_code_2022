SOURCE_FILE = 'day_4_input.txt'



def partially_contains(container: list[int], containee: list[int]) -> bool:
    return containee[0] >= container[0] and containee[0] <= container[1] or containee[1] >= container[0] and containee[1] <= container[1]


def main() -> None:
    reconsider_candidates = 0
    with open(SOURCE_FILE) as f:
        for i, source_line in enumerate(f.readlines(), start=1):
            line = source_line.strip()
            a, b = line.split(",")
            a_low_char, a_high_char = a.split("-")
            b_low_char, b_high_char = b.split("-")
            boundaries_a = [int(a_low_char), int(a_high_char)]
            boundaries_b = [int(b_low_char), int(b_high_char)]
            if partially_contains(boundaries_a, boundaries_b) or partially_contains(boundaries_b, boundaries_a):
                reconsider_candidates += 1
                
    print(reconsider_candidates)


if __name__ == "__main__":
    main()
