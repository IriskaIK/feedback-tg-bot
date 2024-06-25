from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from sulguk import AiogramSulgukMiddleware
from sulguk import SULGUK_PARSE_MODE

from config.config import setup_dispatcher

from dotenv import load_dotenv
load_dotenv()


async def main() -> None:
    bot: Bot = Bot(token=getenv("BOT_TOKEN"),
                   default=DefaultBotProperties(parse_mode=SULGUK_PARSE_MODE))
    dp: Dispatcher = setup_dispatcher(
        chat_id=int(getenv('ADMIN_CHAT_ID')),
    )
    bot.session.middleware(AiogramSulgukMiddleware())

    print("Fuck, im alive again")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Interrupted')
