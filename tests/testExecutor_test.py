import os
import unittest

from python_programmers.funcExecutor import FuncExecutor
from python_programmers.judge import Judge
from python_programmers.moduleLoader import ModuleLoader
from python_programmers.testExecutor import TestExecutor


class TestExecutorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        moduleLoader = ModuleLoader()
        judge = Judge()
        cls.target_quiz_path = os.path.abspath("tests/test_doubles/sample_quiz.py")
        cls.tester = TestExecutor(
            moduleLoader,
            judge,
            os.path.abspath("tests/test_doubles/sample_quiz.py"),
        )

    def test_is_defined(self):
        # then
        self.assertTrue(self.tester)

    def test_유저의_테스트_케이스를_반환할_수_있다(self):
        # when
        testCases = self.tester.getTestCases()

        # then
        self.assertEqual(
            testCases,
            (
                {"input": (2, 3), "output": -1},
                {"input": (44, 2), "output": 42},
            ),
        )

    def test_유저의_정답_여부를_확인할_수_있다_case1_모두_정답(self):
        # when
        result = self.tester.grade()

        # then
        self.assertTrue(result)

    def test_유저의_정답_여부를_확인할_수_있다_case2_모두_오답(self):
        # given
        moduleLoader = ModuleLoader()
        judge = Judge()
        tester = TestExecutor(
            moduleLoader,
            judge,
            os.path.abspath("tests/test_doubles/sample_quiz_with_incorrect.py"),
        )

        # when
        result = tester.grade()

        # then
        self.assertFalse(result)
