from pyrogram import Client, filters 
from database.users_chats_db import db

@Client.on_message(filters.private & filters.command('set_start'))
async def set_start_message(c: Client, m: Message, strings):
    if len(m.text.split()) > 1:
        message = m.text.html.split(None, 1)[1]
    await message.reply_text("Yᴏᴜʀ Sᴛᴀʀᴛ Mᴇssᴀɢᴇ Sᴜᴄᴄᴇssғᴜʟʟʏ ᴀᴅᴅᴇᴅ")
