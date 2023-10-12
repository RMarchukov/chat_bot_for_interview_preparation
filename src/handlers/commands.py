from aiogram import Router, types, F
from aiogram.utils.markdown import hbold
from aiogram.filters import CommandStart, Command
from keyboards.questions import build_topics_keyboard
from keyboards.commands import build_commands_keyboard, menu


command_router = Router()


@command_router.message(CommandStart())
async def start_command(message: types.Message) -> None:
    await message.answer(f"Привіт, {hbold(message.from_user.full_name)}!", reply_markup=menu.as_markup())


@command_router.message(Command("menu"))
@command_router.message(F.text == "Меню")
async def menu_command(message: types.Message) -> None:
    await message.answer("Меню", reply_markup=build_commands_keyboard().as_markup())
    await message.delete()


@command_router.message(Command("topics"))
@command_router.message(F.text == "Загальні питання")
async def show_topics_command(message: types.Message) -> None:
    keyboard = build_topics_keyboard()['topics_keyboard']
    await message.answer("Оберіть розділ", reply_markup=keyboard.as_markup())
    await message.delete()
