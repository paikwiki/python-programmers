class FuncExecutor:
    def __init__(self, func):
        self.__func = func

    def execute(self, *args):
        return self.__func(*args)
