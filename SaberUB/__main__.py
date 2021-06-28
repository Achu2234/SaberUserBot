# Copyright (C) 2021 By Achu biju
#
# This file is part of < https://github.com/okay-retard/ZectUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Achu2234/SaberUserBot/blob/main/LICENSE >
#
# All rights reserved.

from pyrogram import idle, Client, filters
from config import PREFIX
from SaberUB import app, LOGGER
import logging
from SaberUB.modules import *

app.start()
me = app.get_me()
print(f"Saber UserBot started for Anime Lover {me.id}. Type {PREFIX}help in any telegram chat.")
idle()
