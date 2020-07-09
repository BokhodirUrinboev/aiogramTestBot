from aiogram.types import Message
from keyboards.default.useful import *
from aiogram.dispatcher.filters import Command, Text
from data.messages.usefull import *
from keyboards.default.lang import *
from keyboards.inline import *
from aiogram.dispatcher import FSMContext
from loader import dp
from states import Usefull
from data.config import LANG_STORAGE


@dp.message_handler(Text(equals=["📌 Foydali", "📌 Полезное"]))
async def show_usefulls(message: Message):
    user_id = message.from_user.id
    await Usefull.Usefull_menu.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=usefull_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=usefull_uz_button)


@dp.message_handler(Text(equals=["🏢 Kompaniya haqida", "🏢 О Компании"]), state=Usefull.Usefull_menu)
async def show_about(message: Message):
    user_id = message.from_user.id
    await Usefull.Usefull_menu.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(usefull_about_ru, reply_markup=usefull_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(usefull_about_uz, reply_markup=usefull_uz_button)


@dp.message_handler(Text(equals=["ℹ️IMEI-kod bo'yicha ma'lumot", "ℹ️Информация по IMEI-коду"]), state=Usefull.Usefull_menu)
async def show_about(message: Message):
    user_id = message.from_user.id
    await Usefull.Usefull_menu.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(usefull_imei_ru, reply_markup=usefull_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(usefull_imei_uz, reply_markup=usefull_uz_button)


@dp.message_handler(Text(equals=["📟 USSD komandalar", "📟 USSD команды"]), state=Usefull.Usefull_menu)
async def show_about(message: Message):
    user_id = message.from_user.id
    await Usefull.Usefull_ussd.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=ussd_command_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=ussd_command_uz_button)


@dp.message_handler(Text(equals=["GSM Tariflar", "GSM Тарифы"]), state=Usefull.Usefull_ussd)
async def show_gsm_tarrifs(message: Message):
    user_id = message.from_user.id
    await Usefull.Usefull_ussd.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(gsm_tarrifs_ru, reply_markup=ussd_command_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(gsm_tarrifs_uz, reply_markup=ussd_command_uz_button)


@dp.message_handler(Text(equals=["GSM SMS"]), state=Usefull.Usefull_ussd)
async def show_gsm_sms(message: Message):
    user_id = message.from_user.id
    await Usefull.Usefull_ussd.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(gsm_sms_ru, reply_markup=ussd_command_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(gsm_sms_uz, reply_markup=ussd_command_uz_button)


@dp.message_handler(Text(equals=["GSM Минуты", "GSM Minut"]), state=Usefull.Usefull_ussd)
async def show_gsm_minutes(message: Message):
    user_id = message.from_user.id
    await Usefull.Usefull_ussd.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(gsm_minutes_ru, reply_markup=ussd_command_uz_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(gsm_minutes_uz, reply_markup=ussd_command_uz_button)


@dp.message_handler(Text(equals=["GSM Интернет", "GSM Internet"]), state=Usefull.Usefull_ussd)
async def show_gsm_internet(message: Message):
    user_id = message.from_user.id
    await Usefull.Usefull_ussd_internet.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=gsm_internet_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=gsm_internet_uz_button)


@dp.message_handler(Text(equals=["Месячный интернет", "Oylik internet"]), state=Usefull.Usefull_ussd_internet)
async def show_gsm_internet_month(message: Message):
    user_id = message.from_user.id
    await Usefull.Usefull_ussd_internet.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(gsm_internet_monthly_ru, reply_markup=gsm_internet_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(gsm_internet_monthly_uz, reply_markup=gsm_internet_uz_button)


@dp.message_handler(Text(equals=["Ежедневный интернет", "Kunlik internet"]), state=Usefull.Usefull_ussd_internet)
async def show_gsm_internet_day(message: Message):
    user_id = message.from_user.id
    await Usefull.Usefull_ussd_internet.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(gsm_internet_dayly_ru, reply_markup=gsm_internet_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(gsm_internet_dayly_uz, reply_markup=gsm_internet_uz_button)


@dp.message_handler(Text(equals=["Интернет нон-стоп", "Internet non-stop"]), state=Usefull.Usefull_ussd_internet)
async def show_gsm_internet_non_stop(message: Message):
    user_id = message.from_user.id
    await Usefull.Usefull_ussd_internet.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(gsm_internet_non_stop_ru, reply_markup=gsm_internet_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(gsm_internet_non_stop_uz, reply_markup=gsm_internet_uz_button)


@dp.message_handler(Text(equals=["⬅️ Ortga", "⬅️ Назад"]), state=Usefull.Usefull_ussd)
async def back_usefull_menu(message:Message):
    user_id = message.from_user.id
    await Usefull.Usefull_menu.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=usefull_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=usefull_uz_button)


@dp.message_handler(Text(equals=["⬅️ Ortga", "⬅️ Назад"]), state=Usefull.Usefull_ussd_internet)
async def back_usefull_ussd(message:Message):
    user_id = message.from_user.id
    await Usefull.Usefull_ussd.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=ussd_command_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=ussd_command_uz_button)


@dp.message_handler(Text(equals=["⬅️ Ortga", "⬅️ Назад"]), state=Usefull.Usefull_cabinet)
@dp.message_handler(Text(equals=["⬅️ Ortga", "⬅️ Назад"]), state=Usefull.Usefull_send_message)
async def back_usefull_ussd(message:Message):
    user_id = message.from_user.id
    await Usefull.Usefull_menu.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=usefull_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=usefull_uz_button)


@dp.message_handler(Text(equals=["✉️ Murojaat yuborish", "✉️ Отправить обращение"]), state=Usefull.Usefull_menu)
async def show_send_message(message: Message):
    user_id = message.from_user.id
    await Usefull.Usefull_send_message.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=basic_cancel_button_ru)
        await message.answer("Отправить обращение через официальный веб-сайт", reply_markup=usefull_send_message_ru)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=basic_cancel_button_uz)
        await message.answer("Murojaatingizni rasmiy sayt orqali qoldirishingiz mumkin", reply_markup=usefull_send_message_uz)


@dp.message_handler(Text(equals=["👤 Личный кабинет", "👤 Shaxsiy kabinet"]), state=Usefull.Usefull_menu)
async def show_cabinate(message: Message):
    user_id = message.from_user.id
    await Usefull.Usefull_cabinet.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=basic_cancel_button_ru)
        await message.answer("Войти в личный кабинет через официальный веб-сайт", reply_markup=usefull_cabinate_ru)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=basic_cancel_button_uz)
        await message.answer("Shaxsiy kabinetga rasmiy sayt orqali kirishingiz mumkin", reply_markup=usefull_cabinate_uz)