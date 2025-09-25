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
PURPLE = '\033[35m'
YELLO = '\033[93m'

def menu():
    print(f"\n{GREEN}―――――――――――――――――――\n МЕНЮ ВЫБОРА ЖАЛОБ\n―――――――――――――――――――{RESET}\n{BLUE}[1]  просто снос\n[2]  порнография\n[3]  незаконные действия\n[4]  информация о программе\n[77]  доп. жалобы\n\n[99]  ранк жалоб\n[123]  обновить wikee\n{RED}[0]  выход{RESET}")

def info():
    clear()
    print(f"{GRAY}――――――――――――――――――――――――\n ИНФОРМАЦИЯ О ПРОГРАММЕ\n――――――――――――――――――――――――{RESET}\n{BLUE}Разработчик: 40_JluTpoB_vodku\nВерсия: BETA 0.2\nНазвание: wikee\nНазначение: помощь в составлении жалоб,снос\nИзменения: добавлен выбор еще 1 жалобы, добавлен логотоип{RESET}")
    enters()

def rank():
    clear()
    print(f"{GRAY}―――――――――――――――――――\n    РАНГИ ЖАЛОБ\n―――――――――――――――――――\n{RESET}в разработке")
    enters()

def dop():
    clear()
    print(f"{GRAY}―――――――――――――――――――\n    ДОП. ЖАЛОБЫ\n―――――――――――――――――――\n{PINK}[5]  воровство контента\n[0]  назад{RESET}")
    
    s_choice = input(f"\n{CYAN}выберите пункт: {RESET}")
    
    if s_choice == "5":
        clear()
        print(f"{GREEN}вы выбрали: воровство контента{RESET}\n{BLUE}пожаловаться > прочее\n\n{RED}Внимание, воровство: 2 типа:\n1. тип: справа есть не убранные репосты, лайки и т.д.\n2. тип: есть авторский знак likee в видео{RESET}")
        
        typ = input(f"\n{CYAN}Выберите тип (1/2):{RESET}")
        if typ == "1" or typ == "2":
            input("\n\nразработка, бро")
        else:
            input("\nНеверный выбор!")
    
    elif s_choice == "0":
        return
              

def enters():
    input("Нажмите Enter чтобы вернуться в меню...")

def logo():
    art = [
    f"{PURPLE}$$       $$",
    "$#       #$",
    " #$     $#",
    " $#     #$",
    "  #$   #$",
    "    $#$",
    f"{PURPLE}     $ {BLUE}O{RED} D{YELLO} K{ORANGE} A"
    ]
    for line in art:
        print(line)
    
while True:
    logo()
    user_input = input(f"{CYAN}Введите 1 для запуска команды: {RESET}")
    if user_input == "1":
        print(f"{GREEN}snoser{RESET}")
        break
    else:
        for _ in range(5):
            print(f"{RED}error. Введите 1{RESET}")

valid = ["1", "2", "3", "4", "99", "77", "0", "5", "123"]

while True:
    clear()
    menu()

    choice = input(f"\n{CYAN}выберите пункт (1-9): {RESET}")
    if choice not in valid:
        input(f"{RED}error. Введите одно из девяти\n{RESET}Нажмите Enter чтобы перезапустить графический интерфейс пользователя...")
        continue

    if choice == "1":
        clear()
        print(f"\n{GREEN}вы выбрали: snos{RESET}\n{BLUE}чтобы просто снести видео > пожаловаться > безопасность несовершеннолетних >\nнанесение вреда несовершеннолетних\n{RESET}Описание жалобы:\n\nданное видео содержит недопустимые моменты, это может быть рассмотрено как нанесение вреда несовершеннолетним\n\n{RED}РЕДКО РАБОТАЕТ !!!{RESET}\n")
        enters()

    elif choice == "2":
        clear()
        print(f"{GREEN}вы выбрали: порнография{RESET}\n{BLUE}пожаловаться > порнография или нагота *выберите причину в зависимости от случая*\n{RESET}Описание жалобы:\n\nна данном видео присутсвует мужчина\женщина которая наводит сексуальную атмосферу\n(можно считать за просто снос)\n")
        enters()
        
    elif choice == "3":
        clear()
        print(f"\n{GREEN}вы выбрали: незаконные действия{RESET}\n{BLUE}пожаловаться > угроза личной безопасности\n{RESET}Описание жалобы:\n\nданное видео содержит незаконные действия, такие как *описываете действия которые могут быть незаконными*\n")
        enters()
    
    elif choice == "4":
        info()

    elif choice == "77":
        dop()

    elif choice == "99":
        rank()
        
    elif choice == "0":
        print(f"\n{RED}Выход из программы...{RESET}")
        time.sleep(5)
        exit()
    elif choice == "123":
        if input("обновить? y/n:\n") == 'y':
            os.system("rm -rf wikee && git clone https://github.com/10GPADYCOB/wikee.git && cd wikee && python wikee.py")
            exit()
