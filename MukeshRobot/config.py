class Config(object):
    LOGGER =True
    API_ID =23080322 
    API_HASH = "b3611c291bf82d917637d61e4a136535"
    TOKEN = "7271288704:AAF3f9OJQ_8GEZL7y3NEoYbjc7TslSeq6lY"  
    OWNER_ID=7011929837
    
    SUPPORT_CHAT = "-1002150515664" 
    START_IMG = ""
    EVENT_LOGS = ()
    MONGO_DB_URI= ""
   
    DATABASE_URL = "postgresql://postgres.adldmnbzdckqwrckabtj:Aaryanary1097@aws-0-ap-south-1.pooler.supabase.com:6543/postgres"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        ""
    )
    TIME_API_KEY = ""

    
    BL_CHATS = [] 
    DRAGONS = []
    DEV_USERS = []  
    DEMONS = [] 
    TIGERS = []  
    WOLVES = [] 

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
