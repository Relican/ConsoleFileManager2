import os, unittest, subprocess, sys, shutil
import utils



class TestCLI(unittest.TestCase):
    def setUp(self):
        if os.path.exists(os.path.join(os.getcwd(), r"TestCatalog")):
            shutil.rmtree(os.path.join(os.getcwd(), r"TestCatalog"))
        os.mkdir(os.path.join(os.getcwd(), r"TestCatalog"))
        with open(os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt"), "w") as file:
            file.write(utils.LOREM)

    def test_cli_valid_expressions(self):
        test_cases = [
            ('copy', os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt"), 'None')
        ]

        for operation, path, second_path in test_cases:
            with self.subTest(operation=operation, path=path, second_path=second_path):
                cli_result = subprocess.run([sys.executable, 'manager.py', operation, path, second_path],
                                            capture_output=True,
                                            text=True)
                self.assertEqual(cli_result.stdout, "Файл скопирован\n")

    def test_cli_invalid_expressions(self):

        test_cases = [
            ('shmopy', os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt"), 'None')
        ]

        for operation, path, second_path in test_cases:
            with self.subTest(operation=operation, path=path, second_path=second_path):
                cli_result = subprocess.run([sys.executable, 'manager.py', operation, path, second_path],
                                            capture_output=True,
                                            text=True)
                self.assertEqual(cli_result.returncode, 2)

    def tearDown(self):
        shutil.rmtree(os.path.join(os.getcwd(), r"TestCatalog"))


if __name__ == '__main__':
    unittest.main(argv=['', ], exit=False)
