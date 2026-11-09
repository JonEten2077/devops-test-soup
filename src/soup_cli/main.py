import tomllib # БАГ 1: Работает только на Python 3.11+. На 3.10 будет ImportError.
import requests # БАГ 2: Мы НЕ добавили эту библиотеку в pyproject.toml. В чистой среде упадет.
import os
import json
import importlib.resources

def main():
    print("Запуск Soup CLI...")
    
    # БАГ 3: Хардкодный путь. На Windows папки /tmp нет, будет ошибка.
    file_path = "/tmp/soup_data.txt"
    with open(file_path, "w") as f:
        f.write("test")
        
    # БАГ 4: Мы читаем файл data.json, но НЕ указали его в package_data. 
    # При установке из Wheel файла не будет.
    with importlib.resources.open_text("soup_cli", "data.json") as f:
        data = json.load(f)
        
    print("Успех! Данные:", data)

if __name__ == "__main__":
    main()
