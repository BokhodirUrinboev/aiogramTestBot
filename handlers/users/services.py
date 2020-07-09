from aiogram.types import Message
from keyboards.default import services_ru_button, services_uz_button
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher import FSMContext
from loader import dp
from states import Services
from data.messages.services import *
from data.config import LANG_STORAGE


@dp.message_handler(Text(equals=["🔗 Услуги", "🔗 Xizmatlar"]))
async def show_packages(message: Message):
    user_id = message.from_user.id
    await Services.Services_menu.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=services_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=services_uz_button)


@dp.message_handler(Text(equals=["Limitsiz ovoz", "Голос безлимит"]), state=Services.Services_menu)
async def show_non_stop_internet_packages(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(service_unlimited_voice_ru, reply_markup=services_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(service_unlimited_voice_uz, reply_markup=services_uz_button)


@dp.message_handler(Text(equals=["Выручай", "Qo`llab yubor"]), state=Services.Services_menu)
async def show_non_stop_internet_packages(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(service_help_me_ru, reply_markup=services_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(service_help_me_uz, reply_markup=services_uz_button)


@dp.message_handler(Text(equals=["Tungi internet", "Ночной интернет"]), state=Services.Services_menu)
async def show_non_stop_internet_packages(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(service_night_internet_ru, reply_markup=services_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(service_night_internet_uz, reply_markup=services_uz_button)