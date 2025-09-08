import unittest
from .funcs import copy, delete, nf, search, add, analyse, get_folder_size
import os
import datetime
from .config import LOREM

class MyTestCase(unittest.TestCase):
    def test_copy(self):
        if os.path.exists(os.path.join(os.getcwd(), r"TestCatalog")):
            os.rmdir(os.path.join(os.getcwd(), r"TestCatalog"))
        os.mkdir(os.path.join(os.getcwd(), r"TestCatalog"))
        my_file = open(os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt"), "a+")
        my_file.write(LOREM)
        my_file.close()

        copy(os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt"), "None")
        self.assertTrue(os.path.isfile(os.path.join(os.getcwd(), r"TestCatalog", r"File1_copy.txt")))

        for file in os.listdir(os.path.join(os.getcwd(), r"TestCatalog")):
            file_path = os.path.join(os.path.join(os.getcwd(), r"TestCatalog", file))
            os.remove(file_path)
        os.rmdir(os.path.join(os.getcwd(), r"TestCatalog"))

    def test_delete(self):
        if os.path.exists(os.path.join(os.getcwd(), r"TestCatalog")):
            os.rmdir(os.path.join(os.getcwd(), r"TestCatalog"))
        os.mkdir(os.path.join(os.getcwd(), r"TestCatalog"))
        my_file = open(os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt"), "a+")
        my_file.write(LOREM)
        my_file.close()

        delete(os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt"))
        self.assertFalse(os.path.exists(os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt")))

        for file in os.listdir(os.path.join(os.getcwd(), r"TestCatalog")):
            file_path = os.path.join(os.path.join(os.getcwd(), r"TestCatalog", file))
            os.remove(file_path)
        os.rmdir(os.path.join(os.getcwd(), r"TestCatalog"))

    def test_nf(self):
        if os.path.exists(os.path.join(os.getcwd(), r"TestCatalog")):
            os.rmdir(os.path.join(os.getcwd(), r"TestCatalog"))
        os.mkdir(os.path.join(os.getcwd(), r"TestCatalog"))
        my_file = open(os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt"), "a+")
        my_file.write(LOREM)
        my_file.close()

        self.assertTrue(nf(os.path.join(os.getcwd(), r"TestCatalog")) == "1 файла(-ов)")

        for file in os.listdir(os.path.join(os.getcwd(), r"TestCatalog")):
            file_path = os.path.join(os.path.join(os.getcwd(), r"TestCatalog", file))
            os.remove(file_path)
        os.rmdir(os.path.join(os.getcwd(), r"TestCatalog"))

    def test_search(self):
        if os.path.exists(os.path.join(os.getcwd(), r"TestCatalog")):
            os.rmdir(os.path.join(os.getcwd(), r"TestCatalog"))
        os.mkdir(os.path.join(os.getcwd(), r"TestCatalog"))
        my_file = open(os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt"), "a+")
        my_file.write(LOREM)
        my_file.close()

        self.assertTrue(len(search(os.path.join(os.getcwd(), r"TestCatalog"), "File1")) == 1)
        self.assertTrue(len(search(os.path.join(os.getcwd(), r"TestCatalog"), "File2")) == 0)

        for file in os.listdir(os.path.join(os.getcwd(), r"TestCatalog")):
            file_path = os.path.join(os.path.join(os.getcwd(), r"TestCatalog", file))
            os.remove(file_path)
        os.rmdir(os.path.join(os.getcwd(), r"TestCatalog"))

    def test_add(self):
        if os.path.exists(os.path.join(os.getcwd(), r"TestCatalog")):
            os.rmdir(os.path.join(os.getcwd(), r"TestCatalog"))
        os.mkdir(os.path.join(os.getcwd(), r"TestCatalog"))
        my_file = open(os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt"), "a+")
        my_file.write(LOREM)
        my_file.close()

        filedate = datetime.datetime.fromtimestamp(os.stat(os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt")).st_ctime).strftime(
            '%Y-%m-%d')
        add(os.path.join(os.getcwd(), r"TestCatalog"))
        self.assertTrue(os.path.isfile(os.path.join(os.getcwd(), r"TestCatalog", "File1_" + str(filedate) + ".txt")))

        for file in os.listdir(os.path.join(os.getcwd(), r"TestCatalog")):
            file_path = os.path.join(os.path.join(os.getcwd(), r"TestCatalog", file))
            os.remove(file_path)
        os.rmdir(os.path.join(os.getcwd(), r"TestCatalog"))

    def test_get_folder_size(self):
        if os.path.exists(os.path.join(os.getcwd(), r"TestCatalog")):
            os.rmdir(os.path.join(os.getcwd(), r"TestCatalog"))
        os.mkdir(os.path.join(os.getcwd(), r"TestCatalog"))
        my_file = open(os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt"), "a+")
        my_file.write(LOREM)
        my_file.close()

        self.assertTrue(get_folder_size(os.path.join(os.getcwd(), r"TestCatalog")) == 448)

        for file in os.listdir(os.path.join(os.getcwd(), r"TestCatalog")):
            file_path = os.path.join(os.path.join(os.getcwd(), r"TestCatalog", file))
            os.remove(file_path)
        os.rmdir(os.path.join(os.getcwd(), r"TestCatalog"))

    def test_analyse(self):
        if os.path.exists(os.path.join(os.getcwd(), r"TestCatalog")):
            os.rmdir(os.path.join(os.getcwd(), r"TestCatalog"))
        os.mkdir(os.path.join(os.getcwd(), r"TestCatalog"))
        my_file = open(os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt"), "a+")
        my_file.write(LOREM)
        my_file.close()

        analyse_result = analyse(os.path.join(os.getcwd(), r"TestCatalog"))
        self.assertEqual(analyse_result, '')

        for file in os.listdir(os.path.join(os.getcwd(), r"TestCatalog")):
            file_path = os.path.join(os.path.join(os.getcwd(), r"TestCatalog", file))
            os.remove(file_path)
        os.rmdir(os.path.join(os.getcwd(), r"TestCatalog"))


if __name__ == '__main__':
    unittest.main()
