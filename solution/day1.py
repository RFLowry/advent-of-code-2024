from typing import Any

from solution.solution_base import Solution


class Day1Solution(Solution):

    def __init__(self, day=1):
        super().__init__(day)
        self._left_numbers = []
        self._right_numbers = []

    def read_input(self) -> str:
        if not self.input_path.exists():
            raise FileNotFoundError(f"No input file found for day {self.day}")

        if not self._left_numbers or not self._right_numbers:
            with open(self.input_path, 'r') as file:
                for line in file:
                    # split() breaks the line into parts at whitespace
                    left, right = map(int, line.split())
                    self._left_numbers.append(left)
                    self._right_numbers.append(right)

            self._left_numbers.sort()
            self._right_numbers.sort()

        return self.input_path

    def part1(self, data: str) -> Any:

        total = 0

        for left, right in zip(self._left_numbers, self._right_numbers):
            difference = abs(left - right)
            total += difference

        return total

    def part2(self, data: str) -> Any:

        frequency = {}
        for right_nums in self._right_numbers :
            if right_nums in frequency:
                frequency[right_nums] =+ (frequency[right_nums]+1)
            else:
                frequency[right_nums] = 1

        similarity_score = 0
        for left_nums in self._left_numbers :
            similarity_score += (left_nums * frequency.get(left_nums, 0))

        return similarity_score