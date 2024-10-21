from python_programmers.funcExecutor import FuncExecutor
from python_programmers.judge import Judge
from python_programmers.moduleLoader import ModuleLoader


class TestExecutor:
    def __init__(
        self,
        moduleLoader: ModuleLoader,
        judge: Judge,
        filePath: str,
    ):
        self.moduleLoader = moduleLoader
        self.judge = judge
        self.moduleLoader.set_module(filePath)
        self.__testCases = self.__parseTestCases()

    def __parseTestCases(self):
        inputs_and_outputs = self.moduleLoader.get_object("inputs_and_outputs")

        testCases = []
        for inputs_and_output in inputs_and_outputs:
            *input, output = inputs_and_output
            testCases.append({"input": tuple(input), "output": output})

        return tuple(testCases)

    def grade(self):
        funcExecutor = FuncExecutor(self.moduleLoader.get_object("solution"))

        resultList = []
        for testCase in self.__testCases:
            self.judge.set_answer(testCase["output"])
            userAnswer = funcExecutor.execute(*testCase["input"])
            resultList.append(self.judge.grade(userAnswer))

        return all(resultList)
