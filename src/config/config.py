from aiogram import Dispatcher
from src.handlers import register_handlers


def setup_dispatcher(chat_id: int) -> Dispatcher:
    dp: Dispatcher = Dispatcher(chat_id=chat_id)

    register_handlers(dp)
    return dp


__all__ = ["setup_dispatcher"]
