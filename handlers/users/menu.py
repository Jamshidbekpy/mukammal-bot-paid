from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards.default.menu import keyboard as menu_keyboard
from keyboards.default.pythonmenu import keyboard as python_keyboard

router = Router()

@router.message(Command("menu"))
async def bot_menu(message: types.Message):
    await message.answer("Quyidagi menyudan tanlang:", reply_markup=menu_keyboard)
    
@router.message(F.text == "Telegram bot")
async def bot_start(message: types.Message):
    await message.answer("ictacademy.uz")

@router.message(F.text == "Python")
async def bot_start(message: types.Message):
    await message.answer("Quyidagi menyudan tanlang:", reply_markup=python_keyboard)
    
@router.message(F.text == "00 - Kirish")
async def bot_start(message: types.Message):
    await message.answer_audio(
        audio=types.FSInputFile("media/kirish.mp3"),
        caption="🎧 Bu kirish audiosi"
    )
@router.message(F.text == "01 - Funksiyalar")
async def bot_start(message: types.Message):
    await message.answer_video(
        video=types.FSInputFile("media/kirish.mp4"),
        caption="🎞 Bu video"
    )
@router.message(F.text == "Bosh menu")
async def bot_start(message: types.Message):
    await message.answer("Quyidagi menyudan tanlang:", reply_markup=menu_keyboard)
