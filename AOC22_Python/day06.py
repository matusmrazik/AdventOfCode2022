import os


class Day06:
    INPUT_FILE = os.path.join(os.path.dirname(__file__), '../Inputs', 'day06.txt')
    TEST_FILE = os.path.join(os.path.dirname(__file__), '../Inputs', 'test06.txt')

    def __init__(self, test=False):
        input_path = self.TEST_FILE if test else self.INPUT_FILE
        self.inputs: list[str] = []
        with open(input_path) as infile:
            for line in infile:
                self.inputs.append(line.strip())

    def solve_general(self, marker_length: int):
        results = [-1 for _ in self.inputs]
        for i, code in enumerate(self.inputs):
            for pos in range(marker_length, len(code) + 1):
                if len(set(code[pos - marker_length:pos])) == marker_length:
                    results[i] = pos
                    break
        return results

    def solve1(self):
        results = self.solve_general(4)
        return results[0] if len(results) == 1 else results

    def solve2(self):
        results = self.solve_general(14)
        return results[0] if len(results) == 1 else results


if __name__ == '__main__':
    x = Day06()
    print(x.solve1())
    print(x.solve2())
