import asyncio

from pyrogram import filters, Client 
from pyrogram.raw import functions
from pyrogram.types import Message


from tyger.modules.help import add_command_help


@Client.on_message(
    filters.command(["screenshot", "ss"], ".") & filters.private & filters.me
)
async def screenshot(bot: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        bot.send(
            functions.messages.SendScreenshotNotification(
                peer=await bot.resolve_peer(message.chat.id),
                reply_to_msg_id=0,
                random_id=bot.rnd_id(),
            )
        ),
    )


add_command_help(
    "screenshot",
    [
        [
            ".screenshot",
            "Mengirim notifikasi dalam obrolan pribadi (bukan rahasia) untuk mengganggu atau menjahili teman Anda.",
        ],
    ],
)
