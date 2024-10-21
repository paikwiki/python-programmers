import os
import unittest

from python_programmers.funcExecutor import FuncExecutor
from python_programmers.judge import Judge
from python_programmers.moduleLoader import ModuleLoader
from python_programmers.testExecutor import TestExecutor


class TestExecutorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        module_loader = ModuleLoader()
        judge = Judge()
        cls.target_quiz_path = os.path.abspath("tests/test_doubles/sample_quiz.py")
        cls.tester = TestExecutor(
            module_loader,
            judge,
            os.path.abspath("tests/test_doubles/sample_quiz.py"),
        )

    def test_is_defined(self):
        # then
        self.assertTrue(self.tester)

    def test_유저의_정답_여부를_각_테스트케이스별로_확인할_수_있다_case1_모두_정답(
        self,
    ):
        # when
        results = []
        for result in self.tester.grade_one():
            results.append(result)

        # then
        expected = [
            {"expected_output": -1, "input": (2, 3), "result": True, "user_output": -1},
            {
                "expected_output": 42,
                "input": (44, 2),
                "result": True,
                "user_output": 42,
            },
        ]

        self.assertEqual(results, expected)

    def test_유저의_정답_여부를_각_테스트케이스별로_확인할_수_있다_case2_오답_포함(
        self,
    ):
        # given
        module_loader = ModuleLoader()
        judge = Judge()
        tester = TestExecutor(
            module_loader,
            judge,
            os.path.abspath("tests/test_doubles/sample_quiz_with_incorrect.py"),
        )

        # when
        results = []
        for result in tester.grade_one():
            results.append(result)

        # then
        expected = [
            {"expected_output": 5, "input": (2, 3), "result": True, "user_output": 5},
            {
                "expected_output": 42,
                "input": (40, 2),
                "result": False,
                "user_output": 43,
            },
        ]
        self.assertEqual(
            results,
            expected,
        )
