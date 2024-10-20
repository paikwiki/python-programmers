import unittest

from python_programmers.funcExecutor import FuncExecutor


def sample_func():
    return 42


class FuncExecutorTest(unittest.TestCase):
    def test_is_defined(self):
        # when
        funcExecutor = FuncExecutor(sample_func)

        # then
        self.assertTrue(funcExecutor)

    def test_생성자에_전달받은_함수를_실행할_수_있다(self):

        # when
        result = FuncExecutor(sample_func).execute()

        # then
        self.assertEqual(result, 42)

    def test_인자와_함께_함수를_실행할_수_있다(self):
        # given
        def test_func(a):
            return 41 + a

        # when
        result = FuncExecutor(test_func).execute(1)

        # then
        self.assertEqual(result, 42)
