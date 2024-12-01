from abc import ABC, abstractmethod
from pathlib import Path


class Solution(ABC):

    def __init__(self, day: int):
        self.day = day
        self.input_path = Path(f"inputs/day{day}.txt")

    def read_input(self) -> str:
        if not self.input_path.exists():
            raise FileNotFoundError(f"No input file found for day {self.day}")
        return self.input_path.read_text().strip()

    @abstractmethod
    def part1(self, data: str):
        pass

    @abstractmethod
    def part2(self, data: str):
        pass


