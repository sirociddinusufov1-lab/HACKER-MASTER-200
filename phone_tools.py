
import platform
import os
import shutil

def show_menu():
    tools = {
        "1": ("Номи система", system_name),
        "2": ("Версияи система", system_version),
        "3": ("Маълумоти Python", python_version),
        "4": ("Меъмории телефон", architecture),
        "5": ("Номи дастгоҳ", device_name),
        "6": ("Папкаи корӣ", current_folder),
        "7": ("Рӯйхати файлҳо", list_files),
        "8": ("Фазои диск", disk_space),
        "9": ("Папкаи хонагӣ", home_folder),
        "10": ("Санҷиши батарея", battery_info),
        "11": ("Санҷиши Android", android_check),
        "12": ("Маълумоти корбар", username),
        "13": ("Санҷиши Python", python_check),
        "14": ("Мавҷудияти файл", file_check),
        "15": ("Сохтани папка", make_folder),
        "16": ("Санҷиши интернет", internet_check),
        "17": ("Вақти кори система", uptime_info),
        "18": ("Маълумоти экран", screen_info),
        "19": ("Муҳити Termux", termux_info),
        "20": ("Ҳисоботи телефон", phone_report)
    }

    while True:
        print("\n--- 20 АСБОБИ ТЕЛЕФОН ---")
        for key, value in tools.items():
            print(f"[{key}] {value[0]}")
        print("[0] Бозгашт")

        choice = input("Рақам: ").strip()
        if choice == "0":
            break
        elif choice in tools:
            try:
                tools[choice][1]()
            except Exception as e:
                print("Хато:", e)
        else:
            print("Рақами нодуруст!")

def system_name():
    print("Система:", platform.system())

def system_version():
    print("Версия:", platform.version())

def python_version():
    print("Python:", platform.python_version())

def architecture():
    print("Меъморӣ:", platform.machine())

def device_name():
    print("Дастгоҳ:", platform.node())

def current_folder():
    print("Папка:", os.getcwd())

def list_files():
    for name in os.listdir("."):
        print(name)

def disk_space():
    total, used, free = shutil.disk_usage("/")
    print("Ҳамагӣ:", round(total / 1024**3, 2), "GB")
    print("Истифода шудааст:", round(used / 1024**3, 2), "GB")
    print("Озод:", round(free / 1024**3, 2), "GB")

def home_folder():
    print("Home:", os.path.expanduser("~"))

def battery_info():
    print("Маълумоти батарея дар ин версияи Termux дастрас нест.")

def android_check():
    print("Система:", platform.platform())

def username():
    print("Корбар:", os.environ.get("USER", "Номаълум"))

def python_check():
    print("Python кор мекунад!")

def file_check():
    name = input("Номи файл: ")
    print("Файл ҳаст." if os.path.isfile(name) else "Файл ёфт нашуд.")

def make_folder():
    name = input("Номи папкаи нав: ")
    if name:
        os.makedirs(name, exist_ok=True)
        print("Папка сохта шуд!")

def internet_check():
    print("Барои санҷиши интернет аз менюи шабака истифода бар.")

def uptime_info():
    print("Маълумоти вақти кори телефон дар ин муҳит дастрас нест.")

def screen_info():
    print("Маълумоти экранро аз танзимоти Android бин.")

def termux_info():
    print("Муҳити иҷро: Termux")
    print("Python:", platform.python_version())

def phone_report():
    print("Система:", platform.system())
    print("Версия:", platform.release())
    print("Меъморӣ:", platform.machine())
    print("Python:", platform.python_version())
    print("Папка:", os.getcwd())
