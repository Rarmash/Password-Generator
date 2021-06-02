from configparser import ConfigParser
import os

config = ConfigParser()

path = "settings.ini"

def localeCreate(path):
    config.add_section("LOCALE")
    print("Enter your language: English or Русский or Deutsch",sep='\n')
    qq = input()
    if qq == "Русский" or qq == 'русский' or qq == 'russian' or qq == 'Russian':
        config.set("LOCALE", "language", "ru")
    if qq == "English" or qq == 'english' or qq == 'Английский' or qq == 'английский':
        config.set("LOCALE", "language", "en")
    if qq == "Deutsch" or qq == 'deutsch' or qq == 'German' or qq == 'german':
        config.set("LOCALE", "language", "de")
    
    with open(path, "w+") as config_file:
        path = "settings.ini"
        config.write(config_file)
