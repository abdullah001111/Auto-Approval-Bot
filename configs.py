# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "27382214"))
    API_HASH = getenv("API_HASH", "6a3913eb3f026ab02e7ac1c420df2ad0")
    BOT_TOKEN = getenv("BOT_TOKEN", "6504735804:AAFJQ-qNl7q7nyo1z190ZIhsS2D4_ECUakk")
    FSUB = getenv("FSUB", "Mayhem_Bots")
    CHID = int(getenv("CHID", "-1002029165345"))
    SUDO = list(map(int, getenv("SUDO", "5984303934").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://AABOT:AABOT@cluster0.z6rppzx.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
