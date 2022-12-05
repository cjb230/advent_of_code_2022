SOURCE_FILE = 'day_5_input.txt'


def main() -> None:
    mode = "STACK"
    queues = {i: [] for i in range(1, 10)}
    instructions = []
    with open(SOURCE_FILE) as f:
        for i, source_line in enumerate(f.read().splitlines(), start=1):
            if i == 9:
                mode = "MOVES"
            if mode == "STACK":
                for j in range(0, 9):
                    this_string = source_line[j*4:(j*4)+3]
                    this_string = this_string[1]
                    if this_string != " ":
                        queues[j+1].insert(0, this_string)
            else:
                if i >= 11:
                    elements = source_line.split(" ")
                    instructions.append([int(elements[1]),int(elements[3]),int(elements[5])])

    for instruction in instructions:
        index = -1 * instruction[0]
        moved_list = queues[instruction[1]][index:]
        queues[instruction[1]] = queues[instruction[1]][:index]
        queues[instruction[2]].extend(moved_list)

    result = ""
    for i in range(1, 10):
        result += queues[i][-1]
    print(result)


if __name__ == "__main__":
    main()
