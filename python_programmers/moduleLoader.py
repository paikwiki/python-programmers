import importlib.util
import os
import sys


class ModuleLoader:
    def __init__(self):
        self.module = None

    def __set_module_path(self, module_path):
        self.module_path = module_path

    def __set_module_name(self, module_name):
        self.module_name = module_name

    def __load_module(self):
        spec = importlib.util.spec_from_file_location(
            self.module_name, self.module_path
        )
        if spec is None:
            raise ImportError(f"Cannot find module at path: {self.module_path}")

        module = importlib.util.module_from_spec(spec)
        sys.modules[self.module_name] = module
        spec.loader.exec_module(module)
        self.module = module

    def set_module(self, module_path):
        self.__set_module_name(os.path.splitext(os.path.basename(module_path))[0])
        self.__set_module_path(os.path.abspath(module_path))
        self.__load_module()

    def get_object(self, object_name):
        if self.module is None:
            raise RuntimeError("Module not loaded. Call load_module() first.")

        if not hasattr(self.module, object_name):
            raise AttributeError(f"'{object_name}' not found in {self.module_name}.")

        return getattr(self.module, object_name)
