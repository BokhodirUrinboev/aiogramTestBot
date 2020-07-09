from aiogram.dispatcher.filters.state import StatesGroup, State


class Package(StatesGroup):
    Package_menu = State()
    Package_internet = State()


class Services(StatesGroup):
    Services_menu = State()


class Balance(StatesGroup):
    Balance_menu = State()


class AddServices(StatesGroup):
    AddServices_menu = State()
    Add_number = State()
    Add_number_pin = State()
    Add_internet = State()
    Add_password = State()


class Tarrifs(StatesGroup):
    Tarrifs_menu = State()
    Tarrifs_internet = State()
    Tarrifs_mobile = State()
    Tarrifs_mobile_cdma = State()
    Tarrifs_mobile_gsm = State()


class Usefull(StatesGroup):
    Usefull_menu = State()
    Usefull_ussd = State()
    Usefull_cabinet = State()
    Usefull_message = State()
    Usefull_ussd_internet = State()
    Usefull_send_message = State()
    Usefull_cabinet = State()


class Settings(StatesGroup):
    Settings_menu = State()
    Settings_change_lang = State()
    Setings_management = State()