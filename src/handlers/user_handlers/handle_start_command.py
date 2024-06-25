from os import getenv

from aiogram import Bot
from aiogram import F
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from dotenv import load_dotenv
load_dotenv()

router = Router(name="handle_user_start_command")


@router.message(F.chat.id == F.from_user.id,
                F.chat.id != int(getenv('ADMIN_CHAT_ID')),
                Command('start')
                )
async def handle_start_message(
        message: Message,
        bot: Bot,
        chat_id: int,
):
    await bot.send_message(message.chat.id, text="Вітаю! Це бот для фідбека. "
                                         "Напишіть своє запитання і адмін обов'язково зв'яжеться з вами!")


__all__ = ["router"]
