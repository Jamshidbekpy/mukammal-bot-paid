from aiogram import Router, types
from aiogram.filters import Command
from keyboards.default.start import keyboard

router = Router()

# 🔹 /start komandasi
@router.message(Command("start"))
async def bot_start(message: types.Message):
    await message.answer(
        f"Salom, {message.from_user.full_name}! 👋\n"
        "Quyidagi tugmalardan birini tanlang:",
        reply_markup=keyboard
    )


# 🔹 Kontakt yuborilganda
@router.message(lambda message: message.contact)
async def contact_handler(message: types.Message):
    phone = message.contact.phone_number
    name = message.contact.first_name
    await message.answer(f"✅ Raxmat, {name}!\nSening telefon raqaming: {phone}")


# 🔹 Joylashuv yuborilganda
@router.message(lambda message: message.location)
async def location_handler(message: types.Message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    await message.answer(
        f"📍 Joylashuving qabul qilindi!\n\n"
        f"Latitude: {latitude}\nLongitude: {longitude}"
    )
