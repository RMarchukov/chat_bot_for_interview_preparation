from aiogram import Router
from aiogram import types, F
from keyboards.questions import build_questions_keyboard, build_topics_keyboard
from services.questions import get_questions


question_router = Router()


@question_router.message(F.text.in_(build_topics_keyboard()["topic_filter"]))
async def choose_topic(msg: types.Message):
    res = build_topics_keyboard()["topic_filter"]
    topic_id = res.index(msg.text) + 1
    questions_keyboard = build_questions_keyboard(topic_id)['questions_keyboard']
    await msg.answer(text="Оберіть тему", reply_markup=questions_keyboard.as_markup())


@question_router.message(F.text.in_(build_questions_keyboard()['questions_filter']))
async def choose_question(msg: types.Message):
    res = ''
    questions = await get_questions()
    for question in questions:
        if question["title"] == msg.text:
            res = question["answer"]
            break
    await msg.answer(text=f"<b>Питання:</b> \n{msg.text}\n\n<b>Відповідь:</b> \n{res}", parse_mode="HTML")
