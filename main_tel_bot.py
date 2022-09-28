# Телеграмм бот TestWorkPeople

from telegram import Update, Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ContextTypes
from credits import bot_token
from main import data_processor
from data_provider import read_file

bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher



def start(update, context):
    context.bot.send_message(update.effective_chat.id,  "Привет")
    context.bot.send_message(update.effective_chat.id, "Я помогу узнать информацию о сотрудниках")
    context.bot.send_message(update.effective_chat.id, "Если вам необходима помощь нажмите - /help")

def help(update, context):
    update.message.reply_text(f'/1 - ID\n/2 - ФИО\n/3 - День рождения\n/4 - Должность\n/5 - Пол\n/6 - Все данные\n')

def id(update, context):
    update.message.reply_text(str(data_processor(read_file('result.csv'), 1)))

def fio(update, context):
    update.message.reply_text(str(data_processor(read_file('result.csv'), 2)))

def birthday(update, context):
    update.message.reply_text(str(data_processor(read_file('result.csv'), 3)))

def post(update, context):
    update.message.reply_text(str(data_processor(read_file('result.csv'), 4)))

def sex(update, context):
    update.message.reply_text(str(data_processor(read_file('result.csv'), 5)))

def all_data(update, context):
    update.message.reply_text(str(data_processor(read_file('result.csv'), 6)))

def exit(update, context):
    update.message.reply_text(str(data_processor(read_file('result.csv'), 0)))

def info(update, context):
    context.bot.send_message(update.effective_chat.id, f'/help\n/command\n')

def command(update, context): # пока не получается привязать кнопки к необходимой информации
    keyboard = [[InlineKeyboardButton("ID", callback_data='1'), InlineKeyboardButton("ФИО", callback_data='2')],
               [InlineKeyboardButton("День рождения", callback_data='3'), InlineKeyboardButton("Должность", callback_data='4')],
               [InlineKeyboardButton("Пол", callback_data='5'), InlineKeyboardButton("Все данные", callback_data='6')],
                [InlineKeyboardButton("Выход", callback_data='0')]]
    update.message.reply_text('Выбери необходимую информацию', reply_markup=InlineKeyboardMarkup(keyboard))

def button(update, context):
    query = update.callback_query
    query.answer()
    if query.data == '1':

        context.bot.send_message(update.effective_chat.id, text="ID")
        print('1')
    elif query.data == '2':
        context.bot.send_message(update.effective_chat.id, text="ФИО")
        print('2')
    elif query.data == '3':
        context.bot.send_message(update.effective_chat.id, text="День рождения")
        print('3')
    elif query.data == '4':
        context.bot.send_message(update.effective_chat.id, text="Должность")
        print('4')
    elif query.data == '5':
        context.bot.send_message(update.effective_chat.id, text="Пол")
        print('5')
    elif query.data == '6':
        context.bot.send_message(update.effective_chat.id, text="Все данные")
        print('6')
    elif query.data == '0':
        context.bot.send_message(update.effective_chat.id, text="Выход")
        print('0')


start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)

id_handler = CommandHandler('1', id)
fio_handler = CommandHandler('2', fio)
birthday_handler = CommandHandler('3', birthday)
post_handler = CommandHandler('4', post)
sex_handler = CommandHandler('5', sex)
all_data_handler = CommandHandler('6', all_data)
exit_handler = CommandHandler('0', exit)

info_handler = CommandHandler('info', info)
command_handler = CommandHandler('command', command)
button_handler = CallbackQueryHandler(button)



dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)

dispatcher.add_handler(id_handler)
dispatcher.add_handler(fio_handler)
dispatcher.add_handler(birthday_handler)
dispatcher.add_handler(post_handler)
dispatcher.add_handler(sex_handler)
dispatcher.add_handler(all_data_handler)
dispatcher.add_handler(exit_handler)

dispatcher.add_handler(info_handler)
dispatcher.add_handler(command_handler)
dispatcher.add_handler(button_handler)


updater.start_polling()


updater.idle()