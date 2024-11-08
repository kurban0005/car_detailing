import telebot
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

bot = telebot.TeleBot(os.environ.get("TOKEN_TG_BOT"))

bot_commands = ('\nДоступны команды: '
                '\n/start - запуск бота'
                '\n/m23 - о нас'
                '\n/tg - наш канал'
                '\n/site - наш вебсайт'
                '\n/help - помощь'
                '\n/hello - тестовая функция')

m23_text = (f'M23 Detailing | UFA')


def send_telegram_message(message):
    """Отправляет сообщение в Telegram канал."""
    text_message = (f'Запись от\n'
                    f'\n{message.name}\n'
                    f'\nТелефон: +7{message.phone_number}'
                    f'\nАвто: {message.car_model}'
                    f'\nВопрос: {message.question}\n'
                    f'\n{message.date_add}\n'
                    f'\n\n/help - доступные команды')

    # Отправить сообщение для user1
    bot.send_message(chat_id=os.environ.get("CHAT_ID_KURBAN"), text=text_message)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     f'<b>{m23_text}</b>\n'
                     f'{bot_commands}',
                     parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,
                     f'<b>{m23_text}</b>\n'
                     '\nВ данный момент бот находится в разработке.'
                     f'\n{bot_commands}\n',
                     parse_mode='html')


@bot.message_handler(commands=['m23'])
def m23_info(message):
    bot.send_message(message.chat.id,
                     '<b>M23</b>'
                     '\n<b>DETAILING CENTER | UFA</b>\n'
                     '\nПредоставляем такие услуги как:\n'
                     '\n- Тонирование'
                     '\n- Бронирование'
                     '\n- Химчистка'
                     '\n- Оклейка кузова '
                     '\n- Антихром'
                     '\n- Смена цвета'
                     '\n- Керамика / Жидкое стекло '
                     '\n- Установка доп.оборудования'
                     '\n- Шумоизоляция\n'
                     '\nНаш адрес :'
                     '\nг.Уфа, д. Суровка, ул. Виноградная, 1к3\n'
                     '\nТелефон :'
                     '\n+7 962 533 0005\n'
                     '\nWhatsApp :'
                     '\n+7 962 533 0005\n'
                     '\nНаш сайт : '
                     '\nhttp://m23.technomv.beget.tech\n'
                     '\nНаш телеграм канал : '
                     '\nhttps://t.me/m23detailingufa\n'
                     '\n\n/help - доступные команд\n'
                     '\n\nM23 Detailing center | Ufa',
                     parse_mode='html')


@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id,
                     f'<b>{m23_text}</b>\n'
                     '\nHello . . .\n'
                     f'\nИмя : {message.from_user.first_name} '
                     f'\nФамилия : {message.from_user.last_name} '
                     f'\nТвой id : {message.from_user.id}\n'
                     '\n\n/help - доступные команды',
                     parse_mode='html')


@bot.message_handler(commands=['tg'])
def tg_chanel(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Перейти на канал', url='https://t.me/m23detailingufa'))
    bot.send_message(message.chat.id, f'{m23_text}', reply_markup=markup)


@bot.message_handler(commands=['site'])
def site(message):
    markup = telebot.types.InlineKeyboardMarkup()
    # markup.add(telebot.types.InlineKeyboardButton("Перейти на сайт", url='http://m23.technomv.beget.tech'))
    bot.send_message(message.chat.id, f'Сайт временно не работает')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        hello(message)
    else:
        start(message)


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(types.InLineKeyBoardButton(''))
    bot.reply_to(message, 'Зачем мне это изображение? Лучше отправьте деньги.'
                          '\n\n/help - доступные команды', )


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()
