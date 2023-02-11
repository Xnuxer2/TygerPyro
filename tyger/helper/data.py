from pyrogram.types import InlineKeyboardButton, WebAppInfo

class Data:

    text_help_menu = (
        "**Menu Inline Tyger-Pyro**\n**Perintah :** ? ! . * , $"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("💫 ʙᴜᴋᴀ 💫", callback_data="reopen")]]
