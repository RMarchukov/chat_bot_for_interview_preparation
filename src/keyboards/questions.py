from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton
import requests


def build_topics_keyboard():
    topics_keyboard = ReplyKeyboardBuilder()
    topics = requests.get("https://api-for-python-interview-preparation.onrender.com/topics").json()

    for topic in topics:
        topics_keyboard.row(KeyboardButton(text=topic["name"]))
    return {'topics_keyboard': topics_keyboard, 'topic_filter': [topic['name'] for topic in topics]}


def build_questions_keyboard(topic_id=None):
    questions_keyboard = ReplyKeyboardBuilder()
    questions = requests.get("https://api-for-python-interview-preparation.onrender.com/questions").json()

    for question in questions:
        if question['topic_id'] == topic_id:
            questions_keyboard.button(text=question['title'])
    questions_keyboard.adjust(2, 2)

    return {'questions_keyboard': questions_keyboard, 'questions_filter': [question['title'] for question in questions]}
