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

    for idx, (graded) in enumerate(tester.grade_one(), start=1):
        if graded["result"]:
            print(f"🟢 TestCase #{idx}: Success")
        else:
            print(
                f"🔴 TestCase #{idx}: Failure\n"
                + f" - yours:\t{graded["user_output"]}\n"
                + f" - expected:\t{graded["expected_output"]}\n"
                + f" - input:\t{graded["input"]}"
            )
