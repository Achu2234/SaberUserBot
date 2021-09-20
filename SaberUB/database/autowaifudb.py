from . import cli

harem_cheat = cli["Saber"]["AUTOWAIFU"]


async def add_chat(chat_id):
    await harem_cheat.insert_one({"chat_id": chat_id})


async def rm_chat(chat_id):
    await harem_cheat.delete_one({"chat_id": chat_id})


async def get_all_harem_cheat_chats():
    return [kek async for kek in harem_cheat.find({})]


async def is_chat_in_db(chat_id):
    k = await harem_cheat.find_one({"chat_id": chat_id})
    return bool(k)
