import os
import unittest

from python_programmers.moduleLoader import ModuleLoader


class ModuleLoaderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module_path = os.path.abspath("tests/test_doubles/sample_module.py")

    def test_is_defined(self):
        # when
        loader = ModuleLoader()
        loader.set_module(self.module_path)

        # then
        self.assertTrue(loader)

    def test_모듈을_로드할_수_있다(self):
        # when
        loader = ModuleLoader()
        loader.set_module(self.module_path)

        # then
        self.assertIsNotNone(loader.module)

    def test_함수의_이름으로_함수를_가져올_수_있다(self):
        # when
        loader = ModuleLoader()
        loader.set_module(self.module_path)

        solution_func = loader.get_object("solution")
        another_func = loader.get_object("another_func")

        # then
        self.assertEqual(solution_func(), 'Function "solution()" executed.')
        self.assertEqual(another_func(), 'Function "another_func()" executed.')

    def test_모듈에_없는_함수를_가져올_경우_에러를_반환한다(self):
        # when
        loader = ModuleLoader()
        loader.set_module(self.module_path)

        # then
        with self.assertRaises(AttributeError):
            loader.get_object("non_existent_function")
