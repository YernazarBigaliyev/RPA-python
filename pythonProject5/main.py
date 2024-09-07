from pathlib import Path
from collections import defaultdict


# Функция для рекурсивной категоризации файлов по их расширению (типу)
def categorize_files_by_type(folder_path):
    # Создаем defaultdict, где ключ — это расширение файла, а значение — список файлов
    files_by_type = defaultdict(list)

    # Проходим по всем элементам в указанной директории
    for item in folder_path.iterdir():
        # Проверяем, является ли элемент файлом
        if item.is_file():
            # Добавляем файл в словарь по его расширению
            files_by_type[item.suffix].append(str(item))
        # Проверяем, является ли элемент директорией (папкой)
        elif item.is_dir():
            # Рекурсивно заходим в поддиректории
            nested_files = categorize_files_by_type(item)
            # Объединяем результаты из вложенной директории с основным словарем
            for file_type, files in nested_files.items():
                files_by_type[file_type].extend(files)

    return files_by_type


# Указываем путь к директории
directory_path = Path(r"C:\Users\user\Desktop\TestTask")

# Получаем файлы, сгруппированные по расширению, из указанной директории и её поддиректорий
files_by_type = categorize_files_by_type(directory_path)

# Выводим результат, где каждый тип файлов выводится с соответствующим списком файлов
for file_type, files in files_by_type.items():
    print(f"{file_type}: {files}")
