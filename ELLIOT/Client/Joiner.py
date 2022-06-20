import random
from typing import Dict, List, Union

from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
ASSIDS = []
from ELLIOT.main import bot as app
from ELLIOT.Client.assistant import get_assistant_details
from ELLIOT.main import random_assistant
from ELLIOT.Database.clientdb import getassistant, save_assistant


def AssistantAdd(mystic):
    async def wrapper(_, message):
        _assistant = await getassistant(message.chat.id, "assistant")
        if not _assistant:
            ran_ass = random.choice(random_assistant)
            assis = {
                "saveassistant": ran_ass,
            }
            await save_assistant(message.chat.id, "assistant", assis)
        else:
            ran_ass = _assistant["saveassistant"]
        if ran_ass not in random_assistant:
            ran_ass = random.choice(random_assistant)
            assis = {
                "saveassistant": ran_ass,
            }
            await save_assistant(message.chat.id, "assistant", assis)
        ASS_ID, ASS_NAME, ASS_USERNAME, ASS_ACC = await get_assistant_details(
            ran_ass
        )
        try:
            b = await app.get_chat_member(message.chat.id, ASS_ID)
            if b.status == "kicked":
                return await message.reply_text(
                    f"تم حظر الحساب المساعد[{ASS_ID}] قم برفع الحظر.\nحتي تستطيع استخدام البوت\n\nاسم المستخدم: @{ASS_USERNAME}"
                )
            if b.status == "banned":
                return await message.reply_text(
                    f"تم حظر الحساب المساعد[{ASS_ID}] قم برفع الحظر.\nحتي تستطيع استخدام البوت\n\nاسم المستخدم: @{ASS_USERNAME}"
                )
        except UserNotParticipant:
            if message.chat.username:
                try:
                    await ASS_ACC.join_chat(message.chat.username)
                except UserAlreadyParticipant:
                    pass
                except Exception as e:
                    await message.reply_text(
                        f"__Assistant فشل في الانضمام إلى __ \ n \ n ****: {e}"
                    )
                    return
            else:
                try:
                    invitelink = await app.export_chat_invite_link(
                        message.chat.id
                    )
                    if invitelink.startswith("https://t.me/+"):
                        invitelink = invitelink.replace(
                            "https://t.me/+", "https://t.me/joinchat/"
                        )
                    await ASS_ACC.join_chat(invitelink)
                    await message.reply(
                        f"{ASS_NAME} انضم بنجاح",
                    )
                except UserAlreadyParticipant:
                    pass
                except Exception as e:
                    await message.reply_text(
                        f"__Assistant فشل في الانضمام إلى __ \ n \ n ****: {e}"
                    )
                    return
        return await mystic(_, message)

    return wrapper
