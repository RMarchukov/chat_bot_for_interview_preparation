from aiogram import Router
from aiogram import types, F
from keyboards.questions import build_questions_keyboard
from callback_data_classes.questions import CallbackQuestion, CallbackTopic


question_router = Router()


@question_router.callback_query(CallbackTopic.filter(F.type == "topic"))
async def topic_callback(callback: types.CallbackQuery, callback_data: CallbackTopic) -> None:
    keyboard = await build_questions_keyboard(topic_id=callback_data.id)
    await callback.message.answer(text="Оберіть питання", reply_markup=keyboard.as_markup())


@question_router.callback_query(CallbackQuestion.filter(F.type == "question"))
async def question_callback(callback: types.CallbackQuery, callback_data: CallbackQuestion) -> None:
    await callback.message.answer(text=f"Питання: {callback_data.title}\n\nВідповідь:\n{callback_data.answer}")
