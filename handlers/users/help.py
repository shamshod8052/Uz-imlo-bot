from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Bu bot so'zlarni to'g'ri yozilganini tekshiradi. Agar so'z noto'g'ri yozilgan bo'lsa, unga o'xshash so'zlarni chiqaradi.")
    
    # await message.answer("\n".join(text))

    await message.answer(text)