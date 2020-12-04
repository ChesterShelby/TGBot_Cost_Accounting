import telebot
import logging
from aiogram import Bot, Dispatcher, executor, types
from information import TOKEN_BOT
from registration_users import RegistRation

logging.basicConfig(level=logging.INFO)
bot_t = telebot.TeleBot(TOKEN_BOT)
bot_a = Bot(token=TOKEN_BOT)
db = RegistRation('db.db')
dp = Dispatcher(bot_a)
keyboard1 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard1.row('/start', '/reg', '/unreg')


@bot_t.message_handler(commands=['start'])
def start_message(message):
    print('Bot start')
    bot_t.send_message(message.chat.id, 'Привет! Я твой личный помошник по учету твоих финансов! \n' 'Не бойся, я не '
                                        'расскажу твоей маме, что ты покупаешь пиво))))', reply_markup=keyboard1)


@bot_t.message_handler(commands=['reg'])
async def register(message: types.Message):
    print(1)
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
    else:
        db.update_users(message.from_user.id, True)

    await message.answer("Вы успешно зарегистрировались", reply_markup=keyboard1)


@bot_t.message_handler(commands=['unreg'])
async def register(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id, False)
        await message.answer("Вы и так не зарегистрированы", reply_markup=keyboard1)
    else:
        db.update_users(message.from_user.id, False)
        await message.answer("Ваша таблица расходов удалена", reply_markup=keyboard1)

bot_t.polling(none_stop=True, interval=0)
