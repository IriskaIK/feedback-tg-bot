from os import getenv

from aiogram import Bot
from aiogram import F
from aiogram import Router
from aiogram.enums import ContentType
from aiogram.types import Message
from .helper.generate_message_to_admin import generate_message_to_admin

from dotenv import load_dotenv
load_dotenv()


available_content_types = (
    ContentType.TEXT,
    ContentType.ANIMATION,
    ContentType.AUDIO,
    ContentType.DOCUMENT,
    ContentType.PHOTO,
    ContentType.VIDEO,
    ContentType.VOICE,
)

router = Router(name="handle_user_message")


@router.message(F.chat.id == F.from_user.id, F.chat.id != int(getenv('ADMIN_CHAT_ID')))
async def handle_message(
        message: Message,
        bot: Bot,
        chat_id: int,
):
    if message.content_type not in available_content_types:
        await message.reply(
            text="Тип повідомлення не підтримується!",
        )
        return

    from_chat_id = message.from_user.id
    message_id = message.message_id

    if message.text:
        if len(message.text) > 4096:
            await message.reply(text="Занадто довге повідомлення!")
            return

        message_text = generate_message_to_admin(message) + message.html_text + "<br/>Not Answered🔴"
        await bot.send_message(chat_id=chat_id, text=message_text)

    else:
        if message.caption and len(message.caption) > 1024:
            await message.reply(text="Занадто довге повідомлення!")
            return

        caption = message.caption if message.caption else ""
        caption = generate_message_to_admin(message) + caption + "<br/>Not Answered🔴"

        await bot.copy_message(
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_id=message_id,
            caption=caption,
        )
    return


__all__ = ["router"]
