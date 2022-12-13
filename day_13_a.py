SOURCE_FILE = 'day_13_input.txt'
import sys


def is_list(string_in: str) -> bool:
    if string_in[0] == "[" and string_in[-1] == "]":
        open_count = 1
        for char in string_in[1:-1]:
            if char == "[":
                open_count += 1
            elif char == "]":
                open_count -= 1
                if open_count == 0:
                    return False
        if open_count == 1:
            return True
        else:
            print("open_count = %d" % open_count)
            sys.exit(1)
    else:
        return False


def separate(string_in: str) -> tuple[str, str]:
    print("Separating string:", string_in)
    if string_in[0] == "[":


    else:





def compare(left: str, right: str) -> bool:
    print("Now comparing:")
    print(left)
    print(right)
    print()
    """True if ordered."""
    if is_list(left) and is_list(right):
        print("Stripping both lists")
        return compare(left=left[1:-1], right=right[1:-1])
    elif is_list(left):
        print("Turning right to a list")
        return compare(left=left, right=("[" + right + "]"))
    elif is_list(right):
        print("Turning left to a list")
        return compare(left=("[" + left + "]"), right=right)

    if len(left) == 0 and len(right) > 0:
        print("Left exhausted => ORDERED")
        return True
    elif len(left) > 0 and len(right) == 0:
        print("Right exhausted => NOT ORDERED")
        return False
    
    if len(left) > 0:  # and right must be too
        left_first, left_remainder = separate(left)
        right_first, right_remainder = separate(right)


    print("WHY ARE WE HERE?")
    sys.exit(1)


def main() -> None:
    with open(SOURCE_FILE) as f:
        lines = f.readlines()
    
    left = ""
    right = ""
    pairs = {}
    for line_no, line_content in enumerate(lines, start=1):
        if line_no%3 == 1:
            left = line_content[:-1]
        elif line_no%3 == 2:
            right = line_content[:-1]
            pairnum = int(line_no/3) + 1
            pairs[pairnum] = {"left": left, "right": right}
    
    index_sum = 0
    for pair_num, pair in pairs.items():
        print()
        print("PAIR_NUM = ", pair_num)
        print("pair = ", pair)
        if compare(left=pair["left"], right=pair["right"]):
            index_sum += pair_num
        sys.exit()

    print(index_sum)

if __name__ == "__main__":
    main()
