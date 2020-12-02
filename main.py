import logging
import telebot
from aiogram import Bot, Dispatcher, executor, types
from information import TOKEN_BOT
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я твой личный помошник по учету твоих финансов! \n"
                        "Не бойся, я не расскажу твоей маме что ты покупаешь пиво))))")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


