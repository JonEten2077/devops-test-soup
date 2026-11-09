import os
import json
import tempfile
import importlib.resources

def main():
    print("Запуск Soup CLI...")
    
    # ФИКС 3: Используем кроссплатформенный временный путь (работает на Windows и Linux)
    file_path = os.path.join(tempfile.gettempdir(), "soup_data.txt")
    with open(file_path, "w") as f:
        f.write("test")
        
    # ФИКС 4: Читаем data.json (теперь он включен в пакет благодаря правкам в pyproject.toml)
    with importlib.resources.open_text("soup_cli", "data.json") as f:
        data = json.load(f)
        
    print("Успех! Данные:", data)

if __name__ == "__main__":
    main()
