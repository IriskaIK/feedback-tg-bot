from aiogram import Dispatcher

from .user_handlers.handle_user_message import router as users_router
from .admin_handlers.handle_admin_response import router as admin_router
from .user_handlers.handle_start_command import router as user_start_command_router


def register_handlers(dp: Dispatcher) -> None:
    dp.include_router(user_start_command_router)
    dp.include_router(users_router)
    dp.include_router(admin_router)


__all__ = ["register_handlers"]
