import sys
import asyncio
import telepot
import telepot.aio
from telepot.aio.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup
import csv
import datetime
import config
import img


def chunks(lst, chunk_count):
    chunk_size = len(lst) // chunk_count
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


async def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, chat_id)
    keyboard_courses = ReplyKeyboardMarkup(keyboard=[
        config.courses
    ], resize_keyboard=True)
    if content_type != 'text':
        return
    if msg['text'].upper() in config.kurs4.keys():
        with open('Расписание (4 курс) %s.csv' % (config.days[datetime.datetime.today().weekday()]), newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            shelude = 'День недели: %s\n' % (config.days[datetime.datetime.today().weekday()])
            for row in reader:
                shelude += '%s %s %s %s\n' % (row[1], row[2], row[config.kurs4[msg['text']]].replace('\n', ' / '), row[config.kurs4[msg['text']] + 1].replace('\n', ' / '))
            img.render([0, 0], shelude, (0, 0, 0), chat_id)
        await bot.sendPhoto(chat_id, open('img/%s.png' % chat_id, 'rb'))
        await bot.sendMessage(chat_id, text=shelude, reply_markup=keyboard_courses)
    elif msg['text'].upper() in config.kurs3.keys():
        with open('Расписание (3 курс) %s.csv' % (config.days[datetime.datetime.today().weekday()]), newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            shelude = ''
            for row in reader:
                shelude += '%s %s %s %s\n' % (row[1], row[2], row[config.kurs3[msg['text']]].replace('\n', ' / '), row[config.kurs3[msg['text']] + 1].replace('\n', ' / '))
            img.render([0, 0], shelude, (0, 0, 0), chat_id)
        await bot.sendPhoto(chat_id, open('img/%s.png' % chat_id, 'rb'))
        await bot.sendMessage(chat_id, text=shelude, reply_markup=keyboard_courses)

    elif msg['text'].upper() in config.kurs2.keys():
        with open('Расписание (2 курс) %s.csv' % (config.days[datetime.datetime.today().weekday()]), newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            shelude = ''
            for row in reader:
                shelude += '%s %s %s %s\n' % (row[1], row[2], row[config.kurs2[msg['text']]].replace('\n', ' / '), row[config.kurs2[msg['text']] + 1].replace('\n', ' / '))
            img.render([0, 0], shelude, (0, 0, 0), chat_id)
        await bot.sendPhoto(chat_id, open('img/%s.png' % chat_id, 'rb'))
        await bot.sendMessage(chat_id, text=shelude, reply_markup=keyboard_courses)

    elif msg['text'].upper() in config.kurs1.keys():
        with open('Расписание (1 курс) %s.csv' % (config.days[datetime.datetime.today().weekday()]), newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            shelude = ''
            for row in reader:
                shelude += '%s %s %s %s\n' % (row[1], row[2], row[config.kurs1[msg['text']]].replace('\n', ' / '), row[config.kurs1[msg['text']] + 1].replace('\n', ' / '))
            img.render([0, 0], shelude, (0, 0, 0), chat_id)
        await bot.sendPhoto(chat_id, open('img/%s.png' % chat_id, 'rb'))
        await bot.sendMessage(chat_id, text=shelude, reply_markup=keyboard_courses)

    elif msg['text'] in config.courses:
        if msg['text'] == '4 курс':
            keyboard = ReplyKeyboardMarkup(keyboard=chunks(list(config.kurs4.keys()), 3), resize_keyboard=True)
            await bot.sendMessage(chat_id, text='Выбери группу', reply_markup=keyboard)

        elif msg['text'] == '3 курс':
            '''
            keyboard = ReplyKeyboardMarkup(keyboard=[
                list(config.kurs3.keys())[:6], list(config.kurs3.keys())[6:]
            ], resize_keyboard=True)
            '''
            keyboard = ReplyKeyboardMarkup(keyboard=chunks(list(config.kurs3.keys()), 3), resize_keyboard=True)
            await bot.sendMessage(chat_id, text='Выбери группу', reply_markup=keyboard)
        elif msg['text'] == '2 курс':
            keyboard = ReplyKeyboardMarkup(keyboard=chunks(list(config.kurs2.keys()), 3), resize_keyboard=True)
            await bot.sendMessage(chat_id, text='Выбери группу', reply_markup=keyboard)
        elif msg['text'] == '1 курс':
            keyboard = ReplyKeyboardMarkup(keyboard=chunks(list(config.kurs1.keys()), 3), resize_keyboard=True)
            await bot.sendMessage(chat_id, text='Выбери группу', reply_markup=keyboard)
    else:
        await bot.sendMessage(chat_id, text='Выбери курс или напиши группу', reply_markup=keyboard_courses)

'''
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Press me', callback_data='4')],
    ])

    bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard)
'''

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.aio.Bot(TOKEN)

loop = asyncio.get_event_loop()

loop.create_task(MessageLoop(bot, {'chat': on_chat_message, }).run_forever())
print('Listening ...')

loop.run_forever()
