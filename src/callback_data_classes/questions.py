from aiogram.filters.callback_data import CallbackData


class CallbackTopic(CallbackData, prefix="Розділ"):
    id: int
    name: str
    type: str


class CallbackQuestion(CallbackData, prefix="Питання"):
    title: str
    answer: str
    type: str
