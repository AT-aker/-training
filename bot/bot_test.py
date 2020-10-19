from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="1330106143:AAHpIavxj4NjPUq3T_GUxi3Xnw8W_myvGRM")
dp = Dispatcher(bot)

@dp.message_handler()
async def get_message(message:types.Message)
    chat_id = message.chat.id
    text = 'Hi my little friend'
    await bot.send_message(chat_id=chat_id, text=text)
executor.start_polling(dp)

