import telebot
import constants
import maid

servant = maid.Maid()

bot = telebot.TeleBot(constants.token)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if constants.Greetings.count(message.text.lower()) > 0:
        bot.send_message(message.from_user.id, "Здравствуй хозяин.")
    elif message.text.lower() in "как дела?":
        bot.send_message(message.from_user.id, "Отлично, спасибо что интерисуешься :3")
    elif message.text.lower() in ("как тебя зовут?"):
        bot.send_message(message.from_user.id, "Меня зовут " + servant.get_name())
    else:
        bot.send_message(message.from_user.id, "Простите, я не понимаю что вы хотите :с")

bot.polling(none_stop=True,interval=0)