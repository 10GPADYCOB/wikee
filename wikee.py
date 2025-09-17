import sys
import os
import time

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

ORANGE = '\033[33m'
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
PINK = '\033[95m'
GRAY = '\033[90m'
CYAN = '\033[96m'
RESET = '\033[0m'

def menu():
    print(f"\n{GREEN}―――――――――――――――――――\n МЕНЮ ВЫБОРА ЖАЛОБ\n―――――――――――――――――――{RESET}\n{BLUE}[1]  просто снос\n[2]  порнография\n[3]  незаконные действия\n[4]  информация о программе\n[5]  доп. жалобы\n\n[9]  ранк жалоб\n{RED}[0]  выход{RESET}")

def info():
    clear()
    print(f"{GRAY}――――――――――――――――――――――――\n ИНФОРМАЦИЯ О ПРОГРАММЕ\n――――――――――――――――――――――――{RESET}\n{BLUE}Разработчик: 40_JluTpoB_vodku\nВерсия: BETA 0.2\nНазвание: wikee\nНазначение: помощь в составлении жалоб,снос{RESET}")
    enters()

def rank():
    clear()
    print(f"{GRAY}―――――――――――――――――――\n    РАНГИ ЖАЛОБ\n―――――――――――――――――――\n{RESET}в разработке")
    enters()

def dop():
    clear()
    print(f"{GRAY}―――――――――――――――――――\n    ДОП. ЖАЛОБЫ\n―――――――――――――――――――\n{PINK}[1]  воровство{RESET}")
    enters()

def enters():
    input("Нажмите Enter чтобы вернуться в меню...")

while True:
    user_input = input(f"{CYAN}Введите 1 для запуска команды:{RESET} ")
    if user_input == "1":
        print(f"{GREEN}snoser{RESET}")
        break
    else:
        for _ in range(5):
            print(f"{RED}error. Введите 1{RESET}")

valid = ["1", "2", "3", "4", "5", "9", "0"]

while True:
    clear()
    menu()
    
    choice = input("\nвыберите пункт (1-9): ")
    if choice not in valid:
        input(f"{RED}error. Введите одно из девяти\n{RESET}Нажмите Enter чтобы перезапустить графический интерфейс пользователя...")
        continue

    if choice == "1":
        clear()
        print(f"\n{GREEN}вы выбрали: snos{RESET}\n{BLUE}чтобы просто снести видео > пожаловаться > безопасность несовершеннолетних >\nнанесение вреда несовершеннолетних\n{RESET}Описание жалобы:\n\nданное видео содержит недопустимые моменты,\nэто может быть рассмотрено как нанесение вреда несовершеннолетним\n\n{RED}РЕДКО РАБОТАЕТ !!!{RESET}\n")
        enters()

    elif choice == "2":
        clear()
        print(f"{GREEN}вы выбрали: порнография{RESET}\n{BLUE}пожаловаться > порнография или нагота *выберите причину в зависимости от случая*\n{RESET}Описание жалобы:\n\nна данном видео присутсвует мужчина\женщина которая\nнаводит сексуальную атмосферу\n")
        enters()
        
    elif choice == "3":
        clear()
        print(f"\n{GREEN}вы выбрали: незаконные действия{RESET}\n{BLUE}пожаловаться > угроза личной безопасности\n{RESET}Описание жалобы:\n\nданное видео содержит незаконные действия, такие\nкак *описываете действия которые могут быть\nнезаконными*\n")
        enters()
    
    elif choice == "4":
        info()

    elif choice == "5":
        dop()

    elif choice == "9":
        rank()
        
    elif choice == "0":
        print(f"\n{RED}Выход из программы...{RESET}")
        time.sleep(5)
        exit()
