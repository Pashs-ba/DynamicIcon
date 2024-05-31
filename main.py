import datetime
import asyncio

from telethon import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.types import InputPhoto

from utils import load_config, get_current_image, log


async def main(main_client: TelegramClient, config: dict):
    try:
        async with main_client:
            while True:
                p = (await client.get_profile_photos('me'))[0]
                await main_client(DeletePhotosRequest(
                    id=[InputPhoto(
                        id=p.id,
                        access_hash=p.access_hash,
                        file_reference=p.file_reference
                    )]))
                await main_client(UploadProfilePhotoRequest(
                    file=await main_client.upload_file(get_current_image(config))
                ))
                log(config, f"Change icon to {get_current_image(config)}")
                await asyncio.sleep(60 * 60)
    except Exception as e:
        log(config, f"ERROR: {e}")
        exit(1)


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
