from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
DEVS = int(1317223502)
from tyger.helper.PyroHelpers import get_ub_chats
from tyger.modules.basic.profile import extract_user, extract_user_and_reason
from tyger.database import gbandb as Zaid
from tyger.database import gmutedb as Gmute
from tyger.modules.help import add_command_help
from tyger import cmds

ok = []

@Client.on_message(filters.command("gban", cmds) & filters.me)
async def gban_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("`Gbanning...`")
    else:
        ex = await message.edit("`Gbanning....`")
    if not user_id:
        return await ex.edit("Saya tidak dapat menemukan pengguna tersebut.")
    if user_id == client.me.id:
        return await ex.edit("**Lu mau gban diri sendiri? Tolol!!**")
    if user_id in DEVS:
        return await ex.edit("**Gak Bisa Di Gban Kontol karena dia Yang Buat Aku 🗿**")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit("`Harap tentukan pengguna yang valid!`")

    if (await Zaid.gban_info(user.id)):
        return await ex.edit(
            f"[user](tg://user?id={user.id}) **pengguna telah di gban**"
        )
    f_chats = await get_ub_chats(client)
    if not f_chats:
        return await ex.edit("**tidak menjadi admin dimanapun, kasian... 🥺**")
    er = 0
    done = 0
    for gokid in f_chats:
        try:
            await client.ban_chat_member(chat_id=gokid, user_id=int(user.id))
            done += 1
        except BaseException:
            er += 1
    await Zaid.gban_user(user.id)
    ok.append(user.id)
    msg = (
        r"**\\#Berhasil Dibanned//**"
        f"\n\n**Nama:** [{user.first_name}](tg://user?id={user.id})"
        f"\n**User ID:** `{user.id}`"
    )
    if reason:
        msg += f"\n**Alasan:** `{reason}`"
    msg += f"\n**Sukses Di:** `{done}` **Chats**"
    await ex.edit(msg)


@Client.on_message(filters.command("ungban", cmds) & filters.me)
async def ungban_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply("`UnGbanning...`")
    else:
        ex = await message.edit("`UnGbanning....`")
    if not user_id:
        return await ex.edit("Saya tidak dapat menemukan pengguna tersebut.")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit("`Harap tentukan pengguna yang valid!`")

    try:
        if not (await Zaid.gban_info(user.id)):
            return await ex.edit("`Pengguna sudah di ungban`")
        ung_chats = await get_ub_chats(client)
        ok.remove(user.id)
        if not ung_chats:
            return await ex.edit("**tidak menjadi admin dimanapun, kasian... 🥺**")
        er = 0
        done = 0
        for good_boi in ung_chats:
            try:
                await client.unban_chat_member(chat_id=good_boi, user_id=user.id)
                done += 1
            except BaseException:
                er += 1
        await Zaid.ungban_user(user.id)
        msg = (
            r"**\\#UnGbanned_User//**"
            f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})"
            f"\n**User ID:** `{user.id}`"
        )
        if reason:
            msg += f"\n**Reason:** `{reason}`"
        msg += f"\n**Affected To:** `{done}` **Chats**"
        await ex.edit(msg)
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return


@Client.on_message(filters.command("listgban", cmds) & filters.me)
async def gbanlist(client: Client, message: Message):
    users = (await Zaid.gban_list())
    ex = await message.edit_text("`mencari...`")
    if not users:
        return await ex.edit("Anak baik, belom gban orang")
    gban_list = "**GBanned Users:**\n"
    count = 0
    for i in users:
        count += 1
        gban_list += f"**{count} -** `{i.sender}`\n"
    return await ex.edit(gban_list)


@Client.on_message(filters.command("gmute", cmds) & filters.me)
async def gmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.edit_text(message, "`mencari...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await ex.edit(f"`Harap tentukan pengguna yang valid!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await ex.edit(f"`Harap tentukan pengguna yang valid!`")
        return
    if user.id == client.me.id:
        return await ex.edit("**Lu mau gmute diri sendiri? Tolol!**")
    if user.id in DEVS:
        return await ex.edit("**Gak Bisa Di Gmute Kontol karena dia Yang Buat Aku 🗿**")
    try:
        replied_user = reply.from_user
        if replied_user.is_self:
            return await ex.edit("`Kan udah di bilang tidak bisa membisukan diri sendiri, Tolol!.`")
    except BaseException:
        pass

    try:
        if (await Gmute.is_gmuted(user.id)):
            return await ex.edit("`User already gmuted`")
        await Gmute.gmute(user.id)
        ok.append(user.id)
        await ex.edit(f"[{user.first_name}](tg://user?id={user.id}) globally gmuted!")
        try:
            common_chats = await client.get_common_chats(user.id)
            for i in common_chats:
                await i.restrict_member(user.id, ChatPermissions())
        except BaseException:
            pass
    
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return


@Client.on_message(filters.command("ungmute", cmds) & filters.me)
async def ungmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.edit_text("`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await ex.edit(f"`Please specify a valid user!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await ex.edit(f"`Please specify a valid user!`")
        return

    try:
        replied_user = reply.from_user
        if replied_user.is_self:
            return await ex.edit("`Calm down anybob, you can't ungmute yourself.`")
    except BaseException:
        pass

    try:
        if not (await Gmute.is_gmuted(user.id)):
            return await ex.edit("`User already ungmuted`")
        await Gmute.ungmute(user.id)
        ok.remove(user.id)
        try:
            common_chats = await client.get_common_chats(user.id)
            for i in common_chats:
                await i.unban_member(user.id)
        except BaseException:
            pass
        await ex.edit(
            f"[{user.first_name}](tg://user?id={user.id}) globally ungmuted!"
        )
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return


@Client.on_message(filters.command("listgmute", cmds) & filters.me)
async def gmutelist(client: Client, message: Message):
    users = (await Gmute.gmute_list())
    ex = await message.edit_text("`Processing...`")
    if not users:
        return await ex.edit("There are no Muted Users yet")
    gmute_list = "**GMuted Users:**\n"
    count = 0
    for i in users:
        count += 1
        gmute_list += f"**{count} -** `{i.sender}`\n"
    return await ex.edit(gmute_list)

if ok:
 @Client.on_message(filters.incoming & filters.group)
 async def globals_check(client: Client, message: Message):
    if not message:
        return
    if not message.from_user:
        return
    user_id = message.from_user.id
    chat_id = message.chat.id
    if not user_id:
        return
    if (await Zaid.gban_info(user_id)):
        try:
            await client.ban_chat_member(chat_id, user_id)
        except BaseException:
            pass

    if (await Gmute.is_gmuted(user_id)):
        try:
            await message.delete()
        except errors.RPCError:
            pass
        try:
            await client.restrict_chat_member(chat_id, user_id, ChatPermissions())
        except BaseException:
            pass

    message.continue_propagation()


add_command_help(
    "globals",
    [
        [f"{cmds}gban <reply/username/userid>", "Lakukan Larangan Global Ke Semua Grup Di Mana Anda Sebagai Admin."],
        [f"{cmds}ungban <reply/username/userid>", "Hapus Larangan Global."],
        [f"{cmds}listgban", "Menampilkan Daftar Larangan Global."],
    ],
)
