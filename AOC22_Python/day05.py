import os
import re
from collections import deque


class Move:
    count: int
    src: int
    dst: int

    def __init__(self, text: str):
        m = re.match(r'^move (?P<count>\d+) from (?P<src>\d+) to (?P<dest>\d+)$', text)
        self.count = int(m.group('count'))
        self.src = int(m.group('src'))
        self.dst = int(m.group('dest'))


class Day05:
    INPUT_FILE = os.path.join(os.path.dirname(__file__), '../Inputs', 'day05.txt')
    TEST_FILE = os.path.join(os.path.dirname(__file__), '../Inputs', 'test05.txt')

    def __init__(self, test=False):
        input_path = self.TEST_FILE if test else self.INPUT_FILE
        self.inputs: list[deque[str]] = []
        self.moves: list[Move] = []

        def process_line(text: str):
            for i in range(len(self.inputs)):
                crate = text[i * 4 + 1]
                if crate.isspace():
                    continue
                self.inputs[i].appendleft(crate)

        with open(input_path) as infile:
            line = infile.readline()
            n_stacks = (len(line) + 1) // 4
            self.inputs = [deque() for _ in range(n_stacks)]
            process_line(line)
            while True:
                line = infile.readline()
                if line.startswith(' 1 '):
                    break
                process_line(line)
            infile.readline()  # empty line
            for line in infile:
                self.moves.append(Move(line))

    def solve1(self):
        stacks = [deque(_) for _ in self.inputs]
        for move in self.moves:
            for _ in range(move.count):
                x = stacks[move.src - 1].pop()
                stacks[move.dst - 1].append(x)
        return ''.join(_[-1] for _ in stacks)

    def solve2(self):
        stacks = [deque(_) for _ in self.inputs]
        buf = deque[str]()
        for move in self.moves:
            for _ in range(move.count):
                x = stacks[move.src - 1].pop()
                buf.append(x)
            for _ in range(move.count):
                x = buf.pop()
                stacks[move.dst - 1].append(x)
        return ''.join(_[-1] for _ in stacks)


if __name__ == '__main__':
    x = Day05()
    print(x.solve1())
    print(x.solve2())
