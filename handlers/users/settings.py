from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from data.messages.tarrifs import *
from data.config import LANG_STORAGE
import database
from states import Settings
from keyboards.default import settings_uz_button, settings_ru_button, change_lang_uz_button, change_lang_ru_button, \
    menu_reg_ru_button, menu_ru_button, menu_reg_uz_button, menu_uz_button
from aiogram.dispatcher.filters import Command, Text
from loader import dp
db = database.DBCommands()

@dp.message_handler(Text(equals=["📥 Sozlamalar","📥 Настройки"]))
async def show_settings(message: Message):
    user_id = message.from_user.id
    await Settings.Settings_menu.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=settings_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Sozlamalardan birini tanlang:", reply_markup=settings_uz_button)


@dp.message_handler(Text(equals=["🌍 Tilni o'zgaritirish","🌍 Изменить язык"]), state=Settings.Settings_menu)
async def show_language(message: Message):
    user_id = message.from_user.id
    await Settings.Settings_change_lang.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("🌍 Выберите один из следующих языков:", reply_markup=change_lang_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("🌍 Quyidagi tillardan birini tanlang:", reply_markup=change_lang_uz_button)


@dp.message_handler(Text(equals=["🇷🇺 Русский","🇺🇿 O'zbek"]), state=Settings.Settings_change_lang)
async def change_language(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await state.reset_state()
    if message.text == "🇷🇺 Русский":
        LANG_STORAGE[user_id] = 'ru'
        await db.set_language('ru')
        if await db.check_attachment(user_id):
            await message.answer("👇 Выберите действие:", reply_markup=menu_reg_ru_button)
        else:
            await message.answer("👇 Выберите действие:", reply_markup=menu_ru_button)
    elif message.text == "🇺🇿 O'zbek":
        LANG_STORAGE[user_id] = 'uz'
        await db.set_language('uz')
        if await db.check_attachment(user_id):
            await message.answer("👇 Выберите действие:", reply_markup=menu_reg_uz_button)
        else:
            await message.answer("👇 Xizmat turini tanlang:", reply_markup=menu_uz_button)


@dp.message_handler(Text(equals=["⬅️ Ortga", "⬅️ Назад"]), state=Settings.Settings_change_lang)
async def go_back_settings(message:Message):
    user_id = message.from_user.id
    await Settings.Settings_menu.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=settings_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Sozlamalardan birini tanlang:", reply_markup=settings_uz_button)