import argparse

from funcExecutor import FuncExecutor
from judge import Judge
from moduleLoader import ModuleLoader

ANSWER = 42


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

    loader = ModuleLoader(args.target)
    loader.load_module()

    func = loader.get_object(args.func_name)
    inputs_and_outputs = loader.get_object("inputs_and_outputs")

    executor = FuncExecutor(func)

    judge = Judge()

    for idx, (input, output) in enumerate(inputs_and_outputs, start=1):
        judge.setAnswer(output)
        userAnswer = executor.execute(input)

        if judge.grade(userAnswer):
            print(f"🟢 #{idx} ")
        else:
            print(f"🔴 #{idx} {userAnswer=}")
            print(f"  - answer: {output}")
            print(f"  - input: {input}")


if __name__ == "__main__":
    main()
