from aiogram.types import Message
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from keyboards.default import *
from loader import dp
import database
from data.config import LANG_STORAGE
db = database.DBCommands()



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    user = await db.get_user(user_id)
    if user is not None:
        if user.language == 'ru':
            LANG_STORAGE[user_id] = 'ru'
            if await db.check_attachment(user_id):
                await message.answer("👇 Выберите действие:", reply_markup=menu_reg_ru_button)
            else:
                await message.answer("👇 Выберите действие:", reply_markup=menu_ru_button)
        elif user.language == 'uz':
            LANG_STORAGE[user_id] = 'uz'
            if await db.check_attachment(user_id):
                await message.answer("👇 Выберите действие:", reply_markup=menu_reg_uz_button)
            else:
                await message.answer("👇 Xizmat turini tanlang:", reply_markup=menu_uz_button)
    else:
        user = await db.add_new_user()
        await message.answer("🌍 Язык/Til:", reply_markup=language_button)


@dp.message_handler(Text(equals=["🏠 Bosh sahifaga", "🏠 На главную"]), state="*")
async def back(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await state.reset_state()
    if LANG_STORAGE[user_id] == 'ru':
        if await db.check_attachment(user_id):
            await message.answer("👇 Выберите действие:", reply_markup=menu_reg_ru_button)
        else:
            await message.answer("👇 Выберите действие:", reply_markup=menu_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        if await db.check_attachment(user_id):
            await message.answer("👇 Выберите действие:", reply_markup=menu_reg_uz_button)
        else:
            await message.answer("👇 Xizmat turini tanlang:", reply_markup=menu_uz_button)