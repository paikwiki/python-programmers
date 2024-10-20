import argparse

from python_programmers.funcExecutor import FuncExecutor
from python_programmers.judge import Judge
from python_programmers.moduleLoader import ModuleLoader

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

    for idx, ((inputs_and_output)) in enumerate(inputs_and_outputs, start=1):
        *inputs, output = inputs_and_output
        judge.setAnswer(output)
        userAnswer = executor.execute(*inputs)

        if judge.grade(userAnswer):
            print(f"🟢 #{idx} ")
        else:
            print(f"🔴 #{idx} {userAnswer=}")
            print(f"  - answer: {output}")
            print(f"  - input: {input}")
