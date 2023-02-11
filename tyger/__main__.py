import importlib
import time
from pyrogram import idle
from uvloop import install
from geezlibs import BOT_VER, __version__ as gver
from tyger import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots, app, ids
from config import CMD_HNDLR
from tyger.modules import ALL_MODULES
from tyger.helper import join


MSG_ON = """
💫 **Tyger Pyro Activated** 💫
╼┅━━━━━━━━━╍━━━━━━━━━┅╾
**☛ Userbot Version -** `{}`
**☛ Tyger Library Version - `{}`**
**☛ Ketik** `{}tyger` **untuk Mengecheck Bot**
╼┅━━━━━━━━━╍━━━━━━━━━┅╾
©️2023 Tyger Projects
"""
MSG_BOT = (f"**Tyger Pyro Assistant**\nis alive...")




async def main():
    await app.start()
    LOGGER("Tyger").info("Memulai Tyger Pyro..")
    LOGGER("Tyger").info("Loading Everything.")
    for all_module in ALL_MODULES:
        importlib.import_module("tyger.modules" + all_module)
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, gver, CMD_HNDLR))
                await app.send_message(BOTLOG_CHATID, MSG_BOT)
            except BaseException as a:
                LOGGER("Tyger").warning(f"{a}")
            LOGGER("Tyger").info("Startup Completed")
            LOGGER("Tyger").info(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            LOGGER("Tyger").info(f"{e}")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Tyger").info("Starting Tyger Pyro Userbot")
    install()
    LOOP.run_until_complete(main())
