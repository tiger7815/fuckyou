from os import environ 

class Config:
    API_ID = environ.get("API_ID", "27862677")
    API_HASH = environ.get("API_HASH", "e343ce2c81b2b6c2c0d6bee58284e3bd")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7200218828:AAGwk6n-Fj2tpJncAepEBbt-WefFUK6OPi0") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5881684718').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
