import telebot
import webbrowser
import sqlite3 as sq

from telebot import types

bot = telebot.TeleBot('6498800576:AAEQZltiZ9HPheX39PXgLmnImqsABhVL-xs')

main_sql = 'SELECT schedule_id, class_name, week_parity, day_name, lesson_start, lesson_end, classroom_number, classroom_address, subject_name, type_name, teacher_name, note FROM schedule JOIN class ON schedule.class_id = class.class_id JOIN week ON schedule.week_id = week.week_id JOIN day ON schedule.day_id = day.day_id JOIN lesson ON schedule.lesson_id = lesson.lesson_id JOIN classroom ON schedule.classroom_id = classroom.classroom_id JOIN subject ON schedule.subject_id = subject.subject_id JOIN type ON schedule.type_id = type.type_id JOIN teacher ON schedule.teacher_id = teacher.teacher_id WHERE schedule.class_id = '
day_sql = ' AND day.day_id ='
pin = '123'


@bot.message_handler(commands=['menu', 'start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    gr1 = types.InlineKeyboardButton('22ПИ1', callback_data='22ПИ1')
    gr2 = types.InlineKeyboardButton('22ПИ2', callback_data='22ПИ2')
    gr3 = types.InlineKeyboardButton('22ПИ3', callback_data='22ПИ3')
    markup.row(gr1, gr2, gr3)
    gr4 = types.InlineKeyboardButton('21ПИ1', callback_data='21ПИ1')
    gr5 = types.InlineKeyboardButton('21ПИ2', callback_data='21ПИ2')
    gr6 = types.InlineKeyboardButton('21ПИ3', callback_data='21ПИ3')
    markup.row(gr4, gr5, gr6)
    gr7 = types.InlineKeyboardButton('20ПИ1', callback_data='20ПИ1')
    gr8 = types.InlineKeyboardButton('20ПИ2', callback_data='20ПИ2')
    markup.row(gr7, gr8)
    gr9 = types.InlineKeyboardButton('Ссылка на расписание в "Таблицах"',
                                     url='https://docs.google.com/spreadsheets/d/1Iyyqs-DqTkhnoMRbpdyXK1lzF4waM05MzwDCzwWPC4A/edit#gid=0')
    markup.row(gr9)
    gr10 = types.InlineKeyboardButton('Календарь четности недель', callback_data='calendar')
    markup.row(gr10)
    gr11 = types.InlineKeyboardButton('Расписание времни пар', callback_data='time')
    markup.row(gr11)
    gr12 = types.InlineKeyboardButton('Изменить заметку', callback_data='note')
    markup.row(gr12)
    markup.add()
    bot.send_message(message.chat.id,
                     f'Доброго времени суток, {message.from_user.first_name}\nДля доступа к расписанию выбери <b>группу</b>',
                     parse_mode='html', reply_markup=markup)

    @bot.callback_query_handler(func=lambda callback: True)
    def callback_message(callback):
        if callback.data == 'calendar':
            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute("SELECT parity_name, parity_weeks FROM week_info")
            parity = cur.fetchall()
            info = ''
            for row in parity:
                info += f'{row[0]}: {row[1]}\n'
            bot.send_message(message.chat.id, text=info)

        elif callback.data == 'time':
            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute("SELECT lesson_id, lesson_start, lesson_end FROM lesson WHERE lesson_id < 9")
            lesson = cur.fetchall()
            info = ''
            for row in lesson:
                info += f'{row[0]} пара: с {row[1]} по {row[2]}\n'
            bot.send_message(message.chat.id, text=info)

        elif callback.data == '22ПИ1':

            markup = types.InlineKeyboardMarkup()
            dw1 = types.InlineKeyboardButton('Понедельник', callback_data='Monday221')
            dw2 = types.InlineKeyboardButton('Вторник', callback_data='Tuesday221')
            dw3 = types.InlineKeyboardButton('Среда', callback_data='Wednesday221')
            markup.row(dw1, dw2, dw3)
            dw4 = types.InlineKeyboardButton('Четверг', callback_data='Thursday221')
            dw5 = types.InlineKeyboardButton('Пятница', callback_data='Friday221')
            dw6 = types.InlineKeyboardButton('Вся неделя', callback_data='Week221')
            markup.row(dw4, dw5, dw6)
            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Выберите день недели', reply_markup=markup)

        elif callback.data == 'Monday221':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(1) + day_sql + str(1))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на понедельник')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Tuesday221':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(1) + day_sql + str(2))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на вторник')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Wednesday221':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(1) + day_sql + str(3))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на среду')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Thursday221':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(1) + day_sql + str(4))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на четверг')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Friday221':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(1) + day_sql + str(5))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на пятницу')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Week221':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(1))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на всю неделю')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == '22ПИ2':

            markup = types.InlineKeyboardMarkup()
            dw1 = types.InlineKeyboardButton('Понедельник', callback_data='Monday222')
            dw2 = types.InlineKeyboardButton('Вторник', callback_data='Tuesday222')
            dw3 = types.InlineKeyboardButton('Среда', callback_data='Wednesday222')
            markup.row(dw1, dw2, dw3)
            dw4 = types.InlineKeyboardButton('Четверг', callback_data='Thursday222')
            dw5 = types.InlineKeyboardButton('Пятница', callback_data='Friday222')
            dw6 = types.InlineKeyboardButton('Вся неделя', callback_data='Week222')
            markup.row(dw4, dw5, dw6)
            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Выберите день недели', reply_markup=markup)

        elif callback.data == 'Monday222':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(2) + day_sql + str(1))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на понедельник')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Tuesday222':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(2) + day_sql + str(2))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на вторник')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Wednesday222':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(2) + day_sql + str(3))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на среду')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Thursday222':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(2) + day_sql + str(4))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на четверг')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Friday222':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(2) + day_sql + str(5))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на пятницу')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Week222':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(2))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на всю неделю')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == '22ПИ3':

            markup = types.InlineKeyboardMarkup()
            dw1 = types.InlineKeyboardButton('Понедельник', callback_data='Monday223')
            dw2 = types.InlineKeyboardButton('Вторник', callback_data='Tuesday223')
            dw3 = types.InlineKeyboardButton('Среда', callback_data='Wednesday223')
            markup.row(dw1, dw2, dw3)
            dw4 = types.InlineKeyboardButton('Четверг', callback_data='Thursday223')
            dw5 = types.InlineKeyboardButton('Пятница', callback_data='Friday223')
            dw6 = types.InlineKeyboardButton('Вся неделя', callback_data='Week223')
            markup.row(dw4, dw5, dw6)
            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Выберите день недели', reply_markup=markup)

        elif callback.data == 'Monday223':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(3) + day_sql + str(1))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на понедельник')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Tuesday223':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(3) + day_sql + str(2))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на вторник')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Wednesday223':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(3) + day_sql + str(3))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на среду')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Thursday223':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(3) + day_sql + str(4))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на четверг')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Friday223':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(3) + day_sql + str(5))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на пятницу')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Week223':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(3))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на всю неделю')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == '21ПИ1':

            markup = types.InlineKeyboardMarkup()
            dw1 = types.InlineKeyboardButton('Понедельник', callback_data='Monday211')
            dw2 = types.InlineKeyboardButton('Вторник', callback_data='Tuesday211')
            dw3 = types.InlineKeyboardButton('Среда', callback_data='Wednesday211')
            markup.row(dw1, dw2, dw3)
            dw4 = types.InlineKeyboardButton('Четверг', callback_data='Thursday211')
            dw5 = types.InlineKeyboardButton('Пятница', callback_data='Friday211')
            dw6 = types.InlineKeyboardButton('Суббота', callback_data='Saturday211')
            markup.row(dw4, dw5, dw6)
            dw7 = types.InlineKeyboardButton('Вся неделя', callback_data='Week211')
            markup.row(dw7)
            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Выберите день недели', reply_markup=markup)

        elif callback.data == 'Monday211':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(4) + day_sql + str(1))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на понедельник')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Tuesday211':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(4) + day_sql + str(2))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на вторник')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Wednesday211':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(4) + day_sql + str(3))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на среду')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Thursday211':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(4) + day_sql + str(4))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на четверг')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Friday211':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(4) + day_sql + str(5))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на пятницу')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Saturday211':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(4) + day_sql + str(6))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на субботу')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Week211':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(4))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на всю неделю')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == '21ПИ2':

            markup = types.InlineKeyboardMarkup()
            dw1 = types.InlineKeyboardButton('Понедельник', callback_data='Monday212')
            dw2 = types.InlineKeyboardButton('Вторник', callback_data='Tuesday212')
            dw3 = types.InlineKeyboardButton('Среда', callback_data='Wednesday212')
            markup.row(dw1, dw2, dw3)
            dw4 = types.InlineKeyboardButton('Четверг', callback_data='Thursday212')
            dw5 = types.InlineKeyboardButton('Пятница', callback_data='Friday212')
            dw6 = types.InlineKeyboardButton('Суббота', callback_data='Saturday212')
            markup.row(dw4, dw5, dw6)
            dw7 = types.InlineKeyboardButton('Вся неделя', callback_data='Week212')
            markup.row(dw7)
            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Выберите день недели', reply_markup=markup)

        elif callback.data == 'Monday212':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(5) + day_sql + str(1))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на понедельник')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Tuesday212':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(5) + day_sql + str(2))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на вторник')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Wednesday212':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(5) + day_sql + str(3))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на среду')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Thursday212':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(5) + day_sql + str(4))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на четверг')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Friday212':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(5) + day_sql + str(5))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на пятницу')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Week212':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(5))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на всю неделю')
            bot.send_message(message.chat.id, info, parse_mode='html')


        elif callback.data == '21ПИ3':

            markup = types.InlineKeyboardMarkup()
            dw1 = types.InlineKeyboardButton('Понедельник', callback_data='Monday213')
            dw2 = types.InlineKeyboardButton('Вторник', callback_data='Tuesday213')
            dw3 = types.InlineKeyboardButton('Среда', callback_data='Wednesday213')
            markup.row(dw1, dw2, dw3)
            dw4 = types.InlineKeyboardButton('Четверг', callback_data='Thursday213')
            dw5 = types.InlineKeyboardButton('Пятница', callback_data='Friday213')
            dw6 = types.InlineKeyboardButton('Суббота', callback_data='Saturday213')
            markup.row(dw4, dw5, dw6)
            dw7 = types.InlineKeyboardButton('Вся неделя', callback_data='Week213')
            markup.row(dw7)
            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Выберите день недели', reply_markup=markup)

        elif callback.data == 'Monday213':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(6) + day_sql + str(1))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на понедельник')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Tuesday213':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(6) + day_sql + str(2))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на вторник')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Wednesday213':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(6) + day_sql + str(3))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на среду')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Thursday213':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(6) + day_sql + str(4))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на четверг')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Friday213':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(6) + day_sql + str(5))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на пятницу')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Week213':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(6))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на всю неделю')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == '20ПИ1':

            markup = types.InlineKeyboardMarkup()
            dw1 = types.InlineKeyboardButton('Понедельник', callback_data='Monday201')
            dw2 = types.InlineKeyboardButton('Среда', callback_data='Wednesday201')
            markup.row(dw1, dw2)
            dw3 = types.InlineKeyboardButton('Пятница', callback_data='Friday201')
            dw4 = types.InlineKeyboardButton('Вся неделя', callback_data='Week201')
            markup.row(dw3, dw4)
            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Выберите день недели', reply_markup=markup)

        elif callback.data == 'Monday201':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(7) + day_sql + str(1))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на понедельник')
            bot.send_message(message.chat.id, info, parse_mode='html')



        elif callback.data == 'Wednesday201':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(7) + day_sql + str(3))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на среду')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Friday201':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(7) + day_sql + str(5))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на пятницу')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Week201':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(7))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на всю неделю')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == '20ПИ2':

            markup = types.InlineKeyboardMarkup()
            dw1 = types.InlineKeyboardButton('Понедельник', callback_data='Monday202')
            dw2 = types.InlineKeyboardButton('Среда', callback_data='Wednesday202')
            markup.row(dw1, dw2)
            dw3 = types.InlineKeyboardButton('Пятница', callback_data='Friday202')
            dw4 = types.InlineKeyboardButton('Вся неделя', callback_data='Week202')
            markup.row(dw3, dw4)
            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Выберите день недели', reply_markup=markup)

        elif callback.data == 'Monday202':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(8) + day_sql + str(1))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на понедельник')
            bot.send_message(message.chat.id, info, parse_mode='html')



        elif callback.data == 'Wednesday202':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(8) + day_sql + str(3))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на среду')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Friday202':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(8) + day_sql + str(5))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на пятницу')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'Week202':

            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute(main_sql + str(8))
            pi221 = cur.fetchall()
            info = ''
            for row in pi221:
                info += f'Группа: {row[1]}\nНеделя: {row[2]}\nДень: {row[3]}\nВремя пары: <b><i>с {row[4]} по {row[5]}</i></b>\nАудитория: <b><i>{row[6]}, {row[7]}</i></b>\nДисциплина: <b><i>{row[8]} — {row[9]}</i></b>\nПреподаватель: {row[10]}\nЗаметка: {row[11]}\n\n'

            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='Ваше расписание на всю неделю')
            bot.send_message(message.chat.id, info, parse_mode='html')

        elif callback.data == 'note':
            msg = bot.send_message(message.chat.id, 'Введите пин')
            bot.register_next_step_handler(msg, get_user_pin)

    def get_user_pin(message):
        user_pin = message.text
        if user_pin == '123':
            msg = bot.send_message(message.chat.id, 'Введите группу, буквы заглавные (Например: 20ПИ2)')
            bot.register_next_step_handler(msg, get_group)
        else:
            bot.send_message(message.chat.id, 'Неверный пин')

    def get_group(message):
        try:
            class_name = message.text
            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute('SELECT class_id FROM class WHERE class_name = "' + class_name + '"')
            class_id = str(cur.fetchone()[0])

            msg = bot.send_message(message.chat.id, 'Введите день недели с заглавной буквы (Например: Понедельник)')
            bot.register_next_step_handler(msg, get_day, class_id)
        except Exception:
            bot.send_message(message.chat.id, 'Что-то не так, проверь правильное написание в самом расписании')
            return start(message)

    def get_day(message, class_id):
        try:
            day_name = message.text
            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute('SELECT day_id FROM day WHERE day_name = "' + day_name +'"')
            day_id = str(cur.fetchone()[0])

            msg = bot.send_message(message.chat.id, 'Введите дисциплину, как в боте, с заглавной буквы(Например: Алгоритмы и структуры данных)')
            bot.register_next_step_handler(msg, get_type, class_id, day_id)

        except Exception:
            bot.send_message(message.chat.id, 'Что-то не так, проверь правильное написание в самом расписании')
            return start(message)

    def get_type(message, class_id, day_id):
        try:
            subject_name = message.text
            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute('SELECT subject_id FROM subject WHERE subject_name = "' + subject_name + '"')
            subject_id = str(cur.fetchone()[0])

            msg = bot.send_message(message.chat.id, 'Введите тип с заглавной буквы или "Не имеет значения" ')
            bot.register_next_step_handler(msg, get_note, class_id, day_id, subject_id)

        except Exception:
            bot.send_message(message.chat.id, 'Что-то не так, проверь правильное написание в самом расписании')
            return start(message)

    def get_note(message, class_id, day_id, subject_id):
        try:
            type_name = message.text
            with sq.connect("shedule.db") as con:
                cur = con.cursor()
            cur.execute('SELECT type_id FROM type WHERE type_name = "' + type_name + '"')
            type_id = str(cur.fetchone()[0])

            msg = bot.send_message(message.chat.id,'Введите новую заметку')
            bot.register_next_step_handler(msg, make_note, class_id, day_id, subject_id, type_id)

        except Exception:
            bot.send_message(message.chat.id, 'Что-то не так, проверь правильное написание в самом расписании')
            return start(message)

    def make_note(message, class_id, day_id, subject_id, type_id):
        msg_name = message.text
        with sq.connect("shedule.db") as con:
            cur = con.cursor()
            cur.execute('UPDATE schedule SET note = ? WHERE class_id = ? AND day_id = ? AND subject_id = ? AND type_id = ?', [msg_name, class_id, day_id, subject_id, type_id])
            con.commit

        bot.send_message(message.chat.id, 'Заметка добавлена')

bot.polling(none_stop=True)
