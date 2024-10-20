import sys
import unittest

def main():
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_suite = unittest.defaultTestLoader.discover("tests", pattern="*.py")
    result = test_runner.run(test_suite)
    sys.exit(not result.wasSuccessful())

if __name__ == "__main__":
    main()
