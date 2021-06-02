from easy_password_generator import PassGen
import gettext
from modules import encrypt,decrypt
import time
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
    print (_('Введите "Начать", если готовы к работе:'),sep='\n')
    n = input()
    if n=='Начать' or n=='начать' or n=='start' or n=='Start':
        a=0

decrypt.decrypt(fileaes)
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
encrypt.encrypt(file)

while d != 'True':
    print(_('Сколько символов должен содержать пароль?'))
    x = int(input())
    if rr == 0 or rr == 2:
        if rr == 2:
            print(_('Т.к. у вас бесплатная версия программы, то ожидание вашего пароля будет составлять 15 секунд.'))
        elif rr == 0:
            print(_('Т.к. вы ввели неправильный номер лицензии, то будет запущена бесплатная версия программы. Ожидание вашего пароля будет составлять 15 секунд.'))
        time.sleep(1)
        for i in range(1,16):
            k = 15-i
            print(_('Секунд осталось:'),k)
            time.sleep(1)

    pwo = PassGen(minlen = x, maxlen=x)
    l = pwo.generate()

    print(_('Генерируем пароль...'))
    time.sleep(1)
    print('...')
    time.sleep(1)
    print(_('Ваш пароль: '), l, end='\n')
    time.sleep(2)
    print(_('Желаете ли сгенерировать новый пароль?'))
    d = input()
    if d == 'Да' or d == 'да' or d == 'Yes' or d=='yes':
        d='False'
    else:
        break
print(_('Спасибо за использование данной программы, всего вам доброго. До свидания!'))
time.sleep(5)
