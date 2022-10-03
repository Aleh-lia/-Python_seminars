from telegram import Update, Bot, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from credits import bot_token


bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

GENDER = 0
PHOTO = 1
BIO = 2
VIDEO = 3
YEARS = 4
EDUCATION = 5


def start(update,context):
    reply_keyboard = [['Мужчина', 'Женщина']]
    update.message.reply_text('Добрый день! Мы ООО. Укажите свой пол',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return GENDER

def gender(update,context):
    update.message.reply_text('Супер! Теперь отправьте свое фото, или нажмите /skip для пропуска этого шага')
    return PHOTO

def photo(update,context):
    user = str(update.message.from_user['username'])
    photo_file = update.message.document.get_file()
    photo_file.download(user + '_photo.jpg')
    update.message.reply_text('Супер! Мы получили Ваше фото. Теперь отправте краткое резюме о себе или нажмите'
                              ' /skip для пропуска этого шага')
    return BIO

def skip_photo(update,context):
    update.message.reply_text('Значит без фото! Теперь отправте краткое резюме о себе или нажмите'
                              ' /skip для пропуска этого шага')
    return BIO

def bio(update,context):
    user = str(update.message.from_user['username'])
    update.message.reply_text('Супер! Мы получили Ваше резюме.Теперь отправте краткое видео о себе или нажмите'
                              ' /skip для пропуска этого шага')
    f = open(user + 'bio.txt', 'w')
    f.write(update.message.text)
    f.close()
    return VIDEO

def skip_bio(update,context):
    update.message.reply_text('Значит без резюме! Тогда ответьте на несколько вопросов или нажмите'
                              ' /skip для пропуска этого шага')
    return YEARS

def bio_years(update,context):
    user = str(update.message.from_user['username'])
    update.message.reply_text('Отлично! Теперь укажите какое у Вас образование или нажмите'
                              ' /skip для пропуска этого шага')
    f = open(user + 'bio.txt', 'w')
    f.write(update.message.text)
    f.close()
    return EDUCATION

def skip_bio_years(update,context):
    update.message.reply_text('Тогда ответьте на следующий вопрос нажмите'
                              ' /skip для пропуска этого шага')
    return EDUCATION

def bio_education(update, context):
    user = str(update.message.from_user['username'])
    update.message.reply_text('Отлично! Теперь отправьте короткое видео о себе или нажмите'
                              ' /skip для пропуска этого шага')
    f = open(user + 'bio.txt', 'w')
    f.write(update.message.text)
    f.close()
    return VIDEO

def skip_bio_education(update,context):
    update.message.reply_text('Тогда отправьте короткое видео о себе или нажмите'
                              ' /skip для пропуска этого шага')
    return VIDEO


def video(update,context):
    user = str(update.message.from_user['username'])
    video_file = update.message.document.get_file()
    video_file.download(user + '_video.mp4')
    update.message.reply_text('Супер! Мы получили Ваше видео.Мы свяжемся с вами')
    return ConversationHandler.END

def skip_video(update,context):
    update.message.reply_text('Значит без видео! Мы свяжемся с вами')
    return ConversationHandler.END

def cancel(update,context):
    update.message.reply_text('Надеюсь еще напишете нам')
    return ConversationHandler.END






start_handler = CommandHandler('start', start)

gender_handler = MessageHandler(Filters.regex('^(Мужчина|Женщина)$'), gender)

photo_handler = MessageHandler(Filters.photo, photo)
skip_photo_handler = CommandHandler('skip', skip_photo)

bio_handler = MessageHandler(Filters.text & (~Filters.command), bio)
skip_bio_handler = CommandHandler('skip', skip_bio)
bio_years_handler = MessageHandler(Filters.text & (~Filters.command), bio_years)
skip_bio_years_handler = CommandHandler('skip', skip_bio)
bio_education_handler = MessageHandler(Filters.text & (~Filters.command), bio_education)
skip_bio_education_handler = CommandHandler('skip', skip_bio)

video_handler = MessageHandler(Filters.video, video)
skip_video_handler = CommandHandler('skip', skip_video)

cancel_handler = CommandHandler('cancel', cancel)
conv_handler = ConversationHandler(
    entry_points=[start_handler],
    states={
        GENDER: [gender_handler],
        PHOTO: [photo_handler, skip_photo_handler],
        BIO: [bio_handler, skip_bio_handler],
        YEARS:[bio_years_handler, skip_bio_years_handler],
        EDUCATION:[bio_education_handler, skip_bio_education_handler],
        VIDEO: [video_handler, skip_video_handler]
    },
    fallbacks=[cancel_handler]
)

dispatcher.add_handler(conv_handler)





dispatcher.add_handler(start_handler)

dispatcher.add_handler(gender_handler)
dispatcher.add_handler(photo_handler)
dispatcher.add_handler(skip_photo_handler)
dispatcher.add_handler(bio_handler)
dispatcher.add_handler(skip_bio_handler)
dispatcher.add_handler(bio_years_handler)
dispatcher.add_handler(bio_education_handler)

dispatcher.add_handler(video_handler)
dispatcher.add_handler(skip_video_handler)





updater.start_polling()
updater.idle()