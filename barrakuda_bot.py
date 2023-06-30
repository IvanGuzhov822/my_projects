import telebot
from telebot import types

TOKEN = '5695340776:AAHZgPPzlCGD98vUzudHmz6px5muGWSrOgg'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    message_text = """Мероприятия, регаты, походы, прогулки, фотосессии, тренировки и не только на самой красивой и комфортабельный яхте в Казани. Всю необходимую информацию вы можете найти, воспользовавшись этим ботом"""
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton('цена аренды')
    button2 = telebot.types.KeyboardButton('аккаунт в инстаграм')
    button3 = telebot.types.KeyboardButton('геолокация яхт-клуба')
    button4 = telebot.types.KeyboardButton('пассажировместимость')
    button5 = telebot.types.KeyboardButton('контакт для бронирования')
    button6 = telebot.types.KeyboardButton('подборка фото')
    keyboard.add(button1, button2, button3, button4, button5, button6)
    bot.send_message(message.chat.id, message_text, reply_markup=keyboard)

@bot.message_handler(commands=['number'])
def send_number(message):
    number = "+79172907294 Алексей"
    bot.send_message(message.chat.id, number)

@bot.message_handler(commands=['price'])
def send_price(message):
    price = "5000 рублей в час; при заказе прогулки от 4-х часов - цена договорная"
    bot.send_message(message.chat.id, price)

@bot.message_handler(commands=['people'])
def send_people(message):
    peop = "до 8-ми человек"
    bot.send_message(message.chat.id, peop)

@bot.message_handler(commands=['inst'])
def send_insta(message):
    url = 'https://instagram.com/yacht_barracuda_kazan?igshid=YmMyMTA2M2Y='
    bot.send_message(message.chat.id, url)

@bot.message_handler(commands=['geo'])
def send_geo(message):
    url = 'https://www.google.com/maps/place/%D0%9E%D0%9E%D0%9E+%22%D0%AF%D1%85%D1%82-%D0%9A%D0%BB%D1%83%D0%B1+%D0%90%D1%80%D0%B0%D0%BA%D1%87%D0%B8%D0%BD%D0%BE%22/@55.8004842,48.9683012,17z/data=!3m1!4b1!4m6!3m5!1s0x415953b20fbc1e2f:0xb48a31be82326555!8m2!3d55.8004842!4d48.9683012!16s%2Fg%2F11q1r3xn9p'
    bot.send_message(message.chat.id, url)

@bot.message_handler(commands=['photo'])
def send_photo(message):
    pic = open('1.jpg','rb')
    bot.send_photo(message.chat.id, pic)
    pic2 = open('2.jpg','rb')
    bot.send_photo(message.chat.id, pic2)
    pic3 = open('3.jpg','rb')
    bot.send_photo(message.chat.id, pic3)
    pic4 = open('4.jpg','rb')
    bot.send_photo(message.chat.id, pic4)
    pic5 = open('5.jpg','rb')
    bot.send_photo(message.chat.id, pic5)

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.strip()  == 'контакт для бронирования':
        send_number(message)
    elif message.text.strip()  == 'цена аренды':
        send_price(message)
    elif message.text.strip()  == 'пассажировместимость':
        send_people(message)
    elif message.text.strip()  == 'аккаунт в инстаграм':
        send_insta(message)
    elif message.text.strip() == 'геолокация яхт-клуба':
        send_geo(message)
    elif message.text.strip() == 'подборка фото':
        send_photo(message)


bot.polling()

















