
import math

def show_menu():
    tools = {
        "1": ("Ҷамъ", add),
        "2": ("Тарҳ", subtract),
        "3": ("Зарб", multiply),
        "4": ("Тақсим", divide),
        "5": ("Фоиз", percent),
        "6": ("Квадрат", square),
        "7": ("Куб", cube),
        "8": ("Решаи квадратӣ", root),
        "9": ("Қувваи адад", power),
        "10": ("Қимати мутлақ", absolute),
        "11": ("Миёнаи ададҳо", average),
        "12": ("Калонтарин адад", maximum),
        "13": ("Хурдтарин адад", minimum),
        "14": ("Факториал", factorial),
        "15": ("Синус", sine),
        "16": ("Косинус", cosine),
        "17": ("Тангенс", tangent),
        "18": ("Дарозии доира", circumference),
        "19": ("Масоҳати доира", circle_area),
        "20": ("Табдили дараҷа", radians_degrees)
    }

    while True:
        print("\n--- 20 ҲИСОБКУНАК ---")
        for key, value in tools.items():
            print(f"[{key}] {value[0]}")
        print("[0] Бозгашт")

        choice = input("Рақам: ").strip()
        if choice == "0":
            break
        elif choice in tools:
            try:
                tools[choice][1]()
            except ValueError:
                print("Адади дуруст ворид кун!")
            except Exception as e:
                print("Хато:", e)
        else:
            print("Рақами нодуруст!")

def two_numbers():
    a = float(input("Адади якум: "))
    b = float(input("Адади дуюм: "))
    return a, b

def add():
    a, b = two_numbers()
    print("Ҷавоб:", a + b)

def subtract():
    a, b = two_numbers()
    print("Ҷавоб:", a - b)

def multiply():
    a, b = two_numbers()
    print("Ҷавоб:", a * b)

def divide():
    a, b = two_numbers()
    if b == 0:
        print("Ба сифр тақсим намешавад!")
    else:
        print("Ҷавоб:", a / b)

def percent():
    a, b = two_numbers()
    print("Фоиз:", a * b / 100)

def square():
    a = float(input("Адад: "))
    print("Квадрат:", a ** 2)

def cube():
    a = float(input("Адад: "))
    print("Куб:", a ** 3)

def root():
    a = float(input("Адад: "))
    if a < 0:
        print("Решаи квадратии адади манфӣ ҳисоб намешавад.")
    else:
        print("Реша:", math.sqrt(a))

def power():
    a, b = two_numbers()
    print("Ҷавоб:", a ** b)

def absolute():
    a = float(input("Адад: "))
    print("Қимати мутлақ:", abs(a))

def get_numbers():
    values = input("Ададҳоро бо фосила навис: ")
    return [float(x) for x in values.split()]

def average():
    nums = get_numbers()
    if nums:
        print("Миёна:", sum(nums) / len(nums))
    else:
        print("Адад ворид нашуд.")

def maximum():
    nums = get_numbers()
    if nums:
        print("Калонтарин:", max(nums))
    else:
        print("Адад ворид нашуд.")

def minimum():
    nums = get_numbers()
    if nums:
        print("Хурдтарин:", min(nums))
    else:
        print("Адад ворид нашуд.")

def factorial():
    a = int(input("Адади бутун аз 0 то 100: "))
    if 0 <= a <= 100:
        print("Факториал:", math.factorial(a))
    else:
        print("Адад бояд аз 0 то 100 бошад.")

def sine():
    a = float(input("Дараҷа: "))
    print("Sin:", math.sin(math.radians(a)))

def cosine():
    a = float(input("Дараҷа: "))
    print("Cos:", math.cos(math.radians(a)))

def tangent():
    a = float(input("Дараҷа: "))
    if abs(math.cos(math.radians(a))) < 1e-10:
        print("Тангенс муайян нест.")
    else:
        print("Tan:", math.tan(math.radians(a)))

def circumference():
    r = float(input("Радиус: "))
    if r < 0:
        print("Радиус манфӣ намешавад.")
    else:
        print("Дарозии доира:", 2 * math.pi * r)

def circle_area():
    r = float(input("Радиус: "))
    if r < 0:
        print("Радиус манфӣ намешавад.")
    else:
        print("Масоҳат:", math.pi * r ** 2)

def radians_degrees():
    a = float(input("Дараҷа: "))
    print("Радиан:", math.radians(a))
    print("Дараҷа:", math.degrees(a))
