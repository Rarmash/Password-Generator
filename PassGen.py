from configparser import ConfigParser
from modules import alphabet,localeCreate
import random
import time
import os
from modules.localeSelect import lang
d = 1
a = 1
rr = 0

config = ConfigParser()
path = "settings.ini"

if os.path.exists('settings.ini') == False:
    localeCreate.localeCreate(path)

while a!=0:
    print(lang['start'],sep='\n')
    n = input()
    if n in ['Начать', 'начать', 'start', 'Start']:
        a=0

while d != 'True':
    print(lang['howmany'])
    x = int(input())

    print(lang['generating'])
    time.sleep(1)
    print('...')
    time.sleep(1)
    print(lang['yourpass'] + " ", end='')
    for _ in range(x):
        l=random.choice(alphabet.word)
        print(l,end='')
    print('')
    time.sleep(2)
    print(lang['newpass'])
    d = input()
    if d in ['Да', 'да', 'Yes', 'yes']:
        d='False'
    else:
        break
print(lang['exit'])
time.sleep(5)