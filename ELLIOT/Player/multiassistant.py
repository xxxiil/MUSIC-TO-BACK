#Taken From @TeamYukki
#Don't kang Without Credits @TheUpdatesChannel

import random

from pyrogram import filters
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InlineQueryResultArticle,
                            InlineQueryResultPhoto, InputTextMessageContent,
                            Message)

from ELLIOT.main import bot as app
from config import SUDO_USERS as SUDOERS
from ELLIOT.Database.clientdb import get_assistant, save_assistant
from ELLIOT.Client.assistant import get_assistant_details
from ELLIOT.main import random_assistant



ass_num_list = ["1", "2", "3", "4", "5"]


@app.on_message(filters.command("changeassistant") & filters.user(SUDOERS))
async def assis_change(_, message: Message):
    usage = f"**الاستخدام: **/changeassistant [ASS_NO]  اختر منهم\n{' | '.join(ass_num_list)}"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    num = message.text.split(None, 1)[1].strip()
    if num not in ass_num_list:
        return await message.reply_text(usage)
    ass_num = int(message.text.strip().split()[1])
    _assistant = await get_assistant(message.chat.id, "assistant")
    if not _assistant:
        return await message.reply_text(
            "لم يتم العثور على مساعد محفوظ مسبقًا. \ n \ n يمكنك تعيين عبر المساعد /setassistant"
        )
    else:
        ass = _assistant["saveassistant"]
    assis = {
        "saveassistant": ass_num,
    }
    await save_assistant(message.chat.id, "assistant", assis)
    await message.reply_text(
        f"**تم تغيير حساب المساعد **  تم تغيير حساب المساعد من {ass} إلى رقم المساعد **{ass_num}**"
    )


ass_num_list2 = ["1", "2", "3", "4", "5","Random"]


@app.on_message(filters.command("setassistant") & filters.user(SUDOERS))
async def assis_change(_, message: Message):
    usage = f"**الاستخدام: **  / setassistant [ASS_NO or Random] اختر منهم\n{' | '.join(ass_num_list2)}\n\nUse 'Random' to set random Assistant"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    query = message.text.split(None, 1)[1].strip()
    if query not in ass_num_list2:
        return await message.reply_text(usage)
    if str(query) == "Random":
        ran_ass = random.choice(random_assistant)
    else:
        ran_ass = int(message.text.strip().split()[1])
    _assistant = await get_assistant(message.chat.id, "assistant")
    if not _assistant:
        await message.reply_text(
            f"**__تم تخصيص مساعد بوت الموسيقى __ ** \ n \ n رقم المساعد ** {ran_ass}**"
        )
        assis = {
            "saveassistant": ran_ass,
        }
        await save_assistant(message.chat.id, "assistant", assis)
    else:
        ass = _assistant["saveassistant"]
        return await message.reply_text(
            f"تم العثور على رقم المساعد المحفوظ مسبقًا {ass}. \ n \ n يمكنك تغيير المساعد عبر / changeassistant"
        )


@app.on_message(filters.command("checkassistant") & filters.group)
async def check_ass(_, message: Message):
    _assistant = await get_assistant(message.chat.id, "assistant")
    if not _assistant:
        return await message.reply_text(
            "No Pre-Saved Assistant Found.\n\nYou can set Assistant Via /play"
        )
    else:
        ass = _assistant["saveassistant"]
        return await message.reply_text(
            f"تم العثور على المساعد المحفوظ مسبقًا \ n \ n رقم المساعد {ass} "
        )
