from pyrogram import filters, Client
import asyncio
from tyger import SUDO_USER
from tyger.modules.help import *
from pyrogram.methods import messages
from .pmguard import get_arg, denied_users

import tyger.database.pmpermitdb as Zaid



@Client.on_message(filters.command("pmguard", ["."]) & filters.me)
async def pmguard(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**I only understand on or off**")
        return
    if arg == "off":
        await Zaid.set_pm(False)
        await message.edit("**PM Guard Deactivated**")
    if arg == "on":
        await Zaid.set_pm(True)
        await message.edit("**PM Guard Activated**")
@Client.on_message(filters.command("setpmmsg", ["."]) & filters.me)
async def setpmmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**What message to set**")
        return
    if arg == "default":
        await Zaid.set_permit_message(Zaid.PMPERMIT_MESSAGE)
        await message.edit("**Anti_PM message set to default**.")
        return
    await Zaid.set_permit_message(f"`{arg}`")
    await message.edit("**Custom anti-pm message set**")


add_command_help(
    "antipm",
    [
        [".pmguard [on or off]", " -> Mengaktifkan atau menonaktifkan anti-pm."],
        [".setpmmsg [message or default]", " -> Menetapkan pesan anti-pm khusus."],
        [".setblockmsg [message or default]", "-> Mengatur pesan blokir khusus."],
        [".setlimit [value]", " -> This one sets a max. message limit for unwanted PMs and when they go beyond it, bamm!."],
        [".allow", " -> Mengizinkan pengguna untuk mengirim PM kepada Anda."],
        [".deny", " -> Menolak pengguna untuk mengirim PM kepada Anda."],
    ],
)
