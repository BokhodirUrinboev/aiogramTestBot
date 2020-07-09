import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.callback_data import CallbackData

from keyboards.default import service_cancel_button_ru, service_cancel_button_uz, menu_reg_ru_button, menu_ru_button, \
    menu_reg_uz_button, menu_uz_button, service_continue_button_uz, service_continue_button_ru
from keyboards.inline import add_service_ru, add_service_uz
import database
from states import AddServices
from data.config import LANG_STORAGE, NUMBER_STORAGE
from loader import dp
db = database.DBCommands()


@dp.message_handler(Text(equals=["➕ Hizmat qo'shish", "➕ Добавить услугу"]))
async def show_packages(message: Message):
    user_id = message.from_user.id
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("Выберите услугу", reply_markup=add_service_ru)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("Hizmatni tanlang", reply_markup=add_service_uz)


# @dp.callback_query_handler(text="mobile_add", state=AddServices.AddServices_menu)
# async def add_mobile(call: CallbackQuery, message: Message):
#     user_id = message.from_user.id
#     await AddServices.Add_number.set()
#     if LANG_STORAGE[user_id] == 'ru':
#         await message.answer("📱 Для регистрации введите Ваш номер телефона c кодом 99/95", reply_markup=service_cancel_button_ru)
#     elif LANG_STORAGE[user_id] == 'uz':
#         await message.answer("📱 Telefon raqamingizni 99/95 kodi bilan kiriting", reply_markup=service_cancel_button_uz)
#
#
# @dp.message_handler(Text(["❌ Отменить","❌ Bekor qilish"]), state=AddServices.Add_number)
# async def cancel_number(message:Message, state: FSMContext):
#     user_id = message.from_user.id
#     await state.reset_state()
#     if LANG_STORAGE[user_id] == 'ru':
#         if await db.check_attachment(user_id):
#             await message.answer("👇 Выберите действие:", reply_markup=menu_reg_ru_button)
#         else:
#             await message.answer("👇 Выберите действие:", reply_markup=menu_ru_button)
#     elif LANG_STORAGE[user_id] == 'uz':
#         if await db.check_attachment(user_id):
#             await message.answer("👇 Выберите действие:", reply_markup=menu_reg_uz_button)
#         else:
#             await message.answer("👇 Xizmat turini tanlang:", reply_markup=menu_uz_button)
#
#
# @dp.message_handler(regexp=r"^(\d+)$", state=AddServices.Add_number)
# async def add_mobile(state: FSMContext, message: Message):
#     user_id = message.from_user.id
#     if re.match('^(\d{9})$', message.text):
#         mobiles = await db.get_mobile(user_id)
#         for m in mobiles:
#             if (message.text == m.number):
#                 if LANG_STORAGE[user_id] == 'ru':
#                     await message.answer("❗️ Вы хотите повторно ввести существующий сервисный номер!", reply_markup=service_cancel_button_ru)
#                 elif LANG_STORAGE[user_id] == 'uz':
#                     await message.answer("❗️ Siz mavjud bolgan hizmat raqamini qayta kiritmoqchi boldingiz!", reply_markup=service_cancel_button_uz)
#         NUMBER_STORAGE[user_id] = message.text
#         await AddServices.Add_number_pin.set()
#         if LANG_STORAGE[user_id] == 'uz':
#             await message.answer("📵 Kodni to'g'ri kiriting", reply_markup=service_cancel_button_uz)
#         elif LANG_STORAGE[user_id] == 'ru':
#             await message.answer("📵 Введите код правильно", reply_markup=service_cancel_button_ru)
#     else:
#         await AddServices.Add_number.set()
#         if LANG_STORAGE[user_id] == 'ru':
#             await message.answer("📱 Введите правильный номер телефона:99/95*** ** **!",
#                                  reply_markup=service_cancel_button_ru)
#         elif LANG_STORAGE[user_id] == 'uz':
#             await message.answer("📱 Telefon raqamini to'g'ri kiriting:99/95*** ** **!",
#                                  reply_markup=service_cancel_button_uz)
#
#
# @dp.message_handler(regexp=r"^(\d+)$", state=AddServices.Add_number_pin)
# async def add_pin(state: FSMContext, message: Message):
#     user_id = types.User.get_current().id
#     if re.match('^(\d{5})$', message.text):
#         await state.reset_state()
#         mobile = db.attach_mobile(user_id, number=NUMBER_STORAGE[user_id], password=message.text)
#         if LANG_STORAGE[user_id] == 'uz':
#             await message.answer("Tabriklaymiz! Siz muvaffaqiyatli ro'yxatdan o'tdingiz", reply_markup=service_continue_button_uz)
#         elif LANG_STORAGE[user_id] == 'ru':
#             await message.answer("Поздравляем! Вы успешно зарегистрировались", reply_markup=service_continue_button_ru)
#     else:
#         await AddServices.Add_number.set()
#         if LANG_STORAGE[user_id] == 'ru':
#             await message.answer("📵 Введите правильный код",
#                                  reply_markup=service_cancel_button_ru)
#         elif LANG_STORAGE[user_id] == 'uz':
#             await message.answer("📵 To'g'ri kodni kiriting",
#                                  reply_markup=service_cancel_button_uz)
#
# @dp.message_handler(Text(["➡️ Продолжить","➡️ Davom eting"]))
# async def continue_using(message: Message, state: FSMContext):
#     user_id = message.from_user.id
#     await state.reset_state()
#     if LANG_STORAGE[user_id] == 'ru':
#         if await db.check_attachment(user_id):
#             await message.answer("👇 Выберите действие:", reply_markup=menu_reg_ru_button)
#         else:
#             await message.answer("👇 Выберите действие:", reply_markup=menu_ru_button)
#     elif LANG_STORAGE[user_id] == 'uz':
#         if await db.check_attachment(user_id):
#             await message.answer("👇 Выберите действие:", reply_markup=menu_reg_uz_button)
#         else:
#             await message.answer("👇 Xizmat turini tanlang:", reply_markup=menu_uz_button)