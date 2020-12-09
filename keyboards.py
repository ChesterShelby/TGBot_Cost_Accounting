import telebot


class KeyBoard:
    keyboard1 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    def keyboard_1(self):
        self.keyboard1.row('/start', '/регистрация')
