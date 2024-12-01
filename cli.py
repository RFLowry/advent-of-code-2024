import argparse

from core.runner import SolutionRunner


def main():
    parser = argparse.ArgumentParser(description='Run Advent of Code 2024 Solutions')
    parser.add_argument('day', type=int, help='Which day to run? Day 1 through 25', choices=[i for i in range(1, 26)])
    parser.add_argument('-p', '--part', type=int, choices=[1, 2],
                        help='Which part to run (optional)')

    args = parser.parse_args()
    print(args)
    runner = SolutionRunner()
    runner.run(args.day, args.part)


if __name__ == '__main__':
    main()