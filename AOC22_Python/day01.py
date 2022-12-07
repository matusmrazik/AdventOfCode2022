import os


class Day01:
    INPUT_FILE = os.path.join(os.path.dirname(__file__), '../Inputs', 'day01.txt')
    TEST_FILE = os.path.join(os.path.dirname(__file__), '../Inputs', 'test01.txt')

    def __init__(self, test=False):
        input_path = self.TEST_FILE if test else self.INPUT_FILE
        self.inputs: list[list[int]] = []
        with open(input_path, 'r') as infile:
            calories: list[int] = []
            for line in infile:
                stripped = line.strip()
                if len(stripped) == 0:
                    if calories:
                        self.inputs.append(calories)
                        calories = []
                    continue
                calories.append(int(stripped))
            if calories:
                self.inputs.append(calories)

    def solve1(self):
        return max([sum(_) for _ in self.inputs])

    def solve2(self):
        return sum(sorted([sum(_) for _ in self.inputs], reverse=True)[:3])


if __name__ == '__main__':
    x = Day01()
    print(x.solve1())
    print(x.solve2())
