import alphabet
from locales import ru,en,az
import time
import random
d = 1
a = 1

print("Enter your language: English or Русский or Azerbaijanian")
lang = input()

if lang == "Русский" or lang == 'русский' or lang == 'russian' or lang == 'Russian':
    start = ru.start
    license = ru.license
    howmuch = ru.howmuch
    trial = ru.trial
    generating = ru.generating
    secondsleft = ru.secondsleft
    yourpass = ru.yourpass
    again = ru.again
    youraredead = ru.youaredead
if lang == "English" or lang == 'english' or lang == 'Английский' or lang == 'английский':
    start = en.start
    license = en.license
    howmuch = en.howmuch
    trial = en.trial
    generating = en.generating
    secondsleft = en.secondsleft
    yourpass = en.yourpass
    again = en.again
    youraredead = en.youaredead
if lang == "Azerbaijanian" or lang == 'azerbaijanian':
    start = az.start
    license = az.license
    howmuch = az.howmuch
    trial = az.trial
    generating = az.generating
    secondsleft = az.secondsleft
    yourpass = az.yourpass
    again = az.again
    youraredead = az.youaredead

while a!=0:
    print(start,sep='\n')
    n = input()
    if n=='Начать' or n=='начать' or n=='start' or n=='Start':
        a=0
print(license)
y = int(input())
while d != 'True':
    print(howmuch)
    x = int(input())
    if y == 0:
        print(trial)
        time.sleep(1)
        for i in range(1,16):
            k = 15-i
            print(secondsleft,k)
            time.sleep(1)
    print(generating)
    time.sleep(1)
    print('...')
    time.sleep(1)
    print(yourpass,end='')
    for i in range(x):
        l=random.choice(alphabet.word)
        print(l,end='')
    print('')
    time.sleep(2)
    print(again)
    d = input()
    if d == 'Да' or d == 'да' or d == 'Yes' or d=='yes':
        d='False'
    else:
        break
print(youraredead)
time.sleep(5)
