import unittest
import os

from python_programmers.moduleLoader import ModuleLoader

class ModuleLoaderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module_path = os.path.abspath("tests/test_doubles/sample_module.py")

    def test_모듈을_로드할_수_있다(self):
        loader = ModuleLoader(self.module_path)
        loader.load_module()
        self.assertIsNotNone(loader.module)

    def test_함수의_이름으로_함수를_가져올_수_있다(self):
        loader = ModuleLoader(self.module_path)
        loader.load_module()

        solution_func = loader.get_object("solution")
        self.assertEqual(solution_func(), 'Function "solution()" executed.')

        another_func = loader.get_object("another_func")
        self.assertEqual(another_func(), 'Function "another_func()" executed.')

    def test_모듈에_없는_함수를_가져올_경우_에러를_반환한다(self):
        loader = ModuleLoader(self.module_path)
        loader.load_module()

        with self.assertRaises(AttributeError):
            loader.get_object("non_existent_function")
