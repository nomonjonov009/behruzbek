from aiogram.types import Message

from loader import dp 
from utils import texts


@dp.message_handler(commands=['start'])
async def start_handler(message: Message):

    first_name = message.from_user.first_name
    id = message.from_user.id
    username = message.from_user.username
    print(message)

    await message.answer(texts.start(
        first_name=first_name,
        id = id,
        username = username

    ))