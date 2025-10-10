import sys
import os
import time

def clear():
    print('\033c', end='')

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
    print(f"\n{GREEN}―――――――――――――――――――\n МЕНЮ ВЫБОРА ЖАЛОБ\n―――――――――――――――――――{RESET}\n{BLUE}[1]  просто снос\n[2]  порнография\n[3]  незаконные действия\n[4]  информация о программе\n[5]  доп. жалобы\n\n[6]  ранк жалоб\n[7]  обновить wikee\n{RED}[0]  выход{RESET}")

def info():
    clear()
    print(f"{GRAY}――――――――――――――――――――――――\n ИНФОРМАЦИЯ О ПРОГРАММЕ\n――――――――――――――――――――――――{RESET}\n{BLUE}Разработчик: 40_JluTpoB_vodku\nВерсия: BETA 0.4\nНазвание: wikee\nНазначение: помощь в составлении жалоб,снос\nПоследние изменения: добавлен выбор еще 1 жалобы, добавлен логотоип, фикс с ui, фикс с автообновлением{RESET}")
    enters()

def rank():
    clear()
    print(f"{GRAY}―――――――――――――――――――\n    РАНГИ ЖАЛОБ\n―――――――――――――――――――\n{RESET}в разработке")
    enters()

def dop():
    while True:
        clear()
        print(f"{GRAY}―――――――――――――――――――\n    ДОП. ЖАЛОБЫ\n―――――――――――――――――――\n{PINK}[1]  воровство контента\n[0]  назад{RESET}")
        
        s_choice = input(f"\n{CYAN}выберите пункт: {RESET}")
        
        if s_choice == "1":
            while True:
                clear()
                print(f"{GREEN}вы выбрали: воровство контента{RESET}\n{BLUE}пожаловаться > прочее\n\n{RED}Внимание, воровство: 2 типа:\n1. тип: справа есть не убранные репосты, лайки и т.д.\n2. тип: есть авторский знак likee в видео{RESET}")
                
                typ = input(f"\n{CYAN}Выберите тип (1/2) или 0 чтобы вернуться: {RESET}")
                
                if typ == "1":
                    print(f"{GREEN}вы выбрали: 1 тип{RESET}\n{BLUE}пожаловаться > прочее\n{RESET}Описание жалобы:\n\nвидео своровано у другого автора, потому что справа есть просмотр лайков, комментариев, репостов, и так далее\n")
                    input("Нажмите Enter чтобы продолжить...")
                elif typ == "2":
                    print(f"{GREEN}вы выбрали: 2 тип{RESET}\n{BLUE}пожаловаться > прочее\n{RESET}Описание жалобы:\n\nвидео своровано у другого автора, доказать можно тем, что на видео есть знак likee который появляется при скачивании видео\n")
                    input("Нажмите Enter чтобы продолжить...")
                elif typ == "0":
                    break
                else:
                    input("неправильный выбор! Нажмите Enter...")
        
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

valid = ["1", "2", "3", "4", "5", "6", "0", "7"]

while True:
    clear()
    menu()

    choice = input(f"\n{CYAN}выберите пункт (1-7): {RESET}")
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

    elif choice == "5":
        dop()

    elif choice == "6":
        rank()
        
    elif choice == "0":
        print(f"\nЧтобы выйти из папки, введите: cd\n{RED}Выход из программы...{RESET}")
        time.sleep(1)
        exit()
    elif choice == "7":
     if input("обновить? y/n:\n").lower() == 'y':
        try:
            import subprocess
            
            script_dir = os.path.dirname(os.path.abspath(__file__))
            os.chdir(script_dir)
            
            result = subprocess.run(
                ['git', 'pull', 'origin', 'main'],
                capture_output=True,
                text=True,
                check=True
            )
            
            print(f"{GREEN}Обновлено успешно:{RESET}")
            print(result.stdout)
            
            if input("Перезапустить сейчас? y/n: ").lower() == 'y':
                print(f"{BLUE}Перезапуск...{RESET}")
                os.execv(sys.executable, [sys.executable] + sys.argv)
            else:
                print(f"{YELLO}Перезапусти вручную, ленивая жопа{RESET}")
                enters()
                
        except subprocess.CalledProcessError as e:
            print(f"{RED}Ошибка при обновлении:{RESET}")
            print(f"STDOUT: {e.stdout}")
            print(f"STDERR: {e.stderr}")
            enters()
            
        except Exception as e:
            print(f"{RED}всё сломал:{RESET} {str(e)}")
            enters()
