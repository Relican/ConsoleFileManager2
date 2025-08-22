import unittest
import funcs
import os
import datetime


class MyTestCase(unittest.TestCase):
    def test_copy(self):
        os.mkdir(os.getcwd() + r"\TestCatalog")
        my_file = open(os.getcwd() + r"\TestCatalog\File1.txt", "a+")
        my_file.write(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \n")
        my_file.close()
        funcs.copy(os.getcwd() + r"\TestCatalog\File1.txt", "None")
        self.assertTrue(os.path.isfile(os.getcwd() + r"\TestCatalog\File1_copy.txt"))
        for file in os.listdir(os.getcwd() + r"\TestCatalog"):
            file_path = os.path.join(os.getcwd() + r"\TestCatalog", file)
            os.remove(file_path)
        os.rmdir(os.getcwd() + r"\TestCatalog")

    def test_delete(self):
        os.mkdir(os.getcwd() + r"\TestCatalog")
        my_file = open(os.getcwd() + r"\TestCatalog\File1.txt", "a+")
        my_file.write(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \n")
        my_file.close()
        funcs.delete(os.getcwd() + r"\TestCatalog\File1.txt")
        self.assertFalse(os.path.exists(os.getcwd() + r"\TestCatalog\File1.txt"))
        for file in os.listdir(os.getcwd() + r"\TestCatalog"):
            file_path = os.path.join(os.getcwd() + r"\TestCatalog", file)
            os.remove(file_path)
        os.rmdir(os.getcwd() + r"\TestCatalog")

    def test_nf(self):
        os.mkdir(os.getcwd() + r"\TestCatalog")
        my_file = open(os.getcwd() + r"\TestCatalog\File1.txt", "a+")
        my_file.write(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \n")
        my_file.close()
        self.assertTrue(funcs.nf(os.getcwd() + r"\TestCatalog") == "1 файла(-ов)")
        for file in os.listdir(os.getcwd() + r"\TestCatalog"):
            file_path = os.path.join(os.getcwd() + r"\TestCatalog", file)
            os.remove(file_path)
        os.rmdir(os.getcwd() + r"\TestCatalog")

    def test_search(self):
        os.mkdir(os.getcwd() + r"\TestCatalog")
        my_file = open(os.getcwd() + r"\TestCatalog\File1.txt", "a+")
        my_file.write(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \n")
        my_file.close()
        self.assertTrue(len(funcs.search(os.getcwd() + r"\TestCatalog", "File1")) == 1)
        self.assertTrue(len(funcs.search(os.getcwd() + r"\TestCatalog", "File2")) == 0)
        for file in os.listdir(os.getcwd() + r"\TestCatalog"):
            file_path = os.path.join(os.getcwd() + r"\TestCatalog", file)
            os.remove(file_path)
        os.rmdir(os.getcwd() + r"\TestCatalog")

    def test_add(self):
        os.mkdir(os.getcwd() + r"\TestCatalog")
        my_file = open(os.getcwd() + r"\TestCatalog\File1.txt", "a+")
        my_file.write(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \n")
        my_file.close()
        filedate = datetime.datetime.fromtimestamp(os.stat(os.getcwd() + r"\TestCatalog\File1.txt").st_ctime).strftime(
            '%Y-%m-%d')
        funcs.add(os.getcwd() + r"\TestCatalog")
        self.assertTrue(os.path.isfile(os.getcwd() + r"\TestCatalog\File1_" + str(filedate) + ".txt"))
        for file in os.listdir(os.getcwd() + r"\TestCatalog"):
            file_path = os.path.join(os.getcwd() + r"\TestCatalog", file)
            os.remove(file_path)
        os.rmdir(os.getcwd() + r"\TestCatalog")

    def test_get_folder_size(self):
        os.mkdir(os.getcwd() + r"\TestCatalog")
        my_file = open(os.getcwd() + r"\TestCatalog\File1.txt", "a+")
        my_file.write(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \n")
        my_file.close()
        self.assertTrue(funcs.get_folder_size(os.getcwd() + r"\TestCatalog") == 448)
        for file in os.listdir(os.getcwd() + r"\TestCatalog"):
            file_path = os.path.join(os.getcwd() + r"\TestCatalog", file)
            os.remove(file_path)
        os.rmdir(os.getcwd() + r"\TestCatalog")

    def test_analyse(self):
        os.mkdir(os.getcwd() + r"\TestCatalog")
        my_file = open(os.getcwd() + r"\TestCatalog\File1.txt", "a+")
        my_file.write(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \n")
        my_file.close()
        analyse_result = funcs.analyse(os.getcwd() + r"\TestCatalog")
        self.assertEqual(analyse_result, '')
        for file in os.listdir(os.getcwd() + r"\TestCatalog"):
            file_path = os.path.join(os.getcwd() + r"\TestCatalog", file)
            os.remove(file_path)
        os.rmdir(os.getcwd() + r"\TestCatalog")


if __name__ == '__main__':
    unittest.main()
