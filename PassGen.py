from easy_password_generator import PassGen
import gettext
from modules import crypt
import time
import os
d = 1
a = 1
rr = 0

file = "license.txt"
fileaes = "license.txt.aes"

print("Enter your language: English or Русский")
lang = input()  
if lang == "Русский" or lang == 'русский' or lang == 'russian' or lang == 'Russian':
    ru = gettext.translation('ru', localedir='locales', languages=['ru'])
    ru.install()
    _ = ru.gettext
if lang == "English" or lang == 'english' or lang == 'Английский' or lang == 'английский':
    en = gettext.translation('en', localedir='locales', languages=['en'])
    en.install()
    _ = en.gettext

while a!=0:
    print (_("Enter 'Start' if you are ready to go:"),sep='\n')
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
    print(_('How many characters should the password contain?'))
    x = int(input())
    if rr == 0 or rr == 2:
        if rr == 2:
            print(_('The license file is missing, so Trial version of the program will be launched. The waiting time for your password will be 15 seconds.'))
        elif rr == 0:
            print(_('The license file is corrupted, so Trial version of the program will be launched. The waiting time for your password will be 15 seconds.'))
        time.sleep(1)
        for i in range(1,16):
            k = 15-i
            print(_('Seconds left:'),k)
            time.sleep(1)

    pwo = PassGen(minlen = x, maxlen=x)
    l = pwo.generate()

    print(_('Generating a password...'))
    time.sleep(1)
    print('...')
    time.sleep(1)
    print(_('Your password:'), l, end='\n')
    time.sleep(2)
    print(_('Would you like to generate a new password?'))
    d = input()
    if d == 'Да' or d == 'да' or d == 'Yes' or d=='yes':
        d='False'
    else:
        break
print(_('Thank you for using this program, and all the best to you. Goodbye!'))
time.sleep(5)
