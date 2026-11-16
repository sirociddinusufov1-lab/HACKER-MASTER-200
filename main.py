
import network_tools
import security_tools
import python_tools
import phone_tools
import password_tools
import calculator_tools
import file_tools
import history_tools
import system_tools
import extra_tools

print("================================")
print("      HACKER MASTER TJ")
print("         VERSION 20.0")
print("       200 IMPOSSIBILITIES")
print("================================")

modules = [
    ("Шабака ва интернет", network_tools),
    ("Амнияти киберӣ", security_tools),
    ("Омӯзиши Python", python_tools),
    ("Асбобҳои телефон", phone_tools),
    ("Парол ва рамзгузорӣ", password_tools),
    ("Ҳисобкунакҳо", calculator_tools),
    ("Файлҳо ва матн", file_tools),
    ("Таърихи санҷишҳо", history_tools),
    ("Маълумоти система", system_tools),
    ("Асбобҳои иловагӣ", extra_tools)
]

while True:
    print("\n========== МЕНЮ ==========")

    for i, (name, module) in enumerate(modules, 1):
        print(f"[{i}] {name}")

    print("[0] Баромадан")

    choice = input("\nРақамро интихоб кун: ")

    if choice == "0":
        print("То боздид!")
        break

    if choice.isdigit() and 1 <= int(choice) <= len(modules):
        name, module = modules[int(choice) - 1]
        print(f"\n--- {name} ---")
        module.show_menu()
    else:
        print("Рақами нодуруст!")
