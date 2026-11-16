
import os
import shutil

def show_menu():
    tools = {
        "1": ("Намоиши файлҳо", list_files),
        "2": ("Папкаи нав", make_folder),
        "3": ("Сохтани файли нав", create_file),
        "4": ("Навиштан ба файл", write_file),
        "5": ("Хондани файл", read_file),
        "6": ("Ҳаҷми файл", file_size),
        "7": ("Санҷиши файл", check_file),
        "8": ("Санҷиши папка", check_folder),
        "9": ("Номи папкаи корӣ", current_folder),
        "10": ("Шумораи файлҳо", count_files),
        "11": ("Нусхаи файл", copy_file),
        "12": ("Номи файлҳоро нишон додан", file_names),
        "13": ("Ҳисоб кардани сатрҳо", count_lines),
        "14": ("Ҳисоб кардани калимаҳо", count_words),
        "15": ("Ҳисоб кардани ҳарфҳо", count_chars),
        "16": ("Ҷустуҷӯи калима", search_word),
        "17": ("Тоза кардани фосилаҳо", clean_text),
        "18": ("Матнро ба ҳарфи калон", upper_text),
        "19": ("Матнро ба ҳарфи хурд", lower_text),
        "20": ("Маълумоти файл", file_info)
    }

    while True:
        print("\n--- 20 АСБОБИ ФАЙЛ ---")
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

def get_name():
    return input("Номи файл: ").strip()

def list_files():
    for name in os.listdir("."):
        print(name)

def make_folder():
    name = input("Номи папка: ").strip()
    if name:
        os.makedirs(name, exist_ok=True)
        print("Папка сохта шуд!")

def create_file():
    name = get_name()
    if name:
        with open(name, "a", encoding="utf-8"):
            pass
        print("Файл сохта шуд!")

def write_file():
    name = get_name()
    text = input("Матнро навис: ")
    with open(name, "a", encoding="utf-8") as f:
        f.write(text + "\n")
    print("Матн сабт шуд!")

def read_file():
    name = get_name()
    with open(name, "r", encoding="utf-8") as f:
        print(f.read())

def file_size():
    name = get_name()
    if os.path.isfile(name):
        print("Ҳаҷм:", os.path.getsize(name), "байт")
    else:
        print("Файл ёфт нашуд!")

def check_file():
    name = get_name()
    print("Файл ҳаст." if os.path.isfile(name) else "Файл нест.")

def check_folder():
    name = input("Номи папка: ").strip()
    print("Папка ҳаст." if os.path.isdir(name) else "Папка нест.")

def current_folder():
    print("Папкаи корӣ:", os.getcwd())

def count_files():
    files = [x for x in os.listdir(".") if os.path.isfile(x)]
    print("Шумораи файлҳо:", len(files))

def copy_file():
    source = get_name()
    destination = input("Номи нусха: ").strip()
    if os.path.isfile(source) and destination:
        shutil.copy2(source, destination)
        print("Нусха сохта шуд!")
    else:
        print("Файл ёфт нашуд!")

def file_names():
    for name in os.listdir("."):
        print("Ном:", name)

def count_lines():
    name = get_name()
    with open(name, "r", encoding="utf-8") as f:
        print("Сатрҳо:", len(f.readlines()))

def count_words():
    name = get_name()
    with open(name, "r", encoding="utf-8") as f:
        print("Калимаҳо:", len(f.read().split()))

def count_chars():
    name = get_name()
    with open(name, "r", encoding="utf-8") as f:
        print("Аломатҳо:", len(f.read()))

def search_word():
    name = get_name()
    word = input("Калимаи ҷустуҷӯ: ")
    with open(name, "r", encoding="utf-8") as f:
        text = f.read()
    print("Ёфт шуд!" if word in text else "Ёфт нашуд!")

def clean_text():
    text = input("Матн: ")
    print("Матни тоза:", " ".join(text.split()))

def upper_text():
    print(input("Матн: ").upper())

def lower_text():
    print(input("Матн: ").lower())

def file_info():
    name = get_name()
    if os.path.isfile(name):
        print("Ном:", os.path.basename(name))
        print("Ҳаҷм:", os.path.getsize(name), "байт")
        print("Роҳи пурра:", os.path.abspath(name))
    else:
        print("Файл ёфт нашуд!")
