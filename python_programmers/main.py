import argparse

from python_programmers.funcExecutor import FuncExecutor
from python_programmers.judge import Judge
from python_programmers.moduleLoader import ModuleLoader
from python_programmers.testExecutor import TestExecutor


def main():
    parser = argparse.ArgumentParser(
        description="Run a function from a target Python file."
    )
    parser.add_argument(
        "--target", required=True, help="Path to the target Python file."
    )
    parser.add_argument(
        "--func_name",
        default="solution",
        help="Function name to execute (default: solution).",
    )
    args = parser.parse_args()

    loader = ModuleLoader()
    judge = Judge()
    tester = TestExecutor(loader, judge, args.target)

    for idx, (result) in enumerate(tester.gradeOne(), start=1):
        if result:
            print(f"🟢 #{idx}")
        else:
            print(f"🔴 #{idx}")
