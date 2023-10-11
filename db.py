import sqlite3 as sq
import gspread
import pandas as pd
import openpyxl

with (sq.connect("shedule.db") as con):
    cur = con.cursor()

    gc = gspread.service_account(filename='schedule-401419-d4c2eaafc94d.json')
    sh = gc.open('расписание копия')
    wsheet = [sh.worksheet("2 курс"), sh.worksheet("3 курс"), sh.worksheet("4 курс")]
    wsh = sh.sheet1

    group2 = ['E18', 'H18', 'K18']
    day = ['B20', 'B23', 'B24', 'B25', 'B30', 'B32']
    l2 = len(group2)
    ld = len(day)

    #for i in range(0, ld):
    #   res = str(wsheet[0].get(day[i])[0][0])
    #   cur.execute("SELECT day_name FROM day_test WHERE day_name = '" + res + "'")
    #   check = cur.fetchall()
    #   if res == 'Понедельник':
    #       c = 'mo'
    #   elif res == 'Вторник':
    #       c = 'tu'
    #   elif res == 'Среда':
    #       c = 'we'
    #   elif res == 'Четверг':
    #       c = 'th'
    #   elif res == 'Пятница':
    #       c = 'fr'
    #   elif res == 'Суббота':
    #       c = 'su'
    #   if len(check) == 0:
    #       cur.execute("INSERT INTO day_test (id, day_name, day_code) VALUES  (" + str(i + 1) + ", '" + res + "', '" + c + "')")

    #for i in range(0, l2):
    #   res = str(wsheet[0].get(group2[i])[0][0])
    #   c = res[0] + res[1] + res[4]
    #   cur.execute('SELECT id FROM class_test WHERE id = ' + str(i + 1))
    #   check = cur.fetchall()
    #   if len(check) == 0:
    #       cur.execute("INSERT INTO class_test (id, class_name, class_code) VALUES  (" + str(i + 1) + ", '" + res + "', '" + c + "')")

    #for i in range(0, l2):
    #   res = str(wsheet[1].get(group2[i])[0][0])
    #   c = res[0] + res[1] + res[4]
    #   cur.execute('SELECT id FROM class_test WHERE id = ' + str(i + 4))
    #   check = cur.fetchall()
    #   if len(check) == 0:
    #       cur.execute("INSERT INTO class_test (id, class_name, class_code) VALUES  (" + str(i + 4) + ", '" + res + "', '" + c + "')")

    #group4 = ['E18', 'H18']
    #l4 = len(group4)
    #for i in range(0, l4):
    #   res = str(wsheet[2].get(group4[i])[0][0])
    #   c = res[0] + res[1] + res[4]
    #   cur.execute('SELECT id FROM class_test WHERE id = ' + str(i + 7))
    #   check = cur.fetchall()
    #   if len(check) == 0:
    #       cur.execute("INSERT INTO class_test (id, class_name, class_code) VALUES  (" + str(i + 7) + ", '" + res + "', '" + c + "')")

    # time = ['C46', 'C47', 'C48', 'C49', 'C50', 'C51', 'C52', 'C53', 'C28', 'C33']
    # tl = len(time)
    # for i in range(0, tl):
    #   res = str(wsheet[0].get(time[i])[0][0])
    #   cur.execute("SELECT lesson_time FROM lesson_test WHERE lesson_time = '" + res + "'")
    #   check = cur.fetchall()
    #   if len(check) == 0:
    #       cur.execute("INSERT INTO lesson_test (id, lesson_time) VALUES  (" + str(i + 1) + ", '" + res + "')")

    # sub_id = 1
    # t_id = 1
    # type_id = 1

    # for p in range(0, 3):
    #    values_list = wsheet[p].get('E20:E63')
    #   k = len(values_list)

    #   for i in range(0, k):
    #       if len(values_list[i]) != 0:
    #           data = values_list[i][0]
    #           res = data.split('  ')

    #           cur.execute("SELECT subject_name FROM subject_test WHERE subject_name = '" + res[0] + "'")
    #           check = cur.fetchall()
    #           if len(check) == 0:
    #               cur.execute(
    #                   "INSERT INTO subject_test (id, subject_name) VALUES  (" + str(sub_id) + ", '" + res[0] + "')")
    #               sub_id = sub_id + 1

    #           if len(res) > 1:
    #               cur.execute("SELECT type_name FROM type_test WHERE type_name = '" + res[1] + "'")
    #               check = cur.fetchall()
    #               if len(check) == 0:
    #                   cur.execute(
    #                       "INSERT INTO type_test (id, type_name) VALUES  (" + str(type_id) + ", '" + res[1] + "')")
    #                   type_id = type_id + 1

    #               cur.execute("SELECT teacher_name FROM teacher_test WHERE teacher_name = '" + res[2] + "'")
    #               check = cur.fetchall()
    #               if len(check) == 0:
    #                   cur.execute(
    #                       "INSERT INTO teacher_test (id, teacher_name) VALUES  (" + str(t_id) + ", '" + res[2] + "')")
    #                   t_id = t_id + 1

    # r_id = 1
    # for p in range(0, 3):
    #   values_list = wsheet[p].get('F20:F63')
    #   k = len(values_list)
    #
    #   for i in range(0, k):
    #       if len(values_list[i]) != 0:
    #           data = values_list[i][0]
    #           res = data.split('  ')

    #           if len(res) == 2:
    #               if res[1] == 'Л':
    #                   address = 'Львовская, 1В'
    #               if res[1] == 'Р':
    #                   address = 'Родионова, 13б'
    #               cur.execute("SELECT classroom_name, classroom_address FROM classroom_test WHERE classroom_name = '" + res[0] + "' AND classroom_address = '" + address + "'")
    #               check = cur.fetchall()
    #               if len(check) == 0:
    #                   cur.execute(
    #                       "INSERT INTO classroom_test (id, classroom_name, classroom_address) VALUES  (" + str(r_id) + ", '" + res[0] + "', '" + address + "')")
    #                   r_id = r_id + 1
    #           else:
    #               cur.execute("SELECT classroom_name FROM classroom_test WHERE classroom_name = '" + res[0] + "'")
    #               check = cur.fetchall()
    #               if len(check) == 0:
    #                   cur.execute(
    #                       "INSERT INTO classroom_test (id, classroom_name) VALUES  (" + str(
    #                           r_id) + ", '" + res[0] + "')")
    #                   r_id = r_id + 1

    pl = 20
    dn = ['B20', 'B28', 'B33', 'B38', 'B46', 'B55']
    gr = ['E', 'H', 'K']
    gr1 = ['F', 'I', 'L']

    # for i in range(0, 12):

    #    if (pl + i) >= 20 and (pl + i) <= 22:
    #       dw = 'Понедельник'
    #   elif (pl + i) == 23:
    #       dw = 'Вторник'
    #   elif (pl + i) == 24:
    #       dw = 'Среда'
    #   elif (pl + i) >= 25 and (pl + i) <= 29:
    #       dw = 'Четверг'
    #   elif (pl + i) >= 30 and (pl + i) <= 31:
    #       dw = 'Пятница'
    #
    #   n3 = wsheet[0].get('K' + str(pl + i))
    #   if len(n3) > 0:
    #       n2 = wsheet[0].get('C' + str(pl+i))[0][0]
    #       n31 = n3[0][0]
    #       n32 = n31.split('  ')
    #       n4 = wsheet[0].get('L' + str(pl + i))
    #       n41 = n4[0][0]
    #       n42 = n41.split('  ')
    #       if len(n32) >= 3 & len(n42) == 2:
    #           a = [dw, n2, n32[0], n32[1], n32[2], n42[0], n42[1]]
    #           print(a)
    #       elif len(n32) == 1 & len(n42) == 1:
    #           a = [dw, n2, n32[0], n42[0]]
    #           print(a)
    #       elif len(n32) >= 3 & len(n42) == 1:
    #           a = [dw, n2, n32[0], n32[1], n32[2], n42[0]]
    #           print(a)

    # for i in range(0, 24):
    #
    #    if (pl + i) >= 20 and (pl + i) <= 23:
    #       dw = 'Понедельник'
    #   elif (pl + i) >= 24 and (pl + i) <= 26:
    #       dw = 'Вторник'
    #   elif (pl + i) == 27:
    #       dw = 'Среда'
    #   elif (pl + i) == 28:
    #       dw = 'Четверг'
    #   elif (pl + i) >= 29 and (pl + i) <= 34:
    #       dw = 'Пятница'
    #   elif (pl + i) >= 35 and (pl + i) <= 42:
    #       dw = 'Суббота'

    #   n3 = wsheet[1].get('K' + str(pl + i))
    #   if len(n3) > 0:
    #       n2 = wsheet[1].get('C' + str(pl+i))[0][0]
    #       n31 = n3[0][0]
    #       n32 = n31.split('  ')
    #       n4 = wsheet[1].get('L' + str(pl + i))
    #       n41 = n4[0][0]
    #       n42 = n41.split('  ')
    #       if len(n32) >= 3 & len(n42) == 2:
    #           a = [dw, n2, n32[0], n32[1], n32[2], n42[0], n42[1]]
    #           print(a)
    #       elif len(n32) == 1 & len(n42) == 1:
    #           a = [dw, n2, n32[0], n42[0]]
    #           print(a)
    #       elif len(n32) >= 3 & len(n42) == 1:
    #           a = [dw, n2, n32[0], n32[1], n32[2], n42[0]]
    #           print(a)

    # for i in range(0, 14):
    #
    #   if (pl + i) >= 20 and (pl + i) <= 22:
    #      dw = 'Понедельник'
    #   elif (pl + i) >= 23 and (pl + i) <= 25:
    #       dw = 'Вторник'
    #  elif (pl + i) >= 26 and (pl + i) <= 27:
    #       dw = 'Среда'
    #   elif (pl + i) >= 28 and (pl + i) <= 30:
    #       dw = 'Четверг'
    #   elif (pl + i) >= 31 and (pl + i) <= 33:
    #       dw = 'Пятница'
    #
    #   n3 = wsheet[2].get('H' + str(pl + i))
    #   if len(n3) > 0:
    #       n2 = wsheet[2].get('C' + str(pl+i))[0][0]
    #       n31 = n3[0][0]
    #       n32 = n31.split('  ')
    #       n4 = wsheet[2].get('I' + str(pl + i))
    #       n41 = n4[0][0]
    #       n42 = n41.split('  ')
    #       if len(n32) >= 3 & len(n42) == 2:
    #           a = [dw, n2, n32[0], n32[1], n32[2], n42[0], n42[1]]
    #           print(a)
    #       elif len(n32) == 1 & len(n42) == 1:
    #           a = [dw, n2, n32[0], n42[0]]
    #           print(a)
    #       elif len(n32) >= 3 & len(n42) == 1:
    #           a = [dw, n2, n32[0], n32[1], n32[2], n42[0]]
    #           print(a)

    # cur.execute("SELECT * FROM class_test")
    # print(cur.fetchall())

    # cur.execute("SELECT * FROM lesson_test")
    # print(cur.fetchall())

    # cur.execute("SELECT * FROM day_test")
    # print(cur.fetchall())
    con.commit()
