from telethon import TelegramClient, events
from src.models.signal import Signal

def run(client: TelegramClient, chat_ids: list):
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
            print(signal.__dict__)



