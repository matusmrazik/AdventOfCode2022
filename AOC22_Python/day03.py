import os


def priority(char: str):
    return ord(char) - ord('a') + 1 if char.islower() else ord(char) - ord('A') + 27


class Day03:
    INPUT_FILE = os.path.join(os.path.dirname(__file__), '../Inputs', 'day03.txt')
    TEST_FILE = os.path.join(os.path.dirname(__file__), '../Inputs', 'test03.txt')

    def __init__(self, test=False):
        input_path = self.TEST_FILE if test else self.INPUT_FILE
        self.inputs: list[str] = []
        with open(input_path) as infile:
            for line in infile:
                self.inputs.append(line.strip())

    def solve1(self):
        result = 0
        for rucksack in self.inputs:
            half = len(rucksack) // 2
            common = set(rucksack[:half]).intersection(set(rucksack[half:]))
            item = list(common)[0]
            result += priority(item)
        return result

    def solve2(self):
        result = 0
        for i in range(0, len(self.inputs), 3):
            common = set(self.inputs[i]).intersection(set(self.inputs[i + 1])).intersection(set(self.inputs[i + 2]))
            item = list(common)[0]
            result += priority(item)
        return result


if __name__ == '__main__':
    x = Day03()
    print(x.solve1())
    print(x.solve2())
