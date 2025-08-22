import shutil, os, re
from datetime import datetime
import random


# создание файлового каталога
def creation():
    os.makedirs(r"C:\FileCatalog\Catalog1")
    os.makedirs(r"C:\FileCatalog\Catalog2")
    os.makedirs(r"C:\FileCatalog\Catalog3")
    os.makedirs(r"C:\FileCatalog\Catalog4\Catalog4_1")
    os.makedirs(r"C:\FileCatalog\Catalog4\Catalog4_2")
    os.makedirs(r"C:\FileCatalog\Catalog5\Catalog5_1")

    i = 0
    for i in range(random.randint(1, 10000)):
        my_file = open(r"C:\FileCatalog\Catalog1\File1.txt", "a+")
        my_file.write(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \n")
        my_file.close()
        i += 1

    j = 0
    for j in range(random.randint(1, 10000)):
        my_file = open(r"C:\FileCatalog\Catalog2\File1.txt", "a+")
        my_file.write(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \n")
        my_file.close()
        j += 1

    k = 0
    for k in range(random.randint(1, 10000)):
        my_file = open(r"C:\FileCatalog\Catalog3\File1.txt", "a+")
        my_file.write(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \n")
        my_file.close()
        k += 1

    l = 0
    for l in range(random.randint(1, 10000)):
        my_file = open(r"C:\FileCatalog\Catalog4\Catalog4_1\File1.txt", "a+")
        my_file.write(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \n")
        my_file.close()
        l += 1

    m = 0
    for m in range(random.randint(1, 10000)):
        my_file = open(r"C:\FileCatalog\Catalog4\Catalog4_2\File1.txt", "a+")
        my_file.write(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \n")
        my_file.close()
        m += 1

    n = 0
    for n in range(random.randint(1, 10000)):
        my_file = open(r"C:\FileCatalog\Catalog5\Catalog5_1\File1.txt", "a+")
        my_file.write(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \n")
        my_file.close()
        n += 1

    return r'Тестовый каталог по пути C:\FileCatalog\ создан'


# копирование файла
def copy(path, filename):
    # если filename не указан, добавить к существующему имени _copy
    if filename == 'None':
        dst_file = os.path.split(path)[1].split('.')[0] + "_copy." + os.path.split(path)[1].split('.')[1]
        dst = str(os.path.join(os.path.dirname(path), dst_file))
        shutil.copy(path, dst)
    else:
        shutil.copy(path, filename)
    return 'Файл скопирован'


# удаление файла или папки
def delete(path):
    if os.path.isdir(path):
        os.rmdir(path)
        return 'Папка удалена'
    elif os.path.isfile(path):
        os.remove(path)
        return 'Файл удален'
    return None


# кол-во файлов в папке
def nf(path):
    counter = 0
    for address, dirs, files in os.walk(path):
        for name in files:
            counter += 1
    return str(counter) + " файла(-ов)"


# поиск подходящих файлов по фильтру
def search(path, search_string):
    file_list = []
    for address, dirs, files in os.walk(path):
        for name in files:
            if re.search(search_string, name) is not None:
                file_list.append(os.path.join(address, name))
    return file_list


# добавить дату создания
def add(path):
    for address, dirs, files in os.walk(path):
        for name in files:
            filedate = os.stat(os.path.join(address, name)).st_ctime
            dst_name = name.split('.')[0] + "_" + datetime.fromtimestamp(filedate).strftime('%Y-%m-%d') + "." + \
                       name.split('.')[1]
            os.rename(os.path.join(address, name), os.path.join(address, dst_name))
    return 'Имена всех файлов изменены'


# анализ вложенных файлов и папок
def get_folder_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def analyse(path):
    print(f"Общий размер: {get_folder_size(path) / (1024 * 1024):.2f} MB")
    folder_list = []
    for folder_name in os.listdir(path):
        folder_path = os.path.join(path, folder_name)
        if os.path.isdir(folder_path):
            folder_size = get_folder_size(folder_path)
            folder_list.append(f"Папка: {folder_name} — Размер: {folder_size / (1024 * 1024):.2f} MB")
    return "\n".join(folder_list)
