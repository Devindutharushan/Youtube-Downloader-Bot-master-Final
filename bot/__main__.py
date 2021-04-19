from pyrogram import Client
import config

DOWNLOAD_LOCATION = "./Downloads"
BOT_TOKEN = 1559670734:AAHvyr47ekvjayMcwd8D4-AjGrweK4MAQeY

APP_ID = 3163214
API_HASH = beca6bc2790326f46aff39b70cb33f9a


plugins = dict(
    root="plugins",
)

Client(
    "YouTubeDlBot",
    bot_token=BOT_TOKEN,
    api_id=APP_ID,
    api_hash=API_HASH,
    plugins=plugins,
    workers=100
).run()
