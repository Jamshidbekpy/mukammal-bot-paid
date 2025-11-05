import asyncio
# from aiogram import Bot, Dispatcher
from loader import bot, dp

from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
import middlewares, filters, handlers

# from data.config import BOT_TOKEN

# Botni yaratish
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher()

# Middlewares, handlers avtomatik import qilingan bo'lishi mumkin
# Agar kerak bo'lsa, dp.include_router(router) ishlatiladi

async def on_startup():
    """Bot ishga tushganda bajariladigan funksiyalar"""
    # Asosiy komandalarni o'rnatish
    await set_default_commands(bot)

    # Adminlarga xabar yuborish
    await on_startup_notify(dp)

    print("✅ Bot muvaffaqiyatli ishga tushdi!")


async def main():
    # Botni ishga tushirish
    await on_startup()
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
