from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from Assistant import Abishnoi
from Assistant.database.block_db import is_banned_user
from Assistant.database.users_db import add_served_user


@Abishnoi.on_message(filters.command(["start", "help"]))
async def start_command(c: Abishnoi, message: Message):
    if await is_banned_user(message.from_user.id):
        return

    await add_served_user(message.from_user.id)
    await message.reply_text(
        f"[https://telegra.ph/file/8600403902c26c406ad80.jpg](h) ʜᴇʟʟᴏ {message.from_user.mention}.\n\nᴀssɪsᴛᴀɴᴛ ᴏғ \nғᴇᴇʟ ғʀᴇᴇ ᴛᴏ sᴇɴᴅ ᴍᴇssᴀɢᴇ ʜᴇʀᴇ, ᴅᴏɴ'ᴛ ᴅᴍ",
        
    )
    return
