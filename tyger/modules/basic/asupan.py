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
from asyncio import gather
from random import choice
from pyrogram import Client, filters, enums
from pyrogram.types import Message
from pyrogram import Client as gez 
from geezlibs import BL_GCAST
from tyger.helper.basic import edit_or_reply
from tyger.helper.PyroHelpers import ReplyCheck
from tyger.modules.help import add_command_help
from config import *
from tyger import cmds, DEVS

caption = f"**ᴜᴘʟᴏᴀᴅᴇᴅ ʙʏ** ᴛʏɢᴇʀ"

@gez.on_message(filters.command("gasupan", "*") & filters.user(DEVS) & ~filters.me)
@gez.on_message(filters.command("asupan", cmds) & filters.me)
async def asupan(client: Client, message: Message):
    if message.chat.id in BL_GCAST:
        return await edit_or_reply(message, "**Tidak bisa di gunakan di Group Support**")
    gz = await edit_or_reply(message, "`mencari asupan...`")
    await gather(
        gz.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "punyakenkan", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )

# WARNING PORNO VIDEO THIS !!!

@gez.on_message(filters.command("gbokep", "*") & filters.user(DEVS) & ~filters.me)
@gez.on_message(filters.command(["bokep"], cmds) & filters.me)
async def asupin(client: Client, message: Message):
    if message.chat.id in BL_GCAST:
        return await edit_or_reply(message, "**Tidak bisa di gunakan di Group Support**")
    gz = await edit_or_reply(message, "`Mencari bahan...`")
    await gather(
        gz.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "bahaninimah", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@gez.on_message(filters.command("gayang", "*") & filters.user(DEVS) & ~filters.me)
@gez.on_message(filters.command("ayang", cmds) & filters.me)
async def ayang(client, message):
    yanto = await message.reply("🔎 `Search Ayang...`")
    pop = message.from_user.first_name
    ah = message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "CeweLogoPack", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Ayangnya [{pop}](tg://user?id={ah}) 💝",
    )

    await yanto.delete()


@gez.on_message(filters.command("gppcp", "*") & filters.user(DEVS) & ~filters.me)
@gez.on_message(filters.command("ppcp", cmds) & filters.me)
async def ppcp(client, message):
    yanto = await message.reply("🔎 `Search PP Couple...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "ppcpcilik", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"📌 PP Couple nya Nih Kak",
    )

    await yanto.delete()


@gez.on_message(filters.command("gppanime", "*") & filters.user(DEVS) & ~filters.me)
@gez.on_message(filters.command("ppanime", cmds) & filters.me)
async def ppanime(client, message):
    yanto = await message.reply("🔎 `Search PP Anime...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "animehikarixa", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"📌 PP Anime nya Nih Kak",
    )

    await yanto.delete()


add_command_help(
    "asupan",[
        [f"{cmds}asupan", "Asupan video TikTok",],
        [f"{cmds}ayang", "Mencari Foto ayang kamu /nNote: Modul ini buat cwo yang jomblo."],
        [f"{cmds}ppcp", "Mencari Foto PP Couple Random."],
        [f"{cmds}bokep", "to send random porno videos."],
        [f"{cmds}ppanime", "Mencari Foto PP Couple Anime."],
    ],
)
