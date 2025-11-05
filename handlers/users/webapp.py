from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.filters import Command
from aiogram import types, Router

router = Router()

WEB_APP_URL = "https://ictacademy.uz"  # Ngrok orqali HTTPS

@router.message(Command("webapp"))
async def send_webapp_button(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="Web Appga kirish",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )]
        ]
    )
    await message.answer("Web Appga kirish uchun tugmani bosing:", reply_markup=keyboard)
