from telethon import TelegramClient, events, tl
from src.producer import telegram_listener
from src.models.converter import Converter
import logging

api_id = "16107297"
api_hash = "6b4f331380cf71addeefc6b0947da02a"
private_chat_name = "Holding Premium Signal 2021"
media_folder_path = "E:\PythonProjects\TradingBot\media"
chat_ids = ["hieule151296"]

logger = logging.Logger("main-logger")

client: TelegramClient = TelegramClient('sesion', api_id, api_hash)
client.start()

for dialog in client.iter_dialogs():
    if private_chat_name in dialog.name:
        chat_ids.append(dialog.id)

telegram_listener.run(client, chat_ids)

client.run_until_disconnected()
