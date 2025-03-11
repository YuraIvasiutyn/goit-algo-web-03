import os
import shutil
import concurrent.futures
from pathlib import Path


def copy_file(src_file, dest_dir):
    ext = src_file.suffix.lstrip('.').lower()
    if ext:
        target_dir = dest_dir / ext
        target_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy(src_file, target_dir)
        print(f"Копіюється файл: {src_file} до {target_dir}")


def process_directory(src_dir, dest_dir):
    with concurrent.futures.ThreadPoolExecutor() as exacutor:
        for root, dirs, files in os.walk(src_dir):
            futures = []
            for file in files:
                src_file = Path(root) / file
                futures.append(exacutor.submit(copy_file, src_file, dest_dir))

            for future in futures:
                future.result()


if __name__ == "__main__":
    src_dir = input("Введіть шлях до директорії з файлами для обробки: ")
    dest_dir = input(
        "Введіть шлях до директорії для збереження відсортованих файлів (за замовчуванням 'dist'): ") or "dist"

    if not os.path.exists(src_dir):
        print(f"Директорія {src_dir} не існує.")
    else:
        dest_path = Path(dest_dir)
        dest_path.mkdir(parents=True, exist_ok=True)
        process_directory(src_dir, dest_path)
        print(f"Файли були успішно скопійовані в {dest_path}")