import time
import random
from pyrogram import Client, filters, enums
from Script import script
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto

CMD = ["/", "."]

ADD_ME = ["https://telegra.ph/file/45991424ebfe111f195e4.jpg",
          "https://telegra.ph/file/8f8cf8d70d38e91a0f4be.jpg",
          "https://telegra.ph/file/3f8ad73dbc9fcf8ae23e7.jpg",
          "https://telegra.ph/file/11cb83b62098072282b30.jpg",
]

@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(client, message):
    buttons = [[
            InlineKeyboardButton('FIʟᴛᴇʀs', callback_data='filters'),
            InlineKeyboardButton('Fɪʟᴇ Sᴛᴏʀᴇ', callback_data='store_file')
        ], [
            InlineKeyboardButton('Cᴏɴɴᴇᴄᴛɪᴏɴ', callback_data='coct'),
            InlineKeyboardButton('Exᴛʀᴀ Mᴏᴅs', callback_data='extra')
        ], [
            InlineKeyboardButton('Hᴏᴍᴇ', callback_data='start'),
            InlineKeyboardButton('Sᴛᴀᴛᴜs', callback_data='stats')
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await client.send_message(
        chat_id=message.chat.id,
        text=script.HELP_TXT,
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=message.id
    )

@Client.on_message(filters.command(["rules"]) & filters.private, group=1)
async def help(query, message):
        buttons = [[
                    InlineKeyboardButton('𝚁𝚄𝙻𝙴𝚂', callback_data="rule"),
                  ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.edit_message_media(
            message.chat.id, 
            message.id, 
            random.choice(ADD_ME)
        )
        await query.message.edit_text(
            text=script.RULES_TXT.format(query.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
