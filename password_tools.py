
import secrets
import string
import hashlib
import base64

def show_menu():
    tools = {
        "1": ("Сохтани пароли қавӣ", strong_password),
        "2": ("Санҷиши дарозии парол", password_length),
        "3": ("Санҷиши қувваи парол", password_strength),
        "4": ("Сохтани PIN", make_pin),
        "5": ("Сохтани пароли рақамӣ", number_password),
        "6": ("Сохтани пароли ҳарфӣ", letter_password),
        "7": ("Сохтани пароли омехта", mixed_password),
        "8": ("SHA256-и матн", sha256_text),
        "9": ("SHA1-и матн", sha1_text),
        "10": ("MD5-и матн", md5_text),
        "11": ("Рамзгузории Base64", encode_text),
        "12": ("Кушодани Base64", decode_text),
        "13": ("Санҷиши такрори парол", repeat_check),
        "14": ("Генератори рамз", random_code),
        "15": ("Сохтани калиди тасодуфӣ", random_key),
        "16": ("Санҷиши ҳарфҳои калон", uppercase_check),
        "17": ("Санҷиши ҳарфҳои хурд", lowercase_check),
        "18": ("Санҷиши рақам дар парол", digit_check),
        "19": ("Санҷиши аломати махсус", symbol_check),
        "20": ("Маслиҳати амнияти парол", password_advice)
    }

    while True:
        print("\n--- 20 АСБОБИ ПАРОЛ ---")
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

def get_length():
    try:
        n = int(input("Дарозӣ (4 то 64): "))
        if 4 <= n <= 64:
            return n
        print("Рақам бояд аз 4 то 64 бошад.")
    except ValueError:
        print("Рақами дуруст ворид кун.")
    return None

def strong_password():
    n = get_length()
    if n:
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        print("Пароли нав:", ''.join(secrets.choice(chars) for _ in range(n)))

def password_length():
    p = input("Пароли санҷишӣ: ")
    print("Дарозӣ:", len(p))
    print("Пароли ҳақиқиро нанавис!")

def password_strength():
    p = input("Пароли санҷишӣ: ")
    score = sum([
        len(p) >= 12,
        any(c.islower() for c in p),
        any(c.isupper() for c in p),
        any(c.isdigit() for c in p),
        any(not c.isalnum() for c in p)
    ])
    print("Қувва:", score, "аз 5")
    print("Пароли ҳақиқиро нанавис!")

def make_pin():
    n = get_length()
    if n:
        print("PIN:", ''.join(secrets.choice(string.digits) for _ in range(n)))

def number_password():
    n = get_length()
    if n:
        print("Рамз:", ''.join(secrets.choice(string.digits) for _ in range(n)))

def letter_password():
    n = get_length()
    if n:
        chars = string.ascii_letters
        print("Рамз:", ''.join(secrets.choice(chars) for _ in range(n)))

def mixed_password():
    strong_password()

def sha256_text():
    text = input("Матн: ")
    print(hashlib.sha256(text.encode()).hexdigest())

def sha1_text():
    text = input("Матн: ")
    print(hashlib.sha1(text.encode()).hexdigest())

def md5_text():
    text = input("Матн: ")
    print(hashlib.md5(text.encode()).hexdigest())

def encode_text():
    text = input("Матн: ")
    print(base64.b64encode(text.encode()).decode())

def decode_text():
    text = input("Base64: ")
    try:
        print(base64.b64decode(text, validate=True).decode())
    except Exception:
        print("Матн нодуруст аст.")

def repeat_check():
    a = input("Пароли якуми санҷишӣ: ")
    b = input("Пароли дуюми санҷишӣ: ")
    print("Якхелаанд." if a == b else "Фарқ доранд.")

def random_code():
    print("Рамзи тасодуфӣ:", secrets.token_hex(4))

def random_key():
    print("Калиди тасодуфӣ:", secrets.token_urlsafe(24))

def uppercase_check():
    p = input("Матни санҷишӣ: ")
    print("Ҳарфи калон дорад." if any(c.isupper() for c in p) else "Ҳарфи калон надорад.")

def lowercase_check():
    p = input("Матни санҷишӣ: ")
    print("Ҳарфи хурд дорад." if any(c.islower() for c in p) else "Ҳарфи хурд надорад.")

def digit_check():
    p = input("Матни санҷишӣ: ")
    print("Рақам дорад." if any(c.isdigit() for c in p) else "Рақам надорад.")

def symbol_check():
    p = input("Матни санҷишӣ: ")
    print("Аломати махсус дорад." if any(not c.isalnum() for c in p) else "Аломати махсус надорад.")

def password_advice():
    print("Пароли дароз ва нодир истифода бар.")
    print("Барои ҳар ҳисоб пароли алоҳида соз.")
    print("2FA-ро фаъол кун.")
    print("Паролро ба касе нафирист.")
