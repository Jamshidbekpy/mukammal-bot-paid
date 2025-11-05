from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from handlers.users.echo import router as echo_router
from handlers.users.start import router as start_router
from handlers.users.anketa import router as anketa_router
from handlers.users.webapp import router as webapp_router
from handlers.users.createbot import router as createbot_router
from handlers.users.menu import router as menu_router

from data import config

# Default xususiyatlar orqali parse_mode ni o‘rnatamiz
bot = Bot(
    token=config.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(anketa_router)
dp.include_router(webapp_router)
dp.include_router(createbot_router)
dp.include_router(menu_router)
dp.include_router(echo_router)  

