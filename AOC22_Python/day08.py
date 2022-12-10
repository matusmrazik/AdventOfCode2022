import os

import numpy as np


class Day08:
    INPUT_FILE = os.path.join(os.path.dirname(__file__), '../Inputs', 'day08.txt')
    TEST_FILE = os.path.join(os.path.dirname(__file__), '../Inputs', 'test08.txt')

    def __init__(self, test=False):
        input_path = self.TEST_FILE if test else self.INPUT_FILE
        self.inputs = np.genfromtxt(input_path, dtype=np.uint8, delimiter=1)

    def solve1(self):
        rows, cols = self.inputs.shape
        visible = np.zeros(self.inputs.shape, dtype=np.bool8)

        # vertical
        visible[[0, -1], :] = True
        tallest = self.inputs[[0, -1], :].copy()
        for row in range(1, rows):
            visible[row, :] += self.inputs[row, :] > tallest[0]
            visible[-1 - row, :] += self.inputs[-1 - row, :] > tallest[1]
            tallest = np.maximum(tallest, self.inputs[[row, -1 - row], :])

        # horizontal
        visible[:, [0, -1]] = True
        tallest = self.inputs[:, [0, -1]].copy()
        for col in range(1, cols):
            visible[:, col] += self.inputs[:, col] > tallest[:, 0]
            visible[:, -1 - col] += self.inputs[:, -1 - col] > tallest[:, 1]
            tallest = np.maximum(tallest, self.inputs[:, [col, -1 - col]])

        return np.count_nonzero(visible)

    def solve2(self):
        rows, cols = self.inputs.shape
        distance = np.zeros((rows, cols, 4), dtype=np.uint8)

        for row in range(rows):
            # up
            tallest = np.zeros(cols, dtype=self.inputs.dtype)
            for r in range(row + 1, rows):
                distance[r, self.inputs[r, :] > tallest, 0] += 1
                tallest = np.maximum(tallest, self.inputs[r, :])
            # down
            tallest = np.zeros(cols, dtype=self.inputs.dtype)
            for r in range(row - 1, -1, -1):
                distance[r, self.inputs[r, :] > tallest, 1] += 1
                tallest = np.maximum(tallest, self.inputs[r, :])

        for col in range(cols):
            # left
            tallest = np.zeros(rows, dtype=self.inputs.dtype)
            for c in range(col + 1, cols):
                distance[self.inputs[:, c] > tallest, c, 2] += 1
                tallest = np.maximum(tallest, self.inputs[:, c])
            # right
            tallest = np.zeros(rows, dtype=self.inputs.dtype)
            for c in range(col - 1, -1, -1):
                distance[self.inputs[:, c] > tallest, c, 3] += 1
                tallest = np.maximum(tallest, self.inputs[:, c])

        scenic_score = np.prod(distance, axis=2)
        return np.max(scenic_score)


if __name__ == '__main__':
    x = Day08()
    print(x.solve1())
    print(x.solve2())
