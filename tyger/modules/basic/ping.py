# if you can read this, this meant you use code from Geez | Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Geez and Ram doesn't care about credit
# at least we are know as well
# who Geez and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Geez | Ram Team
import time
import random
import speedtest
import asyncio
import functools
from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime
from tyger.helper.PyroHelpers import SpeedConvert
from tyger import StartTime, SUDO_USER
from tyger import app, cmds, DEVS
from tyger.modules.bot.inline import get_readable_time
from tyger.modules.help import add_command_help

class WWW:
    SpeedTest = (
        "Speedtest started at `{start}`\n"
        "Ping ➠ `{ping}` ms\n"
        "Download ➠ `{download}`\n"
        "Upload ➠ `{upload}`\n"
        "ISP ➠ __{isp}__"
    )

    NearestDC = "Country: `{}`\n" "Nearest Datacenter: `{}`\n" "This Datacenter: `{}`"

@Client.on_message(
    filters.command(["speedtest"], cmds) & (filters.me | filters.user(SUDO_USER))
)
async def speed_test(client: Client, message: Message):
    new_msg = await message.reply_text("`Running speed test . . .`")
    try:
       await message.delete()
    except:
       pass
    spd = speedtest.Speedtest()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await new_msg.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )

kopi = [
    "**Hadir Bang** 😁",
    "**Mmuaahh** 😉",
    "**Hadir dong** 😁",
    "**Hadir ganteng** 🥵",
    "**Hadir bro** 😎",
    "**Hadir kak maap telat** 🥺",
]

@Client.on_message(filters.command("absen", ["*"]) & filters.user(DEVS))
async def absen(client: Client, message: Message):
    await message.reply_text(random.choice(kopi))


@Client.on_message(filters.command("gping", "*") & filters.user(DEVS))
async def cpingme(client: Client, message: Message):
    """Ping the assistant"""
    mulai = time.time()
    gez = await message.reply_text("...")
    akhir = time.time()
    await gez.edit_text(f"**🏓 Pong!**\n`{round((akhir - mulai) * 1000)}ms`")


@Client.on_message(
    filters.command("cping", cmds) & (filters.me)
)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await message.reply_text("**Pinging.**")
    end = datetime.now()
    await asyncio.sleep(1)
    try:
       await message.delete()
    except:
       pass
    duration = (end - start).microseconds / 1000
    await xx.edit("**Pinging..**")
    await xx.edit("**Pinging...**")
    await xx.edit("**Pinging....**")
    await asyncio.sleep(1)
    await xx.edit(
        f"**𝐓𝐲𝐠𝐞𝐫 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 🏓**\n"
        f"**⊶⊶⊶⊶⊶⊶⊶⊶**\n"
        f"**🤖 Pɪɴɢᴇʀ »** "
        f" `%sms` \n "
        f"**🤖 Aᴋᴛɪꜰ »** "
        f" `{uptime}` \n " % (duration)
        f"**⊶⊶⊶⊶⊶⊶⊶⊶**\n"
    )
    
@Client.on_message(
    filters.command("ping", cmds) & (filters.me)
)
async def module_ping(client: Client, message: Message):
    cmd = message.command
    help_arg = ""
    bot_username = (await app.get_me()).username
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif not message.reply_to_message and len(cmd) == 1:
        try:
            nice = await client.get_inline_bot_results(bot=bot_username, query="ping")
            await asyncio.gather(
                message.delete(),
                client.send_inline_bot_result(
                    message.chat.id, nice.query_id, nice.results[0].id
                ),
            )
        except BaseException as e:
            print(f"{e}")

@Client.on_message(
    filters.command(["tping"], cmds) & (filters.me | filters.user(SUDO_USER))
)
async def ppingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await message.reply_text("**0% □□□□□**")
    try:
       await message.delete()
    except:
       pass
    await xx.edit("**20% ■□□□□**")
    await xx.edit("**40% ■■□□□**")
    await xx.edit("**60% ■■■□□**")
    await xx.edit("**80% ■■■■□**")
    await xx.edit("**100% ■■■■■**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
        f"**𝗧𝘆𝗴𝗲𝗿𝗣𝘆𝗿𝗼 💫**\n"
        f"**╼┅━━━━━━━╍━━━━━━━┅╾**\n"
        f"** ⇨  Sɪɢɴᴀʟ :** "
        f"`%sms` \n"
        f"** ⇨  Aᴋᴛɪꜰ  :** "
        f"`{uptime}` \n"
        f"** ⇨  Oᴡɴᴇʀ  :** {client.me.mention}" % (duration)
        f"**╼┅━━━━━━━╍━━━━━━━┅╾**\n"
    )


add_command_help(
    "ping",
    [
        [f"{cmds}ping", "Check bot alive or not."],
        [f"{cmds}tping", "Check bot alive or not."],
    ],
)
add_command_help(
    "alive",
    [
        [f"{cmds}alive", "Check bot alive or not."],
        [f"{cmds}tyger", "Check bot alive or not."],
    ],
)
