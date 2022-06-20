#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from ELLIOT.main import bot as app
from config import SUDO_USERS
from ELLIOT.Database.active import (
    get_active_chats, get_active_video_chats)



@app.on_message(filters.command("activevoice") & filters.user(SUDO_USERS))
async def activevc(_, message: Message):
    mystic = await message.reply_text(
        "جارٍ تفعيل الدردشات الصوتية .. يُرجى الانتظار"
    )
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "جروب خاص"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("لا توجد محادثات صوتية نشطة")
    else:
        await mystic.edit_text(
            f"**الدردشات الصوتية النشطة:-**\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command("activevideo") & filters.user(SUDO_USERS))
async def activevi_(_, message: Message):
    mystic = await message.reply_text(
        "الحصول على محادثات فيديو نشطة .. يرجى الانتظار"
    )
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "جروب خاص"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("لا توجد محادثات صوتية نشطة")
    else:
        await mystic.edit_text(
            f"**مكالمات الفيديو النشطة:-**\n\n{text}",
            disable_web_page_preview=True,
        )
