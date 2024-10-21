import os
import unittest

from python_programmers.moduleLoader import ModuleLoader
from python_programmers.testExecutor import TestExecutor


class TestExecutorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.target_quiz_path = os.path.abspath("tests/test_doubles/sample_quiz.py")

    def test_is_defined(self):
        # when
        moduleLoader = ModuleLoader()
        tester = TestExecutor(moduleLoader, self.target_quiz_path)

        # then
        self.assertTrue(tester)

    def test_유저의_테스트_케이스를_반환할_수_있다(self):
        # when
        moduleLoader = ModuleLoader()
        testCases = TestExecutor(moduleLoader, self.target_quiz_path).getTestCases()

        # then
        self.assertEqual(
            testCases,
            (
                {"input": (2, 3), "output": -1},
                {"input": (44, 2), "output": 42},
            ),
        )
