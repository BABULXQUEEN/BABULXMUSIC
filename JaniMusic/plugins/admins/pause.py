from pyrogram import filters
from pyrogram.types import Message

from JaniMusic import app
from JaniMusic.core.call import Loy
from JaniMusic.utils.database import is_Music_playing, Music_off
from JaniMusic.utils.decorators import AdminRightsCheck
from JaniMusic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.command(["pause", "cpause"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not await is_Music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await Music_off(chat_id)
    await Loy.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
