
import socket
import time

def show_menu():
    tools = {
        "1": ("Санҷиши интернет", internet),
        "2": ("Санҷиши DNS", dns),
        "3": ("IP-и домен", domain_ip),
        "4": ("Санҷиши Ping", ping),
        "5": ("Санҷиши порти localhost", local_port),
        "6": ("Санҷиши пайвастшавӣ", connection),
        "7": ("Номи дастгоҳ", hostname),
        "8": ("IP-и дохилии телефон", phone_ip),
        "9": ("Санҷиши сервер", server_check),
        "10": ("Вақти ҷавоби сервер", response_time),
        "11": ("Санҷиши порти 22", lambda: check_port(22)),
        "12": ("Санҷиши порти 80", lambda: check_port(80)),
        "13": ("Санҷиши порти 443", lambda: check_port(443)),
        "14": ("Санҷиши порти 8080", lambda: check_port(8080)),
        "15": ("Маълумоти DNS", dns_info),
        "16": ("Санҷиши номи сайт", domain_check),
        "17": ("Санҷиши интернети TCP", internet),
        "18": ("Санҷиши вақти пайваст", response_time),
        "19": ("Санҷиши localhost", localhost),
        "20": ("Маълумот дар бораи шабака", network_info)
    }

    while True:
        print("\n--- 20 АСБОБИ ШАБАКА ---")
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

def internet():
    try:
        socket.create_connection(("google.com", 80), timeout=5).close()
        print("Интернет фаъол аст!")
    except OSError:
        print("Интернет дастрас нест!")

def dns():
    try:
        print("Google DNS:", socket.gethostbyname("google.com"))
    except OSError:
        print("DNS дастрас нест!")

def domain_ip():
    host = input("Номи домен: ").strip()
    try:
        print("IP:", socket.gethostbyname(host))
    except OSError:
        print("Домен ёфт нашуд!")

def ping():
    response_time()

def local_port():
    try:
        port = int(input("Порти localhost: "))
        check_port(port)
    except ValueError:
        print("Рақам ворид кун!")

def check_port(port):
    if not 1 <= port <= 65535:
        print("Порт бояд аз 1 то 65535 бошад!")
        return
    s = socket.socket()
    s.settimeout(2)
    result = s.connect_ex(("127.0.0.1", port))
    print("Кушода аст" if result == 0 else "Пӯшида аст")
    s.close()

def connection():
    internet()

def hostname():
    print("Номи дастгоҳ:", socket.gethostname())

def phone_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        print("IP:", s.getsockname()[0])
        s.close()
    except OSError:
        print("IP дастрас нест!")

def server_check():
    try:
        socket.create_connection(("google.com", 443), timeout=5).close()
        print("Сервер дастрас аст!")
    except OSError:
        print("Сервер дастрас нест!")

def response_time():
    start = time.time()
    try:
        socket.create_connection(("google.com", 80), timeout=5).close()
        print("Вақти ҷавоб:", round((time.time()-start)*1000), "ms")
    except OSError:
        print("Пайваст нашуд!")

def dns_info():
    dns()

def domain_check():
    domain_ip()

def localhost():
    check_port(80)

def network_info():
    print("Номи дастгоҳ:", socket.gethostname())
    phone_ip()
def run_tool(number):
    tools = {
        "1": internet,
        "2": dns,
        "3": domain_ip,
        "4": ping,
        "5": local_port,
        "6": connection,
        "7": hostname,
        "8": phone_ip,
        "9": server_check,
        "10": response_time,
        "11": lambda: check_port(22),
        "12": lambda: check_port(80),
        "13": lambda: check_port(443),
        "14": lambda: check_port(8080),
        "15": dns_info,
        "16": domain_check,
        "17": internet,
        "18": response_time,
        "19": localhost,
        "20": network_info
    }

    import io
    from contextlib import redirect_stdout

    result = io.StringIO()

    try:
        with redirect_stdout(result):
            tools[str(number)]()
    except Exception as e:
        return "Хато: " + str(e)

    return result.getvalue()
