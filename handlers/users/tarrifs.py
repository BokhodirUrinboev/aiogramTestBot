from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from data.messages.tarrifs import *
from data.config import LANG_STORAGE
from states import Tarrifs
from keyboards.default import tarrifs_uz_button, tarrifs_ru_button,mobile_ru_button, mobile_uz_button, internet_uz_button, internet_ru_button, mobile_gsm_uz_button, mobile_gsm_ru_button, mobile_cdma_uz_button, mobile_cdma_ru_button
from aiogram.dispatcher.filters import Command, Text
from loader import dp


@dp.message_handler(Text(equals=["📋 Тарифы","📋 Tariflar"]))
async def show_tarrifs(message: Message):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_menu.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("💎 Bыберите один из следующих:", reply_markup=tarrifs_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("💎 Quyidagilardan birini tanlang:", reply_markup=tarrifs_uz_button)


@dp.message_handler(Text(equals=["📱 Мобильные тарифы","📱 Mobil tariflar"]), state=Tarrifs.Tarrifs_menu)
async def show_mobile(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_mobile.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("💎 Bыберите один из следующих:", reply_markup=mobile_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("💎 Quyidagilardan birini tanlang:", reply_markup=mobile_uz_button)


@dp.message_handler(Text(equals=["🌏 Интернет тарифы","🌏 Internet tariflar"]), state=Tarrifs.Tarrifs_menu)
async def show_internet(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_internet.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("💎 Bыберите один из следующих:", reply_markup=internet_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("💎 Quyidagilardan birini tanlang:", reply_markup=internet_uz_button)


@dp.message_handler(Text(equals=["⬅️ Ortga", "⬅️ Назад"]), state=Tarrifs.Tarrifs_mobile)
@dp.message_handler(Text(equals=["⬅️ Ortga", "⬅️ Назад"]), state=Tarrifs.Tarrifs_internet)
async def back(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_menu.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=tarrifs_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=tarrifs_uz_button)


@dp.message_handler(Text(equals=["⬅️ Ortga", "⬅️ Назад"]), state=Tarrifs.Tarrifs_mobile_cdma)
@dp.message_handler(Text(equals=["⬅️ Ortga", "⬅️ Назад"]), state=Tarrifs.Tarrifs_mobile_gsm)
async def back_mobile_cdma(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_mobile.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=mobile_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=mobile_uz_button)


@dp.message_handler(Text(equals=["Unlim"]), state=Tarrifs.Tarrifs_internet)
async def show_unlim(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_internet.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(unlim_internet_tarrif_ru, reply_markup=internet_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(unlim_internet_tarrif_uz, reply_markup=internet_uz_button)


@dp.message_handler(Text(equals=["RUN"]), state=Tarrifs.Tarrifs_internet)
async def show_run(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_internet.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(run_internet_tarrifs_ru, reply_markup=internet_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(run_internet_tarrifs_uz, reply_markup=internet_uz_button)


@dp.message_handler(Text(equals=["Active new"]), state=Tarrifs.Tarrifs_internet)
async def show_active(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_internet.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(active_internet_tarrifs_ru, reply_markup=internet_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(active_internet_tarrifs_uz, reply_markup=internet_uz_button)


@dp.message_handler(Text(equals=["Start"]), state=Tarrifs.Tarrifs_internet)
async def show_start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_internet.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(start_internet_tarrifs_ru, reply_markup=internet_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(start_internet_tarrifs_uz, reply_markup=internet_uz_button)


@dp.message_handler(Text(equals=["📋 CDMA тарифы","📋 CDMA tariflar"]), state=Tarrifs.Tarrifs_mobile)
async def show_cdma(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_mobile_gsm.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("💎 Bыберите один из следующих:", reply_markup=mobile_gsm_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("💎 Quyidagilardan birini tanlang:", reply_markup=mobile_gsm_uz_button)


@dp.message_handler(Text(equals=["📋 GSM тарифы","📋 GSM tariflar"]), state=Tarrifs.Tarrifs_mobile)
async def show_gsm(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_mobile_cdma.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("💎 Bыберите один из следующих:", reply_markup=mobile_cdma_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("💎 Quyidagilardan birini tanlang:", reply_markup=mobile_cdma_uz_button)


@dp.message_handler(Text(equals=["TR: Oddiy", "ТП: Простой"]), state=Tarrifs.Tarrifs_mobile_cdma)
async def show_simple(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_mobile_cdma.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(simple_cdma_tarrifs_ru, reply_markup=mobile_cdma_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(simple_gsm_tarrifs_uz, reply_markup=mobile_cdma_uz_button)


@dp.message_handler(Text(equals=["TR: Optimal", "ТП: Оптимальный"]), state=Tarrifs.Tarrifs_mobile_cdma)
async def show_optimal(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_mobile_cdma.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(optimal_cdma_tarrifs_ru, reply_markup=mobile_cdma_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(optimal_cdma_tarrifs_uz, reply_markup=mobile_cdma_uz_button)


@dp.message_handler(Text(equals=["TR: Ajoyib", "ТП: Превосходный"]), state=Tarrifs.Tarrifs_mobile_cdma)
async def show_ajoyib(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_mobile_cdma.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(ajoyib_cdma_tarrifs_ru, reply_markup=mobile_cdma_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(ajoyib_cdma_tarrifs_uz, reply_markup=mobile_cdma_uz_button)


@dp.message_handler(Text(equals=["TR: Obod", "ТП: Обод"]), state=Tarrifs.Tarrifs_mobile_cdma)
async def show_obod(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_mobile_cdma.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(obod_cdma_tarrifs_ru, reply_markup=mobile_cdma_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(obod_cdma_tarrifs_uz, reply_markup=mobile_cdma_uz_button)


@dp.message_handler(Text(equals=["TR: Oddiy +", "ТП: Простой +"]), state=Tarrifs.Tarrifs_mobile_cdma)
async def show_simple_plus(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_mobile_cdma.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(simple_plus_cdma_tarrifs_ru, reply_markup=mobile_cdma_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(simple_plus_cdma_tarrifs_uz, reply_markup=mobile_cdma_uz_button)


@dp.message_handler(Text(equals=["TR: Optimal +", "ТП: Оптимальный +"]), state=Tarrifs.Tarrifs_mobile_cdma)
async def show_optimal_plus(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_mobile_cdma.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(optimal_plus_cdma_tarrifs_ru, reply_markup=mobile_cdma_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(optimal_plus_cdma_tarrifs_uz, reply_markup=mobile_cdma_uz_button)


@dp.message_handler(Text(equals=["TR: Ajotib +", "ТП: Превосходный +"]), state=Tarrifs.Tarrifs_mobile_cdma)
async def show_ajoyib_plus(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_mobile_cdma.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(ajoyib_plus_cdma_tarrifs_ru, reply_markup=mobile_cdma_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(ajoyib_plus_cdma_tarrifs_uz, reply_markup=mobile_cdma_uz_button)


@dp.message_handler(Text(equals=["ТП: Street", "TR: Street"]), state=Tarrifs.Tarrifs_mobile_gsm)
async def show_gsm_street(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_mobile_gsm.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(street_gsm_tarrifs_ru, reply_markup=mobile_gsm_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(street_gsm_tarrifs_uz, reply_markup=mobile_gsm_uz_button)


@dp.message_handler(Text(equals=["ТП: Street Upgrade", "TR: Street Upgrade"]), state=Tarrifs.Tarrifs_mobile_gsm)
async def show_gsm_street_up(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_mobile_gsm.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(street_upgrade_gsm_tarrifs_ru, reply_markup=mobile_gsm_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(street_upgrade_gsm_tarrifs_uz, reply_markup=mobile_gsm_uz_button)


@dp.message_handler(Text(equals=["ТП: Onlime", "TR: Onlime"]), state=Tarrifs.Tarrifs_mobile_gsm)
async def show_gsm_onlime(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_mobile_gsm.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(onlime_gsm_tarrifs_ru, reply_markup=mobile_gsm_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(onlime_gsm_tarrifs_uz, reply_markup=mobile_gsm_uz_button)


@dp.message_handler(Text(equals=["ТП: Flash", "TR: Flash"]), state=Tarrifs.Tarrifs_mobile_gsm)
async def show_gsm_flash(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_mobile_gsm.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(flash_gsm_tarrifs_ru, reply_markup=mobile_gsm_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(flash_gsm_tarrifs_uz, reply_markup=mobile_gsm_uz_button)


@dp.message_handler(Text(equals=["ТП: Flash Upgrade", "TR: Flash Upgrade"]), state=Tarrifs.Tarrifs_mobile_gsm)
async def show_gsm_flash_up(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_mobile_gsm.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(flash_upgrade_gsm_tarrifs_ru, reply_markup=mobile_gsm_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(flash_upgrade_gsm_tarrifs_uz, reply_markup=mobile_gsm_uz_button)


@dp.message_handler(Text(equals=["ТП: Royal", "TR: Royal"]), state=Tarrifs.Tarrifs_mobile_gsm)
async def show_gsm_royal(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_mobile_gsm.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(royal_gsm_tarrifs_ru, reply_markup=mobile_gsm_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(royal_gsm_tarrifs_uz, reply_markup=mobile_gsm_uz_button)


@dp.message_handler(Text(equals=["ТП: Деловой", "TR: Ishbilarmon"]), state=Tarrifs.Tarrifs_mobile_gsm)
async def show_gsm_bussiness(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_mobile_gsm.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(bussiness_gsm_tarrifs_ru, reply_markup=mobile_gsm_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(bussiness_gsm_tarrifs_uz, reply_markup=mobile_gsm_uz_button)


@dp.message_handler(Text(equals=["ТП: Просто 10", "TR: Oddiy 10"]), state=Tarrifs.Tarrifs_mobile_gsm)
async def show_gsm_simple(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await Tarrifs.Tarrifs_mobile_gsm.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer(simple_gsm_tarrifs_ru, reply_markup=mobile_gsm_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer(simple_gsm_tarrifs_uz, reply_markup=mobile_gsm_uz_button)