import re

from telethon import events
from telethon.sync import TelegramClient
from telethon.tl.types import UpdateNewMessage

from constants import CHANNELS
from auto import do_all_actions


async def new_msg(event: UpdateNewMessage):
    text = event.message.message
    
    for el in ['trix', 'up-x', 'play2x', 'taker']:
        if el in text.lower():
            return

    pattern = re.compile('(?:(?<=\s)|(?<=^))([a-zA-Z0-9]{8})(?:(?=\s)|(?=$))')
    occurrences = re.findall(pattern, text)
    not_promo_codes = ['dragonmoney', 'trix', 'up-x', 'taker']
    for promo in occurrences:
        if promo.lower() not in not_promo_codes:
            do_all_actions(promo_code=promo)


def register_all_handlers(client: TelegramClient):
    for channel in CHANNELS:
        client.add_event_handler(new_msg, events.NewMessage(chats=channel))
