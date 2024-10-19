class FuncExecutor():
    def __init__(self, func):
        self.__func = func

    def execute(self):
        return self.__func()
