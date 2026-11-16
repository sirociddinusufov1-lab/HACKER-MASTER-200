
import random
import string
import time
import calendar
from datetime import datetime

def show_menu():
    tools = {
        "1": ("Салом", hello),
        "2": ("Рақами тасодуфӣ", random_number),
        "3": ("Партофтани зар", dice),
        "4": ("Тасодуфан интихоб кардан", random_choice),
        "5": ("Сохтани номи корбар", username),
        "6": ("Сохтани рамзи кӯтоҳ", short_code),
        "7": ("Соати ҳозира", clock),
        "8": ("Санаи имрӯз", today),
        "9": ("Тақвими сол", year_calendar),
        "10": ("Ҳисоб кардани рӯзҳо", days_left),
        "11": ("Бозии тахмини рақам", guessing_game),
        "12": ("Саволу ҷавоб", quiz),
        "13": ("Санҷиши матн", text_test),
        "14": ("Шумораи калимаҳо", word_count),
        "15": ("Баръакс кардани матн", reverse_text),
        "16": ("Интихоби ранги тасодуфӣ", random_color),
        "17": ("Таймери оддӣ", timer),
        "18": ("Сохтани ID", make_id),
        "19": ("Намоиши рӯйхат", show_list),
        "20": ("Маълумоти барнома", app_info)
    }

    while True:
        print("\n--- 20 АСБОБИ ИЛОВАГӢ ---")
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
                print("Маълумоти нодуруст!")
        else:
            print("Рақами нодуруст!")

def hello():
    print("Салом! Ба HACKER MASTER TJ хуш омадӣ!")

def random_number():
    print("Рақам:", random.randint(1, 100))

def dice():
    print("Зар:", random.randint(1, 6))

def random_choice():
    items = input("Чанд интихобро бо вергул навис: ").split(",")
    items = [x.strip() for x in items if x.strip()]
    if items:
        print("Интихоб:", random.choice(items))
    else:
        print("Рӯйхат холӣ аст.")

def username():
    name = input("Ном: ").strip()
    number = random.randint(100, 999)
    print("Номи корбар:", name + str(number))

def short_code():
    chars = string.ascii_uppercase + string.digits
    print("Рамз:", "".join(random.choice(chars) for _ in range(6)))

def clock():
    print("Вақт:", datetime.now().strftime("%H:%M:%S"))

def today():
    print("Сана:", datetime.now().strftime("%Y-%m-%d"))

def year_calendar():
    year = int(input("Сол: "))
    print(calendar.calendar(year))

def days_left():
    year = int(input("Сол: "))
    month = int(input("Моҳ: "))
    day = int(input("Рӯз: "))
    target = datetime(year, month, day)
    difference = (target - datetime.now()).days
    print("Фарқи рӯзҳо:", difference)

def guessing_game():
    secret = random.randint(1, 10)
    print("Ман рақами аз 1 то 10 интихоб кардам.")
    for _ in range(3):
        guess = int(input("Тахмин кун: "))
        if guess == secret:
            print("Офарин! Дуруст!")
            return
        print("Боз кӯшиш кун!")
    print("Рақами дуруст:", secret)

def quiz():
    answer = input("Python барои чӣ истифода мешавад? ")
    if answer.strip():
        print("Ташаккур барои ҷавоб!")
    else:
        print("Ҷавоб ворид кун.")

def text_test():
    text = input("Матн: ")
    print("Матни шумо:", text)
    print("Аломатҳо:", len(text))

def word_count():
    text = input("Матн: ")
    print("Калимаҳо:", len(text.split()))

def reverse_text():
    text = input("Матн: ")
    print("Баръакс:", text[::-1])

def random_color():
    color = "#" + "".join(random.choice("0123456789ABCDEF") for _ in range(6))
    print("Ранги тасодуфӣ:", color)

def timer():
    seconds = int(input("Сония: "))
    if not 1 <= seconds <= 60:
        print("Аз 1 то 60 сония интихоб кун.")
        return
    print("Таймер оғоз шуд!")
    time.sleep(seconds)
    print("Вақт тамом шуд!")

def make_id():
    print("ID:", "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)))

def show_list():
    items = ["Python", "Termux", "Network", "Security", "Technology"]
    for number, item in enumerate(items, 1):
        print(number, item)

def app_info():
    print("HACKER MASTER TJ")
    print("VERSION 20.0")
    print("200 асбоб дар 10 модул")
    print("Омӯзиш ва амнияти қонунӣ")
