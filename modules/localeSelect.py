from configparser import ConfigParser

config = ConfigParser()

config.read("settings.ini")

language = config.get("LOCALE", "language")
section = language.upper()
config.read("locales/{}.ini".format(language))

lang = {
    'start': config.get(section, "start").encode('cp1251').decode('utf-8'),
    'howmany': config.get(section, "howmany").encode('cp1251').decode('utf-8'),
    'generating': config.get(section, "generating").encode('cp1251').decode('utf-8'),
    'yourpass': config.get(section, "yourpass").encode('cp1251').decode('utf-8'),
    'newpass': config.get(section, "newpass").encode('cp1251').decode('utf-8'),
    'exit': config.get(section, "exit").encode('cp1251').decode('utf-8'),
}