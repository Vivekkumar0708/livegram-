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
        f"ʜᴇʟʟᴏ .\n\nᴀssɪsᴛᴀɴᴛ ᴏғ [विवेक कुमार](t.me/vivekkumar07089\nғᴇᴇʟ ғʀᴇᴇ ᴛᴏ sᴇɴᴅ ᴍᴇssᴀɢᴇ ʜᴇʀᴇ, ᴅᴏɴ'ᴛ ᴅᴍ",
        
    )
    return
