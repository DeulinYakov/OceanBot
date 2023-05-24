import telebot
from telebot import *
from telebot.types import ReplyKeyboardMarkup
from telebot.types import InputMediaPhoto

# Токен бота
bot = telebot.TeleBot('TOKEN')
main_functions = ('Да, продолжай', 'let’s go',)
# файлы
Mcalls = '1.jpg'
Bcalls = '2.jpg'


# Функции
def startup_keyboard():
    """Функция создающая начальную клавиатуру для выбора функций бота"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add('Готов(а)')
    return markup


def expensive_keyboard():
    """Функция создающая начальную клавиатуру для выбора функций бота"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add('Слушаю, дорогой')
    return markup


def da_keyboard():
    """Функция создающая начальную клавиатуру для выбора функций бота"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add('Да, продолжай')
    return markup


def pod_keyboard():
    """Функция создающая начальную клавиатуру для выбора функций бота"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add('Забрать подарок 🎁')
    return markup


def ee_keyboard():
    """Функция создающая начальную клавиатуру для выбора функций бота"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add('let’s go')
    return markup


def test_keyboard():
    """Функция создающая начальную клавиатуру для выбора функций бота"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add('1. Little Shark ')
    markup.add('2. Ocean Beauty Bar ')
    markup.add('3. Rumpelstilzchen ')
    return markup


def menu_keyboard():
    """Функция создающая начальную клавиатуру для выбора функций бота"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add('Записаться')
    markup.add('Социальные сети')
    markup.add('Связаться с администратором')
    markup.add('Мои подарки 🎁')
    return markup


def send_message_to_user(message, text, keyboard=None):
    """Эта функцию отправит пользователю сообщение"""
    # Отправим сообщение пользователю и добавим нужную клавиатуру
    msg = bot.send_message(message.chat.id, text, reply_markup=keyboard)


# Обработчик команд
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # Если пользователь прошел проверку, то работаем с ним. Напишем приветственное сообщение
    send_message_to_user(message, f'{message.from_user.first_name}, привет 🥳 \nЯ OCEAN BOT 🌊\n\nВ нашем городе '
                                  f'есть очень много секретных мест с потрясающими атмосферой, сервисом и '
                                  f'энергетикой.\n\nОб одном из этих мест я хочу тебе рассказать. Только '
                                  f'постарайся никому не рассказывать🤫 ты готов(а)?', startup_keyboard())


# Обработчик сообщений
@bot.message_handler(content_types=['text'])
def function_ya(message):
    if message.text in 'Готов(а)':
        send_message_to_user(message,
                             f'Кайф  😍  Я сразу почувствовал, что мы на одной 🌊\nА теперь слушай внимательно!',
                             expensive_keyboard())
    elif message.text in 'Слушаю, дорогой':
        send_message_to_user(message, f'На садовом кольце, неподалёку от Американского посольства есть уютная студия '
                                      f'красоты Ocean Beauty Bar\n\nИнтересно?', da_keyboard())
    elif message.text in main_functions:
        send_message_to_user(message, f'Моя ты хорошая, я так люблю, когда меня слушают 🥹\nА еще у меня есть '
                                      f'подарок. Только сначала скажи, как называется студия?', test_keyboard())
    elif message.text in '2. Ocean Beauty Bar ':
        send_message_to_user(message, f'Даааа!\nЗа твою внимательность я дарю тебе 500 рублей, которые ты можешь '
                                      f'потратить на любимые бьюти-процедуры.\nТы рада?', pod_keyboard())
    elif message.text in '3. Rumpelstilzchen ':
        send_message_to_user(message, f'Давай попробуем ещё раз! Я уверен, ты справишься ☺️', ee_keyboard())
    elif message.text in '1. Little Shark ':
        send_message_to_user(message, f'Давай попробуем ещё раз! Я уверен, ты справишься ☺️', ee_keyboard())
    elif message.text in 'Забрать подарок 🎁':
        send_message_to_user(message, 'Почти готово 👏', )
        pic1 = open(Mcalls, "rb")
        pic2 = open(Bcalls, "rb")
        media = [InputMediaPhoto(pic1), InputMediaPhoto(pic2)]
        bot.send_media_group(message.chat.id, media)
        send_message_to_user(message, f'Ура 🥳 я тебя поздравляю 🍾 \nСвоим подарком ты можешь воспользоваться '
                                      f'записавшись онлайн или через администратора. Так же подпишись на наши соц '
                                      f'сети и следи за новостями Ocean Beauty Bar ❤️\n\nДо скорой встречи 🥰',
                             menu_keyboard())
    elif message.text in 'Записаться':
        send_message_to_user(message, f'Записаться - https://b379106.yclients.com/company/360799/select-services'
                                      f'?referrer=https:%2F%2Ftaplink.cc&o=', menu_keyboard())
    elif message.text in 'Социальные сети':
        send_message_to_user(message, f'Telegram - https://t.me/oceanbeautybar\n\nInstagram - '
                                      f'https://instagram.com/_oceanbeautybar_?igshid=YmMyMTA2M2Y=', menu_keyboard())
    elif message.text in 'Связаться с администратором':
        send_message_to_user(message, f'Wa.me/79150550322', menu_keyboard())
    elif message.text in 'Мои подарки 🎁':
        send_message_to_user(message, 'Почти готово 👏', )
        pic1 = open(Mcalls, "rb")
        pic2 = open(Bcalls, "rb")
        media = [InputMediaPhoto(pic1), InputMediaPhoto(pic2)]
        bot.send_media_group(message.chat.id, media)
        send_message_to_user(message, f'500 ₽ на первое посещение студии красоты Ocean 🌊 Beauty Bar 🥳\n\nЗапись '
                                      f'онлайн или через администратора ', menu_keyboard())
    else:
        # пользователь пишет парашу, шлем его
        pass


bot.polling(none_stop=True)
