from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton


def build_commands_keyboard():
    commands_keyboard = ReplyKeyboardBuilder()
    commands_list = ["Загальні питання", "Особисті питання", "Додати питання", "Перевірити знання"]
    for command in commands_list:
        commands_keyboard.row(KeyboardButton(text=command))
    return commands_keyboard


menu = ReplyKeyboardBuilder().add(KeyboardButton(text="Меню"))
