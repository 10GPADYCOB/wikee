import subprocess
import sys
import os
import time

def clear_screen():
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

def show_menu():
    print(f"\n{GRAY}=== МЕНЮ ВЫБОРА ЖАЛОБ ==={RESET}\n{BLUE}1. просто снос\n2. порнография\n3. незаконные действия\n4. информация о программе\n5. доп. жалобы\n\n9. ранк жалоб\n{RED}0. выход{RESET}")

def show_about():
    clear_screen()
    print(f"{GRAY}=== ИНФОРМАЦИЯ О ПРОГРАММЕ ==={RESET}\n{BLUE}Разработчик: 40_JluTpoB_vodku\nВерсия: BETA 0.2\nНазвание: wikee\nНазначение: помощь в составлении жалоб,снос{RESET}")
    enters()

def show_rank():
    clear_screen()
    print(f"{GRAY}=== РАНГИ ЖАЛОБ ===\n{RESET}в разработке")
    enters()

def show_dop():
    clear_screen()
    print(f"{GRAY}=== ДОП. ЖАЛОБЫ ===\n{PINK}ждите пока я добавлю доп жалобы :){RESET}")
    enters()

def enters():
    input("Нажмите Enter чтобы вернуться в меню...")

while True:
    user_input = input(f"{CYAN}Введите 1 для запуска команды: {RESET}")
    if user_input == "1":
        print(f"{GREEN}snoser{RESET}")
        break
    else:
        for _ in range(5):
            print(f"{RED}error. Введите 1{RESET}")

valid_choices = ["1", "2", "3", "4", "5", "9", "0"]

while True:
    clear_screen()
    show_menu()
    
    choice = input(f"\n{CYAN}выберите пункт (1-9): {RESET}")
    if choice not in valid_choices:

        input(f"{RED}error. Введите одно из девяти\n{RESET}Нажмите Enter чтобы перезапустить графический интерфейс пользователя...")
        continue

    if choice == "1":
        clear_screen()
        print(f"\n{GREEN}вы выбрали: snos{RESET}\n{BLUE}чтобы просто снести видео > пожаловаться > безопасность несовершеннолетних >\nнанесение вреда несовершеннолетних\n{RESET}Описание жалобы:\n\nданное видео содержит недопустимые моменты,\nэто может быть рассмотрено как нанесение вреда несовершеннолетним\n\n{RED}РЕДКО РАБОТАЕТ !!!{RESET}\n")
        enters()

    elif choice == "2":
        clear_screen()
        print(f"{GREEN}вы выбрали: порнография{RESET}\n{BLUE}пожаловаться > порнография или нагота *выберите причину в зависимости от случая*\n{RESET}Описание жалобы:\n\nна данном видео присутсвует мужчина\женщина которая\nнаводит сексуальную атмосферу\n")
        enters()
        
    elif choice == "3":
        clear_screen()
        print(f"\n{GREEN}вы выбрали: незаконные действия{RESET}\n{BLUE}пожаловаться > угроза личной безопасности\n{RESET}Описание жалобы:\n\nданное видео содержит незаконные действия, такие\nкак *описываете действия которые могут быть\nнезаконными*\n")
        enters()
    
    elif choice == "4":
        show_about()

    elif choice == "5":
        show_dop()

    elif choice == "9":
        show_rank()
        
    elif choice == "0":
        print(f"\n{RED}Выход из программы...{RESET}")
        time.sleep(5)
        exit()

