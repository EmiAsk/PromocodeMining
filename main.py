import os

from telethon import TelegramClient

from constants import API_ID, API_HASH, SESSIONS_PATH
from listeners import register_all_handlers


def main():
    client = TelegramClient(os.path.join(SESSIONS_PATH, 'TelegramClient', 'new_session'), api_id=API_ID,
                            api_hash=API_HASH)
    client.start()
    register_all_handlers(client)
  
    client.run_until_disconnected()


if __name__ == '__main__':
    main()
