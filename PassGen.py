import gettext
import alphabet
import time
import random
d = 1
a = 1
rr = 0

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
print(_('Введите номер лицензии, если вы приобретали программу. В противном случае, введите 000000.'))
y = input()

if (int(y[0]) + int(y[1]) + int(y[2])) == 0 and (int(y[3]) + int(y[4]) + int(y[5])) == 0:
    rr = 2
elif (int(y[0]) + int(y[1]) + int(y[2])) == 17 and (int(y[3]) + int(y[4]) + int(y[5])) == 9:
    rr = 1
else:
    rr = 0

while d != 'True':
    print(_('Сколько символов должен содержать пароль?'))
    x = int(input())
    if rr == 0 or rr == 2:
        if rr == 2:
            print(_('Т.к. у вас бесплатная версия программы, то ожидание вашего пароля будет составлять 15 секунд.'))
        elif rr == 0:
            print(_('Т.к. вы ввели неправильный номер лицензии, то будет запущена бесплатная версия программыю. Ожидание вашего пароля будет составлять 15 секунд.'))
        time.sleep(1)
        for i in range(1,16):
            k = 15-i
            print(_('Секунд осталось:'),k)
            time.sleep(1)
    print(_('Генерируем пароль...'))
    time.sleep(1)
    print('...')
    time.sleep(1)
    print(_('Ваш пароль: '),end='')
    for i in range(x):
        l=random.choice(alphabet.word)
        print(l,end='')
    print('')
    time.sleep(2)
    print(_('Желаете ли сгенерировать новый пароль?'))
    d = input()
    if d == 'Да' or d == 'да' or d == 'Yes' or d=='yes':
        d='False'
    else:
        break
print(_('Спасибо за использование данной программы, всего вам доброго. До свидания!'))
time.sleep(5)
