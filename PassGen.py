import alphabet
import time
import random
d = 1
a = 1
while a!=0:
    print('Введите "Начать", если готовы к работе:',sep='\n')
    n = input()
    if n=='Начать' or n=='начать':
        a=0
print('Введите номер лицензии, если вы приобретали программу. В противном случае, введите 0:')
y = int(input())
while d != 'True':
    print('Сколько символов должен содержать пароль?')
    x = int(input())
    if y == 0:
        print('Т.к. у вас бесплатная версия программы, то ожидание вашего пароля будет составлять 15 секунд.')
        time.sleep(1)
        for i in range(1,16):
            k = 15-i
            print('Осталось',k,'секунд.')
            time.sleep(1)
    print('Генерируем пароль...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('Ваш пароль: ',end='')
    for i in range(x):
        l=random.choice(alphabet.word)
        print(l,end='')
    print('')
    time.sleep(2)
    print('Желаете ли сгенерировать новый пароль?')
    d = input()
    if d == 'Да' or d == 'да':
        d='False'
    elif d == 'Нет' or d == 'нет':
        d='True'
print('Спасибо за использование данной программы, всего вам доброго. До свидания!')
time.sleep(5)
