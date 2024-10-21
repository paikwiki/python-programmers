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

    if tester.grade():
        print("🟢")
    else:
        print("🔴")

    # testCases = tester.getTestCases()
    # for idx, (testCase) in enumerate(testCases, start=1):
    #     judge.set_answer(testCase["output"])
    #     userAnswer = executor.execute(*testCase["input"])

    #     if judge.grade(userAnswer):
    #         print(f"🟢 #{idx}")
    #     else:
    #         print(f"🔴 #{idx}")
    #         print(f"  - answer: {testCase["output"]}")
    #         print(f"  - userAnswer: {userAnswer}")
