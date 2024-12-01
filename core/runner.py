from typing import Dict, Type
import time

from solution import day1
from solution.solution_base import Solution


class SolutionRunner:
    def __init__(self):
        self.solutions: Dict[int, Type[Solution]] = {
            1: day1.Day1Solution,

        }

    def run(self, day: int, part: int = None) -> None:

        if day not in self.solutions:
            print(f"Solution has not been implemented for {day}")
            return

        solution = self.solutions[day]()
        start_time = time.time()

        try:
            if part == 1:
                result = solution.part1(solution.read_input())
                print(f"Day {day} Part 1: {result}")
            elif part == 2:
                result = solution.part2(solution.read_input())
                print(f"Day {day} Part 2: {result}")
            else:
                print(f"Day {day} Part 1: {solution.part1(solution.read_input())}")
                print(f"Day {day} Part 2: {solution.part2(solution.read_input())}")
        except NotImplementedError:
            print(f"Solution for day {day} not implemented yet!")
        except Exception as e:
            print(f"Error running day {day}: {str(e)}")

        elapsed = time.time() - start_time
        print(f"Time: {elapsed:.3f} seconds")