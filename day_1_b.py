SOURCE_FILE = 'day_1_input.txt'


class BoundedSet:
    def __init__(self, max_size):
        self.max_size = max_size
        self.elements = []

    def add(self, element):
        if len(self.elements) < self.max_size:
            # If the set is not full, just append the element.
            self.elements.append(element)
        else:
            # If the set is full, find the smallest element.
            min_element = min(self.elements)

            # If the element we want to add is larger than the smallest
            # element in the set, remove the smallest element and add
            # the new element instead.
            if element > min_element:
                self.elements.remove(min_element)
                self.elements.append(element)


def main():
    with open(SOURCE_FILE) as f:
        lines = f.readlines()

    individual_total = 0
    top_three = BoundedSet(3)
    for s in lines:
        if s == '\n':
            top_three.add(individual_total)
            individual_total = 0
        else:
            individual_total += int(s)

    print(sum(top_three.elements))


if __name__ == "__main__":
    main()
