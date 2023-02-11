import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "TygerPyro"])

async def join(client):
    try:
        await client.join_chat("thelordofsatan")
        await client.join_chat("TygerSupport")
    except BaseException:
        pass
