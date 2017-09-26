import sys
import asyncio
import telepot
import telepot.aio
from telepot.aio.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup
import datetime
import config
import img
from openpyxl import load_workbook


def chunks(lst, chunk_count):
    chunk_size = len(lst) // chunk_count
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


async def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, msg['text'], datetime.datetime.fromtimestamp(msg['date']).strftime('%Y-%m-%d %H:%M:%S')
          )
    keyboard_courses = ReplyKeyboardMarkup(keyboard=[
        config.courses
    ], resize_keyboard=True)
    if content_type != 'text':
        return
    if msg['text'].upper() in config.kurs4.keys():
        try:
            wb = load_workbook('xlsx/%s.xlsx' % (config.days[datetime.datetime.today().weekday()]))
            ws = wb['Расписание (%s курс)' % (msg['text'][0])]

            lessons = msg['text'] + '\n'
            aud = '\n'

            for x in range(3, 10):
                if ws.cell(row=x, column=config.kurs4[msg['text']]).value is None:
                    lessons += '\n'
                else:
                    lessons += ws.cell(row=x, column=config.kurs4[msg['text']]).value.replace('\n', ' / ') + '\n'
                if ws.cell(row=x, column=config.kurs4[msg['text']] + 1).value is None:
                    aud += '\n'
                else:
                    aud += ws.cell(row=x, column=config.kurs4[msg['text']] + 1).value.replace('\n', ' / ') + '\n'
            img.render([lessons, aud], (85, 85, 85), chat_id)
            await bot.sendPhoto(chat_id, open('img/%s.png' % chat_id, 'rb'), reply_markup=keyboard_courses)
        except Exception as e:
            print(e)
            await bot.sendMessage(chat_id, text='Расписание не доступно', reply_markup=keyboard_courses)

       # await bot.sendMessage(chat_id, text=lessons, reply_markup=keyboard_courses)
    elif msg['text'].upper() in config.kurs3.keys():
        try:
            wb = load_workbook('xlsx/%s.xlsx' % (config.days[datetime.datetime.today().weekday()]))
            ws = wb['Расписание (%s курс)' % (msg['text'][0])]

            lessons = msg['text'] + '\n'
            aud = '\n'

            for x in range(3, 10):
                if ws.cell(row=x, column=config.kurs3[msg['text']]).value is None:
                    lessons += '\n'
                else:
                    lessons += ws.cell(row=x, column=config.kurs3[msg['text']]).value.replace('\n', ' / ') + '\n'
                if ws.cell(row=x, column=config.kurs3[msg['text']] + 1).value is None:
                    aud += '\n'
                else:
                    aud += ws.cell(row=x, column=config.kurs3[msg['text']] + 1).value.replace('\n', ' / ') + '\n'

            img.render([lessons, aud], (85, 85, 85), chat_id)
            await bot.sendPhoto(chat_id, open('img/%s.png' % chat_id, 'rb'), reply_markup=keyboard_courses)
        except Exception as e:
            print(e)
            await bot.sendMessage(chat_id, text='Расписание не доступно', reply_markup=keyboard_courses)

        # await bot.sendMessage(chat_id, text=shelude, reply_markup=keyboard_courses)

    elif msg['text'].upper() in config.kurs2.keys():
        try:
            wb = load_workbook('xlsx/%s.xlsx' % (config.days[datetime.datetime.today().weekday()]))
            ws = wb['Расписание (%s курс)' % (msg['text'][0])]

            lessons = msg['text'] + '\n'
            aud = '\n'

            for x in range(3, 10):
                if ws.cell(row=x, column=config.kurs2[msg['text']]).value is None:
                    lessons += '\n'
                else:
                    lessons += ws.cell(row=x, column=config.kurs2[msg['text']]).value.replace('\n', ' / ') + '\n'
                if ws.cell(row=x, column=config.kurs2[msg['text']] + 1).value is None:
                    aud += '\n'
                else:
                    aud += ws.cell(row=x, column=config.kurs2[msg['text']] + 1).value.replace('\n', ' / ') + '\n'
            img.render([lessons, aud], (85, 85, 85), chat_id)
            await bot.sendPhoto(chat_id, open('img/%s.png' % chat_id, 'rb'), reply_markup=keyboard_courses)
        except Exception as e:
            print(e)
            await bot.sendMessage(chat_id, text='Расписание не доступно', reply_markup=keyboard_courses)

            # await bot.sendMessage(chat_id, text=shelude, reply_markup=keyboard_courses)

    elif msg['text'].upper() in config.kurs1.keys():
        try:
            wb = load_workbook('xlsx/%s.xlsx' % (config.days[datetime.datetime.today().weekday()]))
            ws = wb['Расписание (%s курс)' % (msg['text'][0])]

            lessons = msg['text'] + '\n'
            aud = '\n'

            for x in range(3, 10):
                if ws.cell(row=x, column=config.kurs1[msg['text']]).value is None:
                    lessons += '\n'
                else:
                    lessons += ws.cell(row=x, column=config.kurs1[msg['text']]).value.replace('\n', ' / ') + '\n'
                if ws.cell(row=x, column=config.kurs1[msg['text']] + 1).value is None:
                    aud += '\n'
                else:
                    aud += ws.cell(row=x, column=config.kurs1[msg['text']] + 1).value.replace('\n', ' / ') + '\n'
            img.render([lessons, aud], (85, 85, 85), chat_id)
            await bot.sendPhoto(chat_id, open('img/%s.png' % chat_id, 'rb'), reply_markup=keyboard_courses)
        except Exception as e:
            print(e)
            await bot.sendMessage(chat_id, text='Расписание не доступно', reply_markup=keyboard_courses)

        # await bot.sendMessage(chat_id, text=shelude, reply_markup=keyboard_courses)

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
