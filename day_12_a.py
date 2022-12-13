import math


SOURCE_FILE = 'day_12_input.txt'


class Node(object):
    tentative_distance: int
    x: int
    y: int
    height: int

    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = ord(height) - 96
        self.tentative_distance = math.inf


def main() -> None:
    all_nodes = []

    with open(SOURCE_FILE) as f:
        lines = f.readlines()
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            all_nodes.append(Node(x=x, y=y, height=char))
            print(all_nodes[0].height)
            break
        break


if __name__ == "__main__":
    main()
