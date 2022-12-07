import os
import typing


class Range:
    def __init__(self, text: str):
        self.start, self.end = (int(_) for _ in text.split('-'))

    def contains(self, other: typing.Self):
        return self.start <= other.start and self.end >= other.end

    def overlaps(self, other: typing.Self):
        return self.start <= other.end and self.end >= other.start


class Day04:
    INPUT_FILE = os.path.join(os.path.dirname(__file__), '../Inputs', 'day04.txt')
    TEST_FILE = os.path.join(os.path.dirname(__file__), '../Inputs', 'test04.txt')

    def __init__(self, test=False):
        input_path = self.TEST_FILE if test else self.INPUT_FILE
        self.inputs: list[tuple[Range, ...]] = []
        with open(input_path) as infile:
            for line in infile:
                self.inputs.append(tuple(Range(_) for _ in line.strip().split(',')))

    def solve1(self):
        return sum(a.contains(b) or b.contains(a) for a, b in self.inputs)

    def solve2(self):
        return sum(a.overlaps(b) for a, b in self.inputs)


if __name__ == '__main__':
    x = Day04()
    print(x.solve1())
    print(x.solve2())
