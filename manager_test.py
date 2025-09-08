import os
import unittest
import subprocess
import sys
import utils



class TestCLI(unittest.TestCase):

    def test_cli_valid_expressions(self):
        if os.path.exists(os.path.join(os.getcwd(), r"TestCatalog")):
            os.rmdir(os.path.join(os.getcwd(), r"TestCatalog"))
        os.mkdir(os.path.join(os.getcwd(), r"TestCatalog"))
        my_file = open(os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt"), "a+")
        my_file.write(utils.LOREM)
        my_file.close()

        test_cases = [
            ('copy', os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt"))
        ]

        for operation, path in test_cases:
            with self.subTest(operation=operation, path=path):
                cli_result = subprocess.run([sys.executable, 'manager.py', operation, path], capture_output=True,
                                            text=True)
                self.assertEqual(cli_result.stdout, "Файл скопирован\n")

        for file in os.listdir(os.path.join(os.getcwd(), r"TestCatalog")):
            file_path = os.path.join(os.getcwd(), r"TestCatalog", file)
            os.remove(file_path)
        os.rmdir(os.path.join(os.getcwd(), r"TestCatalog"))

    def test_cli_invalid_expressions(self):
        if os.path.exists(os.path.join(os.getcwd(), r"TestCatalog")):
            os.rmdir(os.path.join(os.getcwd(), r"TestCatalog"))
        os.mkdir(os.path.join(os.getcwd(), r"TestCatalog"))
        my_file = open(os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt"), "a+")
        my_file.write(utils.LOREM)
        my_file.close()

        test_cases = [
            ('shmopy', os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt"))
        ]

        for operation, path in test_cases:
            with self.subTest(operation=operation, path=path):
                cli_result = subprocess.run([sys.executable, 'manager.py', operation, path], capture_output=True,
                                            text=True)
                self.assertEqual(cli_result.returncode, 2)

        for file in os.listdir(os.path.join(os.getcwd(), r"TestCatalog")):
            file_path = os.path.join(os.getcwd(), r"TestCatalog", file)
            os.remove(file_path)
        os.rmdir(os.path.join(os.getcwd(), r"TestCatalog"))


if __name__ == '__main__':
    unittest.main(argv=['', ], exit=False)
