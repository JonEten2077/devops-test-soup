import importlib.resources
import json
import tempfile
from pathlib import Path

def main():
    print("Starting Soup CLI...")

    # ФИКС 3: Кроссплатформенный временный путь
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "soup_data.txt"
        file_path.write_text("test")

    # ФИКС 4: Современный и безопасный способ чтения файла из пакета
    data_file = importlib.resources.files("soup_cli") / "data.json"
    with data_file.open("r", encoding="utf-8") as f:
        data = json.load(f)

    print("Success! Data:", data)

if __name__ == "__main__":
    main()
