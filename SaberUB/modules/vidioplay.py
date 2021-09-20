import os
import asyncio
from pytgcalls import GroupCallFactory
from pyrogram import filters, Client, idle
from pyrogram.types import Message
from config import API_ID, API_HASH, SESSION
from SaberUB import app, CMD_HELP
from config import PREFIX

app = Client(SESSION, API_ID, API_HASH)
group_call_factory = GroupCallFactory(app, GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM)
VIDEO_CALL = {}

CMD_HELP.update(
    {
        "Misc": """
『 **Misc** 』
  `v` -> Reply To Video.
  `stop` -> stop vidio
"""
    }
)

@app.on_message(filters.command(["v"], PREFIX) & filters.me
async def stopvide(_, message: Message):
    replied = m.reply_to_message
    if not replied:
        await m.reply("❌ **Please Reply To Video**")
    elif replied.video or replied.document:
        msg = await m.reply("📥 **Start Downloading...**")
        chat_id = m.chat.id
        try:
            video = await client.download_media(m.reply_to_message)
            await msg.edit("🔁 **Processing**")
            os.system(f'ffmpeg -i "{video}" -vn -f s16le -ac 2 -ar 48000 -acodec pcm_s16le -filter:a "atempo=0.81" vid-{chat_id}.raw -y')
            print()
        except Exception as e:
            await msg.edit(f"**🚫 Error** - `{e}`")
        await asyncio.sleep(5)
        try:
            group_call = group_call_factory.get_file_group_call(f'vid-{chat_id}.raw')
            await group_call.start(chat_id)
            await group_call.set_video_capture(video)
            VIDEO_CALL[chat_id] = group_call
            await msg.edit("**🎥 Starting Video Steram!**")
            print()
        except Exception as e:
            await msg.edit(f"**Error** -- `{e}`")
            return os.system("rm -rf downloads")
    else:
        await m.reply("❌ **Please Reply To Video**")
        return os.system("rm -rf downloads")
                
@app.on_message(filters.command(["stop"], PREFIX) & filters.me
async def stream(_, message: Message):
    chat_id = m.chat.id
    try:
        await VIDEO_CALL[chat_id].stop()
        await m.reply("**⏹️ Stopped Streaming!**")
    except Exception as e:
        await m.reply(f"**🚫 Error** - `{e}`")
