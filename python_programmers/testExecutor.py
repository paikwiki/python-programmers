from python_programmers.moduleLoader import ModuleLoader


class TestExecutor:
    def __init__(self, moduleLoader: ModuleLoader, filePath: str):
        self.moduleLoader = moduleLoader
        self.moduleLoader.set_module(filePath)

    def getTestCases(self):
        inputs_and_outputs = self.moduleLoader.get_object("inputs_and_outputs")

        testCases = []
        for inputs_and_output in inputs_and_outputs:
            *input, output = inputs_and_output
            testCases.append({"input": tuple(input), "output": output})

        return tuple(testCases)
