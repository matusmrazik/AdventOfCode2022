import os
import re
import typing


class Directory:
    name: str
    size_files: int
    size_total: int | None
    subdirs: dict[str, typing.Self]
    parent: typing.Self

    def __init__(self, name: str):
        self.name = name
        self.size_files = 0
        self.size_total = None
        self.subdirs = {}
        self.parent = None

    def add_file(self, size: int):
        self.size_files += size
        self.size_total = None

    def add_subdir(self, name: str):
        subdir = Directory(name)
        self.subdirs[name] = subdir
        subdir.parent = self
        self.size_total = None

    def find_subdir(self, name: str):
        return self.subdirs[name]

    def compute_size(self):
        if self.size_total is not None:
            return self.size_total
        result = self.size_files
        for subdir in self.subdirs.values():
            result += subdir.compute_size()
        self.size_total = result
        return result

    def find_dirs_smaller_than(self, size: int):
        result = 0 if self.compute_size() > size else self.compute_size()
        for subdir in self.subdirs.values():
            result += subdir.find_dirs_smaller_than(size)
        return result

    def list_all_subdirs(self):
        result: list[typing.Self] = [self]
        for subdir in self.subdirs.values():
            result += subdir.list_all_subdirs()
        return result


class Day07:
    INPUT_FILE = os.path.join(os.path.dirname(__file__), '../Inputs', 'day07.txt')
    TEST_FILE = os.path.join(os.path.dirname(__file__), '../Inputs', 'test07.txt')

    def __init__(self, test=False):
        input_path = self.TEST_FILE if test else self.INPUT_FILE
        self.inputs: list[str] = []
        with open(input_path) as infile:
            for line in infile:
                self.inputs.append(line.strip())

    def create_dir_tree(self):
        command_pattern = re.compile(r'^\$ (?P<cmd>cd|ls) ?(?P<dir>.+)?$')
        content_pattern = re.compile(r'^(?P<what>dir|\d+) (?P<name>.+)$')

        root_dir = Directory('/')
        cur_dir = root_dir

        for line in self.inputs:
            m = command_pattern.match(line)
            if m is not None:
                cmd, dirname = m.groups()
                if cmd == 'ls':
                    continue
                if dirname == '/':
                    cur_dir = root_dir
                    continue
                elif dirname == '..':
                    cur_dir = cur_dir.parent
                    continue
                cur_dir = cur_dir.find_subdir(dirname)
                continue
            m = content_pattern.match(line)
            if m is not None:
                what, name = m.groups()
                if what == 'dir':
                    cur_dir.add_subdir(name)
                    continue
                cur_dir.add_file(int(what))

        return root_dir

    def solve1(self):
        root_dir = self.create_dir_tree()
        return root_dir.find_dirs_smaller_than(100000)

    def solve2(self):
        TOTAL_SPACE = 70000000
        UPDATE_SPACE = 30000000

        root_dir = self.create_dir_tree()
        all_dirs = root_dir.list_all_subdirs()
        all_dirs.sort(key=lambda d: d.compute_size())

        space_needed = UPDATE_SPACE - (TOTAL_SPACE - root_dir.compute_size())
        for i in range(len(all_dirs)):
            if all_dirs[i].compute_size() >= space_needed:
                return all_dirs[i].compute_size()
        return None


if __name__ == '__main__':
    x = Day07()
    print(x.solve1())
    print(x.solve2())
