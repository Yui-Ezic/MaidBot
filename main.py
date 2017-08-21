import telebot
import constants
import maid

# Создание экземпляра Служаночки
servant = maid.Maid()

# Создание экземпляра бота
bot = telebot.TeleBot(constants.token)

# Фильтр матов
def mat_filter(text):
    """
    Функция принимает строку text, и ищет в ней мат с помомщью ключевых слов, записанных в списке constants.Negative.
    Используеться при полученнии сообщения.
    """
    if not text:
        return True
    for keywords in constants.Negative:
        if keywords in text:
            return False
    return True

@bot.message_handler(content_types=['text'])
def handle_text(message):
    """
    Функция вызываеться, когда пользователь присылает текстовое сообщение, и содержит реакции на это сообщеение.
    """

    # Проверяем содержиться ли в строке мат
    if not mat_filter(message.text.lower()):
        bot.send_message(message.from_user.id, "Ата-та, нельзя материться!")
    # Ответ на приветствия.
    elif constants.Greetings.count(message.text.lower()) > 0:
        bot.send_message(message.from_user.id, "Здравствуй хозяин.")
    # Ответ на "как дела?" и подобные
    elif message.text.lower() == "как дела?" or message.text.lower() == "как дела":
        bot.send_message(message.from_user.id, "Отлично, спасибо что интерисуешься :3")
    # Ответ на вопрос об имени
    elif message.text.lower() == ("как тебя зовут?") or message.text.lower() == ("как тебя зовут?"):
        bot.send_message(message.from_user.id, "Меня зовут " + servant.get_name())
    # Ответ на "лол"
    elif message.text.lower() == ("лол"):
        bot.send_message(message.from_user.id, "кек")
    # Заглушка
    else:
        bot.send_message(message.from_user.id, "Простите, я не понимаю что вы хотите :с")

bot.polling(none_stop=True,interval=0)