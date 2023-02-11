
import time
import traceback
from sys import version as pyver 
from datetime import datetime
from pyrogram import Client
from pyrogram import __version__ as pyrover
from pyrogram.enums import ParseMode
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)

from tyger import CMD_HELP, StartTime, app
from tyger.helper.data import Data
from tyger.helper.inline import inline_wrapper, paginate_help

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


async def alive_function(message: Message, answers):
    uptime = await get_readable_time((time.time() - StartTime))
    msg = f"""
<b> — Hey Baby, I am alive.</b>

<b> 💫 User :</b> {message.from_user.mention}
<b> 💫 Plugins :</b> <code>{len(CMD_HELP)} Modules</code>
<b> 💫 Python Version :</b> <code>{pyver.split()[0]}</code>
<b> 💫 Pyrogram Version :</b> <code>{pyrover}</code>
<b> 💫 Bot Uptime :</b> <code>{uptime}</code>

<b> — Bot version: 2.0</b>
"""
    answers.append(
        InlineQueryResultArticle(
            title="Alive",
            description="Check Bot's Stats",
            thumb_url="https://telegra.ph/file/15fc3bc9963fb6cbbcc37.png",
            input_message_content=InputTextMessageContent(
                msg, parse_mode=ParseMode.HTML, disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("──「 ʜᴇʟᴘ 」──", callback_data="helper")]]
            ),
        )
    )
    return answers


async def help_function(answers):
    bttn = paginate_help(0, CMD_HELP, "helpme")
    answers.append(
        InlineQueryResultArticle(
            title="Help Article!",
            description="Check Command List & Help",
            thumb_url="https://telegra.ph/file/15fc3bc9963fb6cbbcc37.png",
            input_message_content=InputTextMessageContent(
                Data.text_help_menu.format(len(CMD_HELP))
            ),
            reply_markup=InlineKeyboardMarkup(bttn),
        )
    )
    return answers

async def ping_function(message: Message, answers):
    start = datetime.now()
    uptime = await get_readable_time((time.time() - StartTime))
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    msg = (
        f"╭✠╼━━━━━━━━━━━━━━━\n"
        f"│ 💫 𝗧𝘆𝗴𝗲𝗿𝗣𝘆𝗿𝗼-𝗕𝗼𝘁 💫\n"
        f"├✠╼━━━━━━━━━━━━━━━\n"
        f"│★ Pɪɴɢᴇʀ    : </b> <code>{duration}ms</code>\n"
        f"│★ Uᴘᴛɪᴍᴇ    : </b> <code>{uptime}</code>"
        f"╰✠╼━━━━━━━━━━━━━━━━\n"
        f"©️ Tyger Projects"
    )
    answers.append(
        InlineQueryResultArticle(
            title="ping",
            description="Check Bot's Stats",
            thumb_url="https://telegra.ph/file/15fc3bc9963fb6cbbcc37.png",
            input_message_content=InputTextMessageContent(
                msg, parse_mode=ParseMode.HTML, disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url="t.me/TygerSupport")]]
            ),
        )
    )
    return answers


@app.on_inline_query()
@inline_wrapper
async def inline_query_handler(client: Client, query):
    try:
        text = query.query.strip().lower()
        string_given = query.query.lower()
        answers = []
        if text.strip() == "":
            return
        elif text.split()[0] == "alive":
            answerss = await alive_function(query, answers)
            await client.answer_inline_query(query.id, results=answerss, cache_time=10)
        elif string_given.startswith("helper"):
            answers = await help_function(answers)
            await client.answer_inline_query(query.id, results=answers, cache_time=0)
        elif string_given.startswith("ping"):
            answers = await ping_function(query, answers)
            await client.answer_inline_query(query.id, results=answers, cache_time=0)
    except Exception as e:
        e = traceback.format_exc()
        print(e, "InLine")
