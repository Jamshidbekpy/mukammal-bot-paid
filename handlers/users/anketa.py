from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.filters.state import StateFilter
from states.personalData import PersonalData
from aiogram import Router

router = Router()

# Boshlanish komandasi
@router.message(Command("anketa"))
async def anketa_start(message: types.Message, state: FSMContext):
    await message.answer("Iltimos, to'liq ismingizni kiriting:")
    await state.set_state(PersonalData.fullname)

# Fullname qabul qilish
@router.message(StateFilter(PersonalData.fullname))
async def process_fullname(message: types.Message, state: FSMContext):
    await state.update_data(fullname=message.text)
    await message.answer("Iltimos, elektron pochta manzilingizni kiriting:")
    await state.set_state(PersonalData.email)

# Email qabul qilish
@router.message(StateFilter(PersonalData.email))
async def process_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("Iltimos, telefon raqamingizni kiriting:")
    await state.set_state(PersonalData.phone)

# Telefon qabul qilish va yakunlash
@router.message(StateFilter(PersonalData.phone))
async def process_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    user_data = await state.get_data()
    await message.answer(
        f"Sizning ma'lumotlaringiz:\n"
        f"To'liq ism: {user_data['fullname']}\n"
        f"Email: {user_data['email']}\n"
        f"Telefon: {user_data['phone']}\n"
        "Rahmat!"
    )
    await state.clear()  # FSMni tozalash
