import os
import re

def rename_files(folder_path, series_name, season_number):
    # Проверяем, что путь к папке существует и это действительно папка
    if not os.path.isdir(folder_path):
        print("Указанный путь не является папкой или не существует.")
        return
    
    # Получаем список файлов в папке
    files = os.listdir(folder_path)
    
    # Проходимся по всем файлам в папке
    for file_name in files:
        # Извлекаем номер серии из имени файла, используя регулярное выражение
        match = re.search(r'\d+', file_name)
        if match:
            episode_number = match.group()
        else:
            episode_number = "???"  # Если номер серии не найден, ставим ??? вместо номера
        
        # Заменяем пробелы на точки в имени файла
        new_file_name = series_name.replace(' ', '.')
        
        file_name_parts = os.path.splitext(file_name)
        extension = file_name_parts[1]
        
        # Формируем новое имя файла с номером сезона и номером серии
        new_file_name_with_season = f"{new_file_name}.S{season_number:02d}E{episode_number}{extension}"
        
        # Формируем полные пути к старому и новому файлам
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name_with_season)
        
        # Переименовываем файл
        os.rename(old_file_path, new_file_path)
        
        print(f"Переименован файл: {file_name} -> {new_file_name_with_season}")

# Пример использования функции
folder_path = "D:\\путь\\до\\папки"
series_name = "название сериала"
season_number = 1
rename_files(folder_path, series_name, season_number)
