import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message
from tyger.helper.aiohttp_helper import AioHttp
from tyger.modules.help import add_command_help
from tyger import cmds

@Client.on_message(filters.command(["unsplash", "pic"], cmds) & filters.me)
async def unsplash_pictures(bot: Client, message: Message):
    cmd = message.command

    if len(cmd) > 1 and isinstance(cmd[1], str):
        keyword = cmd[1]

        if len(cmd) > 2 and int(cmd[2]) < 10:
            await message.edit("```Getting Pictures```")
            count = int(cmd[2])
            images = []
            while len(images) is not count:
                img = await AioHttp().get_url(
                    f"https://source.unsplash.com/1600x900/?{keyword}"
                )
                if img not in images:
                    images.append(img)

            for img in images:
                await bot.send_photo(message.chat.id, str(img))

            await message.delete()
            return
        else:
            await message.edit("```Getting Picture```")
            img = await AioHttp().get_url(
                f"https://source.unsplash.com/1600x900/?{keyword}"
            )
            await asyncio.gather(
                message.delete(), 
                bot.send_photo(message.chat.id, str(img))
            )



add_command_help(
    "unsplash",
    [
        [f"{cmds}unsplash __or__ {cmds}pic", "Send random pic of keyword first argument."],
    ],
)
