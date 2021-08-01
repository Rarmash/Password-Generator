from configparser import ConfigParser

config = ConfigParser()

path = "settings.ini"

def localeCreate(path):
    config.add_section("LOCALE")
    print("Enter your language: English or Русский or Deutsch or Українська or Azərbaycan",sep='\n')
    qq = input()
    if qq in ["Русский", 'русский', 'russian', 'Russian']:
        config.set("LOCALE", "language", "ru")
    if qq in ["English", 'english', 'Английский', 'английский']:
        config.set("LOCALE", "language", "en")
    if qq in ["Deutsch", 'deutsch', 'German', 'german']:
        config.set("LOCALE", "language", "de")
    if qq in ["Українська", 'українська', 'украинский', 'Украинский']:
        config.set("LOCALE", "language", "ua")
    if qq in ["Azərbaycan", 'azərbaycan', 'Azerbaijanian', 'azerbaijanian']:
        config.set("LOCALE", "language", "az")

    with open(path, "w+") as config_file:
        path = "settings.ini"
        config.write(config_file)
