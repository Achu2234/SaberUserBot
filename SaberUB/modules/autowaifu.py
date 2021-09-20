import time
from pyrogram import filters
import os
from bs4 import BeautifulSoup as bs
import requests
from SaberUB import app, CMD_HELP
from SaberUB.database.autowaifudb import add_chat, is_chat_in_db, rm_chat
from config import PREFIX, BOT_LIST

CMD_HELP.update(
    {
        "AutoProtecc": """
『 **Auto Harem** 』
  `addharem` -> Add a chat to your harem autoprotecc list.
  `rmharem` -> Remove a chat from your harem autoprotecc list.
"""
    }
)


@app.on_message(filters.command("addharem", PREFIX) & filters.me)
async def add_harem_hc(client, message):
    pablo = await message.edit("`Processing..`")
    if await is_chat_in_db(int(message.chat.id)):
        await pablo.edit("`This Chat is Already In My DB`")
        return
    await add_chat(int(message.chat.id))
    await pablo.edit("`Successfully Added Chat To Harem Watch.`")


@app.on_message(filters.command("rmharem", PREFIX) & filters.me)
async def remove_nsfw(client, message):
    pablo = await message.edit("`Processing..`")
    if not await is_chat_in_db(int(message.chat.id)):
        await pablo.edit("`This Chat is Not in dB.`")
        return
    await rm_chat(int(message.chat.id))
    await pablo.edit("`Successfully Removed Chat From Harem Watch.`")


async def is_harem_enabled(f, client, message):
    if await is_chat_in_db(int(message.chat.id)):
        return
    else:
        return

is_harem_enabled = filters.create(func=is_harem_enabled, name="is_harem_enabled")

@app.on.message(filters.user(BOT_LIST) & ~filters.edited & is_harem_enabled & filters.group)
async def autowaifu(client, message):
    if message.photo:

#        if message.user.id in BOT_LIST:
            dl = await app.download_media(message, "resources/")
            file = {"encoded_image": (dl, open(dl, "rb"))}
            grs = requests.post(
                "https://www.google.com/searchbyimage/upload",
                files=file,
                allow_redirects=False,
            )
            loc = grs.headers.get("location")
            response = requests.get(
                loc,
                headers={
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
                },
            )
            xx = bs(response.text, "html.parser")
            div = xx.find_all("div", {"class": "r5a77d"})[0]
            alls = div.find("a")
            text = alls.text
            send = await app.send_message(message.chat.id, f"/protecc {text}")
            await sleep(5)
            await send.delete()
            os.remove(dl)
