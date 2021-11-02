from telethon import TelegramClient, events, utils
from src.models.signal import Signal
from logging import Logger
from datetime import timedelta, datetime

def run(client: TelegramClient, chat_ids: list, logger: Logger):
    @client.on(events.NewMessage(chats=chat_ids))
    async def handler(event: events.NewMessage.Event):
        # getting image, saved for later
        # use resulted "path" to load image instead of getting its name directly
        # if event.message.media:
        #     path = await client.download_media(event.message, media_folder_path)
        #     print(f"save to path {path}")


        text:str = event.message.message
        signal = Signal.text_to_signal(text.lower())
        if signal:
            chat_name = utils.get_display_name(await event.get_chat())
            print(f"chat name: {chat_name}| {(datetime.now() + timedelta(hours=7))}| {signal.__dict__}")