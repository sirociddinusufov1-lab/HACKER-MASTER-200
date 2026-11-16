
import platform
import os
import sys
import shutil
import datetime

def show_menu():
    tools = {
        "1": ("Номи система", system_name),
        "2": ("Версияи система", system_version),
        "3": ("Версияи Python", python_version),
        "4": ("Меъмории система", architecture),
        "5": ("Номи компютер ё телефон", device_name),
        "6": ("Папкаи корӣ", current_folder),
        "7": ("Папкаи хонагӣ", home_folder),
        "8": ("Маълумоти корбар", username),
        "9": ("Роҳи Python", python_path),
        "10": ("Версияи платформа", platform_info),
        "11": ("Фазои диск", disk_space),
        "12": ("Шумораи файлҳо", file_count),
        "13": ("Санаи ҳозира", current_date),
        "14": ("Вақти ҳозира", current_time),
        "15": ("Муҳити система", environment),
        "16": ("Маълумоти CPU", cpu_info),
        "17": ("Санҷиши папка", folder_check),
        "18": ("Санҷиши файл", file_check),
        "19": ("Ҳисоботи система", system_report),
        "20": ("Маълумоти Python", python_info)
    }

    while True:
        print("\n--- 20 АСБОБИ СИСТЕМА ---")
        for key, value in tools.items():
            print(f"[{key}] {value[0]}")
        print("[0] Бозгашт")

        choice = input("Рақам: ").strip()
        if choice == "0":
            break
        elif choice in tools:
            try:
                tools[choice][1]()
            except OSError as e:
                print("Хато:", e)
        else:
            print("Рақами нодуруст!")

def system_name():
    print("Система:", platform.system())

def system_version():
    print("Версия:", platform.release())

def python_version():
    print("Python:", platform.python_version())

def architecture():
    print("Меъморӣ:", platform.machine())

def device_name():
    print("Ном:", platform.node())

def current_folder():
    print("Папка:", os.getcwd())

def home_folder():
    print("Home:", os.path.expanduser("~"))

def username():
    print("Корбар:", os.environ.get("USER", "Номаълум"))

def python_path():
    print("Роҳи Python:", sys.executable)

def platform_info():
    print(platform.platform())

def disk_space():
    total, used, free = shutil.disk_usage("/")
    print("Ҳамагӣ:", round(total / 1024**3, 2), "GB")
    print("Истифода:", round(used / 1024**3, 2), "GB")
    print("Озод:", round(free / 1024**3, 2), "GB")

def file_count():
    files = [x for x in os.listdir(".") if os.path.isfile(x)]
    print("Файлҳо:", len(files))

def current_date():
    print("Сана:", datetime.date.today())

def current_time():
    print("Вақт:", datetime.datetime.now().strftime("%H:%M:%S"))

def environment():
    print("ОС:", os.name)
    print("Муҳити Python:", sys.implementation.name)

def cpu_info():
    print("Меъмории CPU:", platform.machine())
    print("Шумораи CPU:", os.cpu_count())

def folder_check():
    name = input("Номи папка: ")
    print("Ҳаст." if os.path.isdir(name) else "Нест.")

def file_check():
    name = input("Номи файл: ")
    print("Ҳаст." if os.path.isfile(name) else "Нест.")

def system_report():
    print("Система:", platform.system())
    print("Версия:", platform.release())
    print("Меъморӣ:", platform.machine())
    print("Python:", platform.python_version())
    print("Корбар:", os.environ.get("USER", "Номаълум"))

def python_info():
    print("Python:", sys.version)
    print("Роҳи Python:", sys.executable)
    print("Версияи забон:", sys.implementation.name)
