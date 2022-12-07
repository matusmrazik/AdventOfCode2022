import os

SCORES_1 = {
    'A': {'X': 4, 'Y': 8, 'Z': 3},
    'B': {'X': 1, 'Y': 5, 'Z': 9},
    'C': {'X': 7, 'Y': 2, 'Z': 6},
}

SCORES_2 = {
    'A': {'X': 3, 'Y': 4, 'Z': 8},
    'B': {'X': 1, 'Y': 5, 'Z': 9},
    'C': {'X': 2, 'Y': 6, 'Z': 7},
}


class Day02:
    INPUT_FILE = os.path.join(os.path.dirname(__file__), '../Inputs', 'day02.txt')
    TEST_FILE = os.path.join(os.path.dirname(__file__), '../Inputs', 'test02.txt')

    def __init__(self, test=False):
        input_path = self.TEST_FILE if test else self.INPUT_FILE
        self.inputs: list[tuple[str, str]] = []
        with open(input_path) as infile:
            for line in infile:
                self.inputs.append((line[0], line[2]))

    def solve1(self):
        return sum(SCORES_1[a][b] for a, b in self.inputs)

    def solve2(self):
        return sum(SCORES_2[a][b] for a, b in self.inputs)


if __name__ == '__main__':
    x = Day02()
    print(x.solve1())
    print(x.solve2())
