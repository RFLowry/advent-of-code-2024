from pathlib import Path
from typing import List


class InputReader:

    @staticmethod
    def read_input(day: int) -> List[str]:
        path = Path(f"inputs/day{day}.txt")
        return path.read_text().splitlines()

