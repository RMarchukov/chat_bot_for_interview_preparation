from aiogram.utils.keyboard import InlineKeyboardBuilder
from services.questions import get_topics, get_questions
from callback_data_classes.questions import CallbackQuestion, CallbackTopic


async def build_topics_keyboard() -> InlineKeyboardBuilder:
    topics_keyboard = InlineKeyboardBuilder()
    sizes = ()
    topics = await get_topics()

    for topic in topics:
        topics_keyboard.button(text=topic['name'], callback_data=CallbackTopic(id=topic['id'],
                                                                               name=topic['name'],
                                                                               type="topic"))
        sizes += 1,
    topics_keyboard.adjust(*sizes)
    return topics_keyboard


async def build_questions_keyboard(topic_id: int) -> InlineKeyboardBuilder:
    questions_keyboard = InlineKeyboardBuilder()

    questions = await get_questions()

    for question in questions:
        if question['topic_id'] == topic_id:
            questions_keyboard.button(text=question['title'], callback_data=CallbackQuestion(title=question['title'],
                                                                                             type='question',
                                                                                             answer=question['answer']))

    return questions_keyboard
