import unittest
from .funcs import copy, delete, num_files, search, add, analyse, get_folder_size
import os
import datetime
import shutil
from .config import LOREM


class MyTestCase(unittest.TestCase):
    def setUp(self):
        if os.path.exists(os.path.join(os.getcwd(), r"TestCatalog")):
            shutil.rmtree(os.path.join(os.getcwd(), r"TestCatalog"))
        os.mkdir(os.path.join(os.getcwd(), r"TestCatalog"))
        with open(os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt"), "w") as f:
            f.write(LOREM)

    def test_copy(self):
        copy(os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt"), "None")
        self.assertTrue(os.path.isfile(os.path.join(os.getcwd(), r"TestCatalog", r"File1_copy.txt")))

    def test_delete(self):
        delete(os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt"))
        self.assertFalse(os.path.exists(os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt")))

    def test_num_files(self):
        self.assertTrue(num_files(os.path.join(os.getcwd(), r"TestCatalog")) == "1 файла(-ов)")

    def test_search(self):
        self.assertTrue(len(search(os.path.join(os.getcwd(), r"TestCatalog"), "File1")) == 1)
        self.assertTrue(len(search(os.path.join(os.getcwd(), r"TestCatalog"), "File2")) == 0)

    def test_add(self):
        filedate = datetime.datetime.fromtimestamp(
            os.stat(os.path.join(os.getcwd(), r"TestCatalog", r"File1.txt")).st_ctime).strftime(
            '%Y-%m-%d')
        add(os.path.join(os.getcwd(), r"TestCatalog"))
        self.assertTrue(os.path.isfile(os.path.join(os.getcwd(), r"TestCatalog", "File1_" + str(filedate) + ".txt")))

    def test_get_folder_size(self):
        self.assertGreater(get_folder_size(os.path.join(os.getcwd(), r"TestCatalog")), 0)

    def test_analyse(self):
        analyse_result = analyse(os.path.join(os.getcwd(), r"TestCatalog"))
        self.assertEqual(analyse_result, 'Файл: File1.txt — Размер: 0.00 MB')

    def tearDown(self):
        shutil.rmtree(os.path.join(os.getcwd(), r"TestCatalog"))


if __name__ == '__main__':
    unittest.main()
