from pyrogram import filters, Client
import asyncio
from tyger import SUDO_USER
from tyger.modules.help import *
from pyrogram.methods import messages
from .pmguard import get_arg, denied_users
import tyger.database.pmpermitdb as Zaid
from tyger import cmds

@Client.on_message(filters.command("pmguard", ["."]) & filters.me)
async def pmguard(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**on atau off**")
        return
    if arg == "off":
        await Zaid.set_pm(False)
        await message.edit("**PM Guard Dimatikan**")
    if arg == "on":
        await Zaid.set_pm(True)
        await message.edit("**PM Guard diaktifkan**")
@Client.on_message(filters.command("setpmmsg", ["."]) & filters.me)
async def setpmmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**berikan pesan untuk set**")
        return
    if arg == "default":
        await Zaid.set_permit_message(Zaid.PMPERMIT_MESSAGE)
        await message.edit("**pesan Anti PM diset ke default**.")
        return
    await Zaid.set_permit_message(f"`{arg}`")
    await message.edit("**Pesan custom Anti Pm diset**")


add_command_help(
    "antipm",
    [
        [f"{cmds}pmguard [on or off]", " -> Mengaktifkan atau menonaktifkan anti-pm."],
        [f"{cmds}setpmmsg [message or default]", " -> Menetapkan pesan anti-pm khusus."],
        [f"{cmds}setblockmsg [message or default]", "-> Mengatur pesan blokir khusus."],
        [f"{cmds}setlimit [value]", " -> This one sets a max. message limit for unwanted PMs and when they go beyond it, bamm!."],
        [f"{cmds}allow", " -> Mengizinkan pengguna untuk mengirim PM kepada Anda."],
        [f"{cmds}deny", " -> Menolak pengguna untuk mengirim PM kepada Anda."],
    ],
)
