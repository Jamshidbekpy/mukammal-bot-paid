from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router = Router()


# 🔹 1. /panel buyrug‘i — tugma yuboradi
@router.message(Command("panel"))
async def send_main_panel(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🤖 Create Bot", callback_data="create_bot")]
        ]
    )
    await message.answer("Quyidagi menyudan tanlang:", reply_markup=keyboard)


# 🔹 2. FSM holati
class CreateBotState(StatesGroup):
    waiting_for_token = State()


# 🔹 3. Tugma bosilganda yo‘riqnoma chiqaradi
@router.callback_query(F.data == "create_bot")
async def handle_create_bot(callback: CallbackQuery, state: FSMContext):
    text = (
        "<b>🔧 Bot yaratish bo‘yicha yo‘riqnoma:</b>\n\n"
        "1️⃣ <a href='https://t.me/BotFather'>@BotFather</a> ga kiring.\n"
        "2️⃣ /newbot buyrug‘ini yuboring.\n"
        "3️⃣ Bot nomi va username tanlang (masalan: MyShopBot).\n"
        "4️⃣ BotFather sizga <b>API Token</b> beradi.\n\n"
        "🔑 Endi shu tokenni shu yerga yuboring (shunchaki xabar sifatida)."
    )
    await callback.message.answer(text)
    await state.set_state(CreateBotState.waiting_for_token)
    await callback.answer()


# 🔹 4. Tokenni qabul qilish
@router.message(CreateBotState.waiting_for_token)
async def receive_token(message: types.Message, state: FSMContext):
    token = message.text.strip()

    # Oddiy format tekshiruvi
    if ":" not in token:
        await message.answer("⚠️ Bu to‘g‘ri token emas. Iltimos, BotFather bergan tokenni yuboring.")
        return

    # TODO: keyinchalik tokenni bazaga saqlash mumkin
    await message.answer(
        "✅ Token qabul qilindi!\n"
        "Endi sizning botingiz bizning tizim orqali ishlaydi."
    )
    await state.clear()
