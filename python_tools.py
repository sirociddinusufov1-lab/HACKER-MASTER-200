
def show_menu():
    tools = {
        "1": ("Салом дар Python", hello),
        "2": ("Ҳисоб кардани ҷамъ", add),
        "3": ("Тарҳи ададҳо", subtract),
        "4": ("Зарб", multiply),
        "5": ("Тақсим", divide),
        "6": ("Санҷиши адади ҷуфт", even_odd),
        "7": ("Санҷиши синну сол", age_check),
        "8": ("Ҳисоб кардани квадрат", square),
        "9": ("Ҳисоб кардани куб", cube),
        "10": ("Дарозии матн", text_length),
        "11": ("Ҳарфҳои калон", uppercase),
        "12": ("Ҳарфҳои хурд", lowercase),
        "13": ("Баръакс кардани матн", reverse_text),
        "14": ("Ҳисоб кардани ҳарфҳо", count_letters),
        "15": ("Чоп кардани рақамҳо", count_numbers),
        "16": ("Рӯйхати меваҳо", fruits),
        "17": ("Сохтани номи пурра", full_name),
        "18": ("Санҷиши парол", password_check),
        "19": ("Омӯзиши if", learn_if),
        "20": ("Омӯзиши loop", learn_loop)
    }

    while True:
        print("\n--- 20 АСБОБИ PYTHON ---")
        for key, value in tools.items():
            print(f"[{key}] {value[0]}")
        print("[0] Бозгашт")

        choice = input("Рақам: ").strip()
        if choice == "0":
            break
        elif choice in tools:
            tools[choice][1]()
        else:
            print("Рақами нодуруст!")

def hello():
    print("Hello! Салом!")

def add():
    a = float(input("Адади якум: "))
    b = float(input("Адади дуюм: "))
    print("Ҷавоб:", a + b)

def subtract():
    a = float(input("Адади якум: "))
    b = float(input("Адади дуюм: "))
    print("Ҷавоб:", a - b)

def multiply():
    a = float(input("Адади якум: "))
    b = float(input("Адади дуюм: "))
    print("Ҷавоб:", a * b)

def divide():
    a = float(input("Адади якум: "))
    b = float(input("Адади дуюм: "))
    if b == 0:
        print("Ба сифр тақсим намешавад!")
    else:
        print("Ҷавоб:", a / b)

def even_odd():
    n = int(input("Рақам: "))
    print("Ҷуфт" if n % 2 == 0 else "Тоқ")

def age_check():
    age = int(input("Синну сол: "))
    print("Калонсол" if age >= 18 else "Ноболиғ")

def square():
    n = float(input("Рақам: "))
    print("Квадрат:", n ** 2)

def cube():
    n = float(input("Рақам: "))
    print("Куб:", n ** 3)

def text_length():
    text = input("Матн: ")
    print("Дарозӣ:", len(text))

def uppercase():
    print(input("Матн: ").upper())

def lowercase():
    print(input("Матн: ").lower())

def reverse_text():
    print(input("Матн: ")[::-1])

def count_letters():
    text = input("Матн: ")
    print("Шумораи аломатҳо:", len(text))

def count_numbers():
    for i in range(1, 11):
        print(i)

def fruits():
    items = ["Себ", "Нок", "Ангур", "Банан"]
    for item in items:
        print(item)

def full_name():
    first = input("Ном: ")
    last = input("Насаб: ")
    print("Номи пурра:", first, last)

def password_check():
    password = input("Пароли санҷишӣ: ")
    if len(password) >= 12:
        print("Парол дарозии хуб дорад.")
    else:
        print("Парол кӯтоҳ аст.")
    print("Пароли ҳақиқии худро нанавис!")

def learn_if():
    number = int(input("Рақам: "))
    if number > 0:
        print("Мусбат")
    elif number < 0:
        print("Манфӣ")
    else:
        print("Сифр")

def learn_loop():
    for i in range(1, 6):
        print("Дарси Python:", i)
