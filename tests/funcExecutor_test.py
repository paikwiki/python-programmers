import unittest

from python_programmers.funcExecutor import FuncExecutor


class FuncExecutorTest(unittest.TestCase):
    def test_생성자에_전달받은_함수를_실행할_수_있다(self):
        # given
        def test_func():
            return 42

        # when
        result = FuncExecutor(test_func).execute()

        # then
        self.assertEqual(result, 42)
