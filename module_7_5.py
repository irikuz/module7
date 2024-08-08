import os
import time

directory = "."
current_dir = os.getcwd()
files_in_dir = os.listdir(current_dir)

for root, dirs, files in os.walk(directory):
    for file in files_in_dir:
        file_path = os.path.join(file)
        file_time = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
        file_size = os.path.getsize(file)
        parent_dir = os.path.dirname(file_path)
        

        print(
            f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт, Время изменения {formatted_time}'
            f'Родительская директория: {parent_dir}')
