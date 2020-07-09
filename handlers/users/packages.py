from aiogram.types import Message
from keyboards.default import packages_uz_button, packages_ru_button, internet_packages_uz_button, internet_packages_ru_button
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher import FSMContext
from loader import dp
from states import Package
from data.messages import sms_packages_ru, sms_packages_uz, minute_packages_ru, minute_packages_uz
from data.messages import internet_month_packages_ru, internet_month_packages_uz, internet_day_packages_ru, internet_day_packages_uz
from data.messages import internet_non_stop_packages_ru, internet_non_stop_packages_uz, internet_tas_ix_packages_uz, internet_tas_ix_packages_ru
from data.config import LANG_STORAGE


@dp.message_handler(Text(equals=["💼 Paketlar", "💼 Пакеты"]))
async def show_packages(message: Message):
    user_id = message.from_user.id
    await Package.Package_menu.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=packages_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=packages_uz_button)


@dp.message_handler(Text(equals=["✉️Sms paketlar", "✉️Sms пакеты"]), state=Package.Package_menu)
async def show_sms_packages(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(sms_packages_ru, reply_markup=packages_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(sms_packages_uz, reply_markup=packages_uz_button)


@dp.message_handler(Text(equals=["📞 Qonqg`iroq uchun paketlar", "📞 Пакеты минут"]), state=Package.Package_menu)
async def show_call_packages(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(minute_packages_ru, reply_markup=packages_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(minute_packages_uz, reply_markup=packages_uz_button)


@dp.message_handler(Text(equals=["🌐 Интернет пакеты", "🌐 Internet paketlar"]), state=Package.Package_menu)
async def show_internet_packages(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Package.Package_internet.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=internet_packages_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=internet_packages_uz_button)


@dp.message_handler(Text(equals=["Месячные Интернет пакеты", "Oylik internet paketlar"]), state=Package.Package_internet)
async def show_month_internet_packages(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(internet_month_packages_ru, reply_markup=internet_packages_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(internet_month_packages_uz, reply_markup=internet_packages_uz_button)


@dp.message_handler(Text(equals=["Ежедневные Интернет пакеты", "Kunlik internet paketlar"]), state=Package.Package_internet)
async def show_day_internet_packages(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(internet_day_packages_ru, reply_markup=internet_packages_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(internet_day_packages_uz, reply_markup=internet_packages_uz_button)


@dp.message_handler(Text(equals=["Интернет нон-стоп пакеты", "Internet non-stop paketlar"]), state=Package.Package_internet)
async def show_non_stop_internet_packages(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(internet_non_stop_packages_ru, reply_markup=internet_packages_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(internet_non_stop_packages_uz, reply_markup=internet_packages_uz_button)


@dp.message_handler(Text(equals=["Пакеты для TAS-IX", "TAS-IX uchun paketlar"]), state=Package.Package_internet)
async def show_tas_ix_internet_packages(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(internet_tas_ix_packages_ru, reply_markup=internet_packages_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(internet_tas_ix_packages_uz, reply_markup=internet_packages_uz_button)


@dp.message_handler(Text(equals=["⬅️ Ortga", "⬅️ Назад"]), state=Package.Package_internet)
async def back(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Package.Package_menu.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=packages_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=packages_uz_button)