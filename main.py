import os

import yaml
from telethon import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest
import asyncio


def load_config() -> dict:
    return yaml.safe_load(open(f"{os.path.dirname(__file__)}/config.yaml"))


async def main(main_client: TelegramClient, config: dict):
    async with main_client:
        await main_client(UploadProfilePhotoRequest(
            file=await main_client.upload_file('images/0.png')
        ))


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    config = load_config()
    client = TelegramClient('test_session',
                            config["base"]["api_id"],
                            config["base"]["api_hash"])
    client.start(phone=config["auth"]["phone"],
                 password=config["auth"]["password"])
    loop.run_until_complete(main(client, config))
