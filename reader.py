import csv
import img
import datetime

courses = ['1 курс', '2 курс', '3 курс', '4 курс']
kurs4 = {'4КСК7': 3, '4ПКС8': 5, '4АК4': 7, '4Т7': 9, '4Д2': 11, '4ПП2': 13}
kurs3 = {'3КСК8': 3, '3КСК9': 5, '3ПКС9': 7, '3ПКС10': 9, '3АК6': 11, '3Ф6': 13, '3Т9': 15, '3Т10': 17, '3ОДЛ6': 19, '3ИД1': 21, '3Д3': 23, '3ПП3': 25}
days = {0: 'Понедельник', 1: 'Вторник', 2: 'Среда', 3: 'Четверг', 4: 'Пятница', 5: 'Суббота'}
kurs2 = {'2КСК10': 3, '2КСК11': 5, '2ПКС11': 7, '2ПКС12': 9, '2АК7': 11, '2Ф7': 13, '2Т11': 15, '2Т12': 17, '2ОДЛ7': 19, '2ИД2': 21, '2Д4': 23}
msg = {'text': ''}
msg['text'] = '4ПКС8'
print(msg['text'][0])
xy = [0, 0]
with open('Расписание (4 курс) %s.csv' % (days[0]), newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    shelude = ''
    for row in reader:
        shelude += '%s %s %s %s\n' % (row[1], row[2], row[kurs4[msg['text']]].replace('\n', ' / '), row[kurs4[msg['text']] + 1].replace('\n', ' / '))
       #draw.text(xy, '%s %s %s %s' % (row[1], row[2], row[kurs4[msg['text']]].replace('\n', ' / '), row[kurs4[msg['text']] + 1].replace('\n', ' / ')), (0, 0, 0), font=font)
print(shelude)
img.render([0, 0], shelude, (0, 0, 0))
