from easy_password_generator import PassGen
from configparser import ConfigParser
from modules import crypt,localeCreate
import time
import os
d = 1
a = 1
rr = 0

config = ConfigParser()
path = "settings.ini"

if os.path.exists('settings.ini') == False:
    localeCreate.localeCreate(path)

config.read("settings.ini")
language = config.get("LOCALE", "language")
section = language.upper()
config.read("locales/{}.ini".format(language))

start = config.get(section, "start")
howmany = config.get(section, "howmany")
missing = config.get(section, "missing")
corrupt = config.get(section, "corrupt")
secleft = config.get(section, "secleft")
generating = config.get(section, "generating")
yourpass = config.get(section, "yourpass")
newpass = config.get(section, "newpass")
exit = config.get(section, "exit")

file = "license.txt"
fileaes = "license.txt.aes"

while a!=0:
    print (start.encode('cp1251').decode('utf-8'),sep='\n')
    n = input()
    if n=='Начать' or n=='начать' or n=='start' or n=='Start':
        a=0

if os.path.exists('lisense.txt.aes') == True:
    crypt.decrypt()
    with open('license.txt','r') as file123:
        ll = file123.readline()
    ll_int = [int(x) for x in ll]
    ll = sum(ll_int)
    if ll == 26:
        rr = 1
    elif ll == 0:
        rr = 2
    else:
        rr = 0
    crypt.encrypt()
else:
    rr = 2

while d != 'True':
    print(howmany.encode('cp1251').decode('utf-8'))
    x = int(input())
    if rr == 0 or rr == 2:
        if rr == 2:
            print(missing.encode('cp1251').decode('utf-8'))
        elif rr == 0:
            print(corrupt.encode('cp1251').decode('utf-8'))
        time.sleep(1)
        for i in range(1,16):
            k = 15-i
            print(secleft.encode('cp1251').decode('utf-8'),k)
            time.sleep(1)

    pwo = PassGen(minlen = x, maxlen=x)
    l = pwo.generate()

    print(generating.encode('cp1251').decode('utf-8'))
    time.sleep(1)
    print('...')
    time.sleep(1)
    print(yourpass.encode('cp1251').decode('utf-8'), l, end='\n')
    time.sleep(2)
    print(newpass.encode('cp1251').decode('utf-8'))
    d = input()
    if d == 'Да' or d == 'да' or d == 'Yes' or d=='yes':
        d='False'
    else:
        break
print(exit.encode('cp1251').decode('utf-8'))
time.sleep(5)