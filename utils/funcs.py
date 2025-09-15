import shutil, os, re
from datetime import datetime
import random
from .config import LOREM


# создание файлового каталога
def creation():
    if os.path.exists(os.path.join(os.getcwd(), r"FileCatalog")):
        shutil.rmtree(os.path.join(os.getcwd(), r"FileCatalog"))
    os.makedirs(os.path.join(os.getcwd(), r"FileCatalog", r"Catalog1"))
    os.makedirs(os.path.join(os.getcwd(), r"FileCatalog", r"Catalog2"))
    os.makedirs(os.path.join(os.getcwd(), r"FileCatalog", r"Catalog3"))
    os.makedirs(os.path.join(os.getcwd(), r"FileCatalog", r"Catalog4", r"Catalog4_1"))
    os.makedirs(os.path.join(os.getcwd(), r"FileCatalog", r"Catalog4", r"Catalog4_2"))
    os.makedirs(os.path.join(os.getcwd(), r"FileCatalog", r"Catalog5", r"Catalog5_1"))

    with open(os.path.join(os.getcwd(), r"FileCatalog", r"Catalog1", r"File1.txt"), "a+") as file:
        file.write(LOREM * random.randint(1, 10000))

    with open(os.path.join(os.getcwd(), r"FileCatalog", r"Catalog2", r"File1.txt"), "a+") as file:
        file.write(LOREM * random.randint(1, 10000))

    with open(os.path.join(os.getcwd(), r"FileCatalog", r"Catalog3", r"File1.txt"), "a+") as file:
        file.write(LOREM * random.randint(1, 10000))

    with open(os.path.join(os.getcwd(), r"FileCatalog", r"Catalog4", r"Catalog4_1", r"File1.txt"), "a+") as file:
        file.write(LOREM * random.randint(1, 10000))

    with open(os.path.join(os.getcwd(), r"FileCatalog", r"Catalog4", r"Catalog4_2", r"File1.txt"), "a+") as file:
        file.write(LOREM * random.randint(1, 10000))

    with open(os.path.join(os.getcwd(), r"FileCatalog", r"Catalog5", r"Catalog5_1", r"File1.txt"), "a+") as file:
        file.write(LOREM * random.randint(1, 10000))

    return r'Тестовый каталог создан'


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
def num_files(path):
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
            if re.search(str(search_string).lower(), str(name).lower()) is not None:
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
    folder_list = []
    for folder_name in os.listdir(path):
        folder_path = os.path.join(path, folder_name)
        if os.path.isdir(folder_path):
            folder_size = get_folder_size(folder_path)
            folder_list.append(f"\U0001F4C1 {folder_name} — Размер: {folder_size / (1024 * 1024):.2f} MB")
        elif os.path.isfile(folder_path):
            folder_size = os.path.getsize(folder_path)
            folder_list.append(f"\U0001F4C4 {folder_name} — Размер: {folder_size / (1024 * 1024):.2f} MB")

    return "\n".join(sorted(folder_list))
