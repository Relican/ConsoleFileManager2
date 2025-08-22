import os
import unittest
import subprocess
import sys


class TestCLI(unittest.TestCase):

    def test_cli_valid_expressions(self):
        os.mkdir(os.getcwd() + r'\TestCatalog')
        my_file = open(os.getcwd() + r"\TestCatalog\File1.txt", "a+")
        my_file.write(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \n")
        my_file.close()

        test_cases = [
            ('copy', os.getcwd() + r'\TestCatalog\File1.txt')
        ]

        for operation, path in test_cases:
            with self.subTest(operation=operation, path=path):
                cli_result = subprocess.run([sys.executable, 'manager.py', operation, path], capture_output=True,
                                            text=True)
                self.assertEqual(cli_result.stdout, "Файл скопирован\n")

        for file in os.listdir(os.getcwd() + r"\TestCatalog"):
            file_path = os.path.join(os.getcwd() + r"\TestCatalog", file)
            os.remove(file_path)
        os.rmdir(os.getcwd() + r"\TestCatalog")

    def test_cli_invalid_expressions(self):
        os.mkdir(os.getcwd() + r'\TestCatalog')
        my_file = open(os.getcwd() + r"\TestCatalog\File1.txt", "a+")
        my_file.write(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \n")
        my_file.close()

        test_cases = [
            ('shmopy', os.getcwd() + r'\TestCatalog\File1.txt')
        ]

        for operation, path in test_cases:
            with self.subTest(operation=operation, path=path):
                cli_result = subprocess.run([sys.executable, 'manager.py', operation, path], capture_output=True,
                                            text=True)
                self.assertEqual(cli_result.returncode, 2)

        for file in os.listdir(os.getcwd() + r"\TestCatalog"):
            file_path = os.path.join(os.getcwd() + r"\TestCatalog", file)
            os.remove(file_path)
        os.rmdir(os.getcwd() + r"\TestCatalog")


if __name__ == '__main__':
    unittest.main(argv=['', ], exit=False)
