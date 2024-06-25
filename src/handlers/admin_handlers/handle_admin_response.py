from os import getenv
from typing import Optional

from aiogram import Bot
from aiogram import F
from aiogram import Router
from aiogram.exceptions import TelegramAPIError
from aiogram.types import Message

from .helper.get_data_from_message import extract_id
from .helper.generate_edited_message import generate_edited_message
from dotenv import load_dotenv

load_dotenv()

router = Router(name="handle_admin_response")


@router.message(F.reply_to_message, F.chat.id == int(getenv('ADMIN_CHAT_ID')))
async def reply_to_user(message: Message, bot: Bot, chat_id: int):
    message_data = extract_id(message.reply_to_message)
    print(message_data)
    if message_data['user_id'] is None and message_data['msg_id'] is None:
        return
    try:
        await bot.copy_message(
            from_chat_id=message.chat.id,
            chat_id=message_data['user_id'],
            message_id=message.message_id,
            reply_to_message_id=message_data['msg_id'],
        )
        if not message_data["answered"]:
            text = generate_edited_message(message_data).replace("Not Answered🔴", "<br/>Answered🟢")
            await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=message.reply_to_message.message_id,
                                    text=text)


    except TelegramAPIError as inner_ex:
        await message.reply(text="Щось пішло не так. Можливо це повідомлення було видалене користувачем.")


__all__ = ["router"]
