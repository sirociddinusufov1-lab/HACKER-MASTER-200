
def show_menu():
    tools = {
        "1": ("Маслиҳатҳои амниятӣ", tips),
        "2": ("Қоидаҳои пароли қавӣ", password_rules),
        "3": ("Амнияти Wi-Fi", wifi_tips),
        "4": ("Амнияти телефон", phone_tips),
        "5": ("Муҳофизати маълумот", data_tips),
        "6": ("Муҳофизати ҳисоб", account_tips),
        "7": ("Фишинг чист?", phishing),
        "8": ("Вирус чист?", virus_info),
        "9": ("Firewall чист?", firewall),
        "10": ("HTTPS чист?", https_info),
        "11": ("Навсозии система", updates),
        "12": ("Нусхаи эҳтиётӣ", backup),
        "13": ("Муҳофизати Bluetooth", bluetooth),
        "14": ("Муҳофизати Wi-Fi-и ҷамъиятӣ", public_wifi),
        "15": ("Иҷозатҳои барномаҳо", permissions),
        "16": ("Муҳофизати файлҳо", file_security),
        "17": ("Дуздии маълумот", data_theft),
        "18": ("Аутентификатсияи дуқадамӣ", two_factor),
        "19": ("Амнияти браузер", browser_security),
        "20": ("Санҷиши одатҳои амниятӣ", checklist)
    }

    while True:
        print("\n--- 20 АСБОБИ АМНИЯТ ---")
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

def tips():
    print("Пароли қавӣ ва навсозии мунтазам истифода бар.")

def password_rules():
    print("Парол бояд дароз, гуногун ва барои ҳар ҳисоб алоҳида бошад.")

def wifi_tips():
    print("WPA2 ё WPA3 истифода бар. WPS-ро хомӯш кун.")

def phone_tips():
    print("Қулфи экран ва навсозии Android-ро фаъол кун.")

def data_tips():
    print("Маълумоти шахсиро бо одамони ношинос нафирист.")

def account_tips():
    print("Барои ҳисобҳо паролҳои гуногун истифода бар.")

def phishing():
    print("Фишинг — фиреб барои гирифтани парол ё маълумоти шахсӣ.")

def virus_info():
    print("Вирус — барномаи зараровар мебошад.")

def firewall():
    print("Firewall — воситаи назорати пайвастҳои шабакавӣ.")

def https_info():
    print("HTTPS маълумотро ҳангоми интиқол рамзгузорӣ мекунад.")

def updates():
    print("Android ва барномаҳоро мунтазам навсозӣ кун.")

def backup():
    print("Нусхаи эҳтиётии файлҳои муҳимро нигоҳ дор.")

def bluetooth():
    print("Bluetooth-ро вақте истифода намебарӣ, хомӯш кун.")

def public_wifi():
    print("Дар Wi-Fi-и ҷамъиятӣ маълумоти ҳассос ворид накун.")

def permissions():
    print("Ба барномаҳо танҳо иҷозатҳои заруриро деҳ.")

def file_security():
    print("Файлҳои ношиносро накушо.")

def data_theft():
    print("Маълумоти ҳассосро дар сайтҳои шубҳанок ворид накун.")

def two_factor():
    print("2FA — тасдиқи иловагӣ барои ворид шудан ба ҳисоб.")

def browser_security():
    print("Браузерро навсозӣ кун ва сайтҳои шубҳанокро накушо.")

def checklist():
    print("""
--- РӮЙХАТИ АМНИЯТ ---
1. Пароли қавӣ дорӣ?
2. Қулфи экран фаъол аст?
3. Android нав аст?
4. 2FA фаъол аст?
5. Нусхаи эҳтиётӣ дорӣ?
""")

def run_tool(number):
    tools = {
        1: tips,
        2: password_rules,
        3: wifi_tips,
        4: phone_tips,
        5: data_tips,
        6: account_tips,
        7: phishing,
        8: virus_info,
        9: firewall,
        10: https_info,
        11: updates,
        12: backup,
        13: bluetooth,
        14: public_wifi,
        15: permissions,
        16: file_security,
        17: data_theft,
        18: two_factor,
        19: browser_security,
        20: checklist
    }

    import io
    from contextlib import redirect_stdout

    if int(number) not in tools:
        return "Асбоб ёфт нашуд!"

    result = io.StringIO()

    with redirect_stdout(result):
        tools[int(number)]()

    return result.getvalue()
