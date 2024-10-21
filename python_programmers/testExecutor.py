from python_programmers.funcExecutor import FuncExecutor
from python_programmers.judge import Judge
from python_programmers.moduleLoader import ModuleLoader


class TestExecutor:
    def __init__(
        self,
        module_loader: ModuleLoader,
        judge: Judge,
        file_path: str,
    ):
        self.module_loader = module_loader
        self.judge = judge
        self.module_loader.set_module(file_path)
        self.__test_cases = self.__parse_test_cases()

    def __parse_test_cases(self):
        inputs_and_outputs = self.module_loader.get_object("inputs_and_outputs")

        test_cases = []
        for inputs_and_output in inputs_and_outputs:
            *input, output = inputs_and_output
            test_cases.append({"input": tuple(input), "output": output})

        return tuple(test_cases)

    def grade_one(self):
        func_executor = FuncExecutor(self.module_loader.get_object("solution"))

        for test_case in self.__test_cases:
            self.judge.set_answer(test_case["output"])
            user_answer = func_executor.execute(*test_case["input"])
            judge_result = self.judge.grade(user_answer)
            result = {
                "input": test_case["input"],
                "expected_output": self.judge.answer,
                "user_output": judge_result["user_output"],
                "result": judge_result["result"],
            }

            yield result
