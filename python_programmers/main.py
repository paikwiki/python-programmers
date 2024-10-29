import argparse
import os

from python_programmers import config
from python_programmers.funcExecutor import FuncExecutor
from python_programmers.judge import Judge
from python_programmers.moduleLoader import ModuleLoader
from python_programmers.testExecutor import TestExecutor


def main():
    parser = argparse.ArgumentParser(
        description="Run a function from a target Python file."
    )
    parser.add_argument("--target", help="Path to the target Python file.")
    parser.add_argument(
        "--func_name",
        default="solution",
        help="Function name to execute (default: solution).",
    )
    parser.add_argument(
        "--latest",
        default="true",
        choices=["true", "false"],
        help="Whether to use the latest edited Python file (default: true).",
    )
    args = parser.parse_args()

    if args.target:
        target = args.target
    else:
        if args.latest == "true":
            quizz_files = os.listdir(config.DEFAULT_QUIZZES_DIR)
            quizz_files = [f for f in quizz_files if f.endswith(".py")]
            latest_edited_file = max(
                quizz_files,
                key=lambda f: os.path.getmtime(
                    os.path.join(config.DEFAULT_QUIZZES_DIR, f)
                ),
            )
            target = f"{config.DEFAULT_QUIZZES_DIR}/{latest_edited_file}"
        else:
            print("Please provide a target Python file.")
            exit(1)

    loader = ModuleLoader()
    judge = Judge()
    tester = TestExecutor(loader, judge, target)

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
