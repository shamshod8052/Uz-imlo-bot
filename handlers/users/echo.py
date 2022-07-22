from .checkwords import check_word
from .transliterate import to_cyrillic, to_latin
from aiogram import types
from loader import dp


# Echo bot
@dp.message_handler()
async def echo(message: types.Message):
    word = to_cyrillic(message.text)
    result = check_word(word)
    if result['available']==2:
        response = "Iltimos so'z kiriting!"
    elif result['available']==1:
        response = f"✅ {to_latin(word)}"
    else:
        if len(result['matches'])==0:
            response = "Bunday so'z mavjud emas!!!"
        else:
            result = list(result['matches'])
            for i in range(len(result)):
                result[i] = to_latin(result[i])
            w = "\n✅"+"\n✅ ".join(result)
            response = f"❌ {to_latin(word)} {w}"
    await message.reply(response)