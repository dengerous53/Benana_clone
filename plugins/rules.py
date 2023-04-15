import time
import random
from pyrogram import Client, filters, enums
from Script import script
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto

CMD = ["/", "."]


@Client.on_message(filters.command(["rules"]))
async def help(client, message):
        buttons = [[
                    InlineKeyboardButton('𝚁𝚄𝙻𝙴𝚂', callback_data="rule"),
                  ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.send_photo(
           photo=random.choice(ADD_ME),
           caption=script.RULES_TXT,
           chat_id=message.chat.id,
           reply_markup=reply_markup,
           parse_mode=enums.ParseMode.HTML,
           reply_to_message_id=message.id
       )
