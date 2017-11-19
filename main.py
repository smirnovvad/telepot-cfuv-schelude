import sys
import asyncio
import telepot.aio
from telepot import glance
from telepot.aio.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from telepot.aio.delegate import (
    per_chat_id, per_callback_query_origin, create_open, pave_event_space)
import datetime
import apsw


def main():

    # ТУТ БУДЕТ НАШ КОД РАБОТЫ С БАЗОЙ ДАННЫХ
    # КОД ДАЛЬНЕЙШИХ ПРИМЕРОВ ВСТАВЛЯТЬ В ЭТО МЕСТО

    # Не забываем закрыть соединение с базой данных

    TOKEN = sys.argv[1]  # get token from command-line

    bot = telepot.aio.DelegatorBot(TOKEN, [
        pave_event_space()(
            per_chat_id(), create_open, AttendanceStarter, timeout=3),
        pave_event_space()(
            per_callback_query_origin(), create_open, Attendance, timeout=60),
    ])

    loop = asyncio.get_event_loop()

    loop.create_task(MessageLoop(bot).run_forever())
    print('Listening ...')

    loop.run_forever()


class AttendanceStarter(telepot.aio.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(AttendanceStarter, self).__init__(*args, **kwargs)

    async def on_chat_message(self, msg):

        content_type, chat_type, chat_id = glance(msg)

        conn = apsw.Connection('test.sqlite')

        cursor = conn.cursor()
        cursor.execute("SELECT name,id_tg,id FROM students")
        res = cursor.fetchall()
        students, id_tg, id_student = zip(*res)
        print(students, id_tg)
        if msg['from']['id'] in id_tg:
            student = [t for t in res if t[1] == msg['from']['id']]
            print(student[0][2])
            cursor.execute("SELECT * FROM attendance WHERE date_pass > date('now','-1 month') and id_student=?", (student[0][2],))
            passes = cursor.fetchall()
            await self.sender.sendMessage(f'У вас {len(passes)} пропуск за месяц')
        elif content_type == 'text' and any(msg['text'] in s for s in students):
            print('Chat:', content_type, chat_type, msg['text'], msg['from'], datetime.datetime.fromtimestamp(msg['date']).strftime('%Y-%m-%d %H:%M:%S'))
            students = [elem for elem in students if msg['text'] in elem]
            await self.sender.sendMessage('Выберите себя', reply_markup=InlineKeyboardMarkup(inline_keyboard=list(map(lambda c: [InlineKeyboardButton(text=str(c), callback_data=str(c))], list(students)))))

        elif content_type == 'text' and msg['text'] not in res:
            print('Chat:', content_type, chat_type, msg['text'], msg['from'], datetime.datetime.fromtimestamp(msg['date']).strftime('%Y-%m-%d %H:%M:%S'))
            await self.sender.sendMessage(
                'Привет, зарегистрирйся для продолжения',
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[[
                        InlineKeyboardButton(text='Регистрация', callback_data='register'),
                    ]]
                )
            )

        cursor.close()
        self.close()


class Attendance(telepot.aio.helper.CallbackQueryOriginHandler):

    def __init__(self, *args, **kwargs):
        super(Attendance, self).__init__(*args, **kwargs)

    async def on_callback_query(self, msg):
        query_id, from_id, query_data = glance(msg, flavor='callback_query')
        self.sender = telepot.aio.helper.Sender(self.bot, from_id)
        print(query_data)

        conn = apsw.Connection('test.sqlite')

        cursor = conn.cursor()
        cursor.execute("SELECT name,id_tg FROM students")
        res = cursor.fetchall()
        print(res)
        students, id_tg = zip(*res)
        if query_data == 'register':
            await self.sender.sendMessage(
                'Напишите свою фамилию')
        if query_data in students:
            cursor.execute("UPDATE `students` SET `id_tg`=? WHERE `name`=?;", (from_id, query_data))
            print(query_data, from_id)
            await self.sender.sendMessage('Отлично, вы зарегистрированы', reply_markup=ReplyKeyboardMarkup(keyboard=[['Мои пропуски']], resize_keyboard=True))
        cursor.close()

    async def on__idle(self, event):
        await asyncio.sleep(5)
        await self.editor.deleteMessage()

        self.close()


def chunks(lst, chunk_count):
    chunk_size = len(lst) // chunk_count
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


if __name__ == '__main__':
    main()
