
import os
from datetime import datetime

HISTORY_FILE = "history.txt"

def save_history(action):
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {action}\n")

def show_menu():
    tools = {
        "1": ("Сабти амали нав", add_history),
        "2": ("Намоиши таърих", show_history),
        "3": ("Шумораи сабтҳо", count_history),
        "4": ("Ҷустуҷӯи таърих", search_history),
        "5": ("Сабти сана", show_date),
        "6": ("Сабти вақти ҳозира", show_time),
        "7": ("Намоиши 5 сабти охир", last_five),
        "8": ("Намоиши 10 сабти охир", last_ten),
        "9": ("Санҷиши файли таърих", check_history),
        "10": ("Номи файли таърих", file_name),
        "11": ("Ҳаҷми таърих", history_size),
        "12": ("Сабти ёддошт", add_note),
        "13": ("Ҷустуҷӯи ёддошт", search_note),
        "14": ("Намоиши сабтҳо аз рӯи калима", filter_history),
        "15": ("Нусхаи таърих", backup_history),
        "16": ("Намоиши роҳи файл", history_path),
        "17": ("Сабти санҷиши амният", security_record),
        "18": ("Сабти омӯзиши Python", python_record),
        "19": ("Сабти кори шабака", network_record),
        "20": ("Маълумоти умумии таърих", history_info)
    }

    while True:
        print("\n--- 20 АСБОБИ ТАЪРИХ ---")
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
                print("Хатои файл:", e)
        else:
            print("Рақами нодуруст!")

def read_history():
    if not os.path.isfile(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        return f.readlines()

def add_history():
    action = input("Амали анҷомдода: ")
    save_history(action)
    print("Сабт шуд!")

def show_history():
    lines = read_history()
    print("".join(lines) if lines else "Таърих холӣ аст.")

def count_history():
    print("Шумораи сабтҳо:", len(read_history()))

def search_history():
    word = input("Калима: ")
    results = [x for x in read_history() if word.lower() in x.lower()]
    print("".join(results) if results else "Ёфт нашуд.")

def show_date():
    print("Сана:", datetime.now().strftime("%Y-%m-%d"))

def show_time():
    print("Вақт:", datetime.now().strftime("%H:%M:%S"))

def last_five():
    print("".join(read_history()[-5:]) or "Таърих холӣ аст.")

def last_ten():
    print("".join(read_history()[-10:]) or "Таърих холӣ аст.")

def check_history():
    print("Файл ҳаст." if os.path.isfile(HISTORY_FILE) else "Файл ҳоло сохта нашудааст.")

def file_name():
    print("Файл:", HISTORY_FILE)

def history_size():
    if os.path.isfile(HISTORY_FILE):
        print("Ҳаҷм:", os.path.getsize(HISTORY_FILE), "байт")
    else:
        print("Файл ҳоло сохта нашудааст.")

def add_note():
    note = input("Ёддошт: ")
    save_history("Ёддошт: " + note)
    print("Ёддошт сабт шуд!")

def search_note():
    word = input("Калимаи ёддошт: ")
    results = [x for x in read_history() if "Ёддошт:" in x and word.lower() in x.lower()]
    print("".join(results) if results else "Ёддошт ёфт нашуд.")

def filter_history():
    word = input("Калима барои филтр: ")
    results = [x for x in read_history() if word.lower() in x.lower()]
    print("".join(results) if results else "Сабт нест.")

def backup_history():
    if os.path.isfile(HISTORY_FILE):
        backup = "history_backup.txt"
        with open(HISTORY_FILE, "r", encoding="utf-8") as src:
            content = src.read()
        with open(backup, "w", encoding="utf-8") as dst:
            dst.write(content)
        print("Нусха сохта шуд:", backup)
    else:
        print("Таърих холӣ аст.")

def history_path():
    print("Роҳи файл:", os.path.abspath(HISTORY_FILE))

def security_record():
    save_history("Санҷиши амният")
    print("Сабт шуд!")

def python_record():
    save_history("Омӯзиши Python")
    print("Сабт шуд!")

def network_record():
    save_history("Санҷиши шабака")
    print("Сабт шуд!")

def history_info():
    lines = read_history()
    print("Файл:", HISTORY_FILE)
    print("Шумораи сабтҳо:", len(lines))
    print("Мавҷуд аст:", os.path.isfile(HISTORY_FILE))
