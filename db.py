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
    day = ['B20', 'B28', 'B33', 'B38', 'B46', 'B55']
    l2 = len(group2)
    ld = len(day)

    #    for i in range(0, ld):
    #    res = str(wsheet[0].get(day[i])[0][0])
    #    cur.execute("SELECT day_name FROM day_test WHERE day_name = '" + res + "'")
    #    check = cur.fetchall()
    #    if len(check) == 0:
    #        cur.execute("INSERT INTO day_test (id, day_name) VALUES  (" + str(i + 1) + ", '" + res + "')")

    #   for i in range(0, l2):
    #   res = str(wsheet[0].get(group2[i])[0][0])
    #   cur.execute('SELECT id FROM class_test WHERE id = ' + str(i + 1))
    #   check = cur.fetchall()
    #   if len(check) == 0:
    #       cur.execute("INSERT INTO class_test (id, class_name) VALUES  (" + str(i + 1) + ", '" + res + "')")

    # for i in range(0, l2):
    #   res = str(wsheet[1].get(group2[i])[0][0])
    #   cur.execute('SELECT id FROM class_test WHERE id = ' + str(i + 4))
    #   check = cur.fetchall()
    #   if len(check) == 0:
    #       cur.execute("INSERT INTO class_test (id, class_name) VALUES  (" + str(i + 4) + ", '" + res + "')")

    # group4 = ['E18', 'H18']
    # l4 = len(group4)
    # for i in range(0, l4):
    #   res = str(wsheet[2].get(group4[i])[0][0])
    #   cur.execute('SELECT id FROM class_test WHERE id = ' + str(i + 7))
    #   check = cur.fetchall()
    #   if len(check) == 0:
    #       cur.execute("INSERT INTO class_test (id, class_name) VALUES  (" + str(i + 7) + ", '" + res + "')")

    # time = ['C46', 'C47', 'C48', 'C49', 'C50', 'C51', 'C52', 'C53', 'C28', 'C33']
    # tl = len(time)
    # for i in range(0, tl):
    #   res = str(wsheet[0].get(time[i])[0][0])
    #   cur.execute("SELECT lesson_time FROM lesson_test WHERE lesson_time = '" + res + "'")
    #   check = cur.fetchall()
    #   if len(check) == 0:
    #       cur.execute("INSERT INTO lesson_test (id, lesson_time) VALUES  (" + str(i + 1) + ", '" + res + "')")

    sub_id = 1
    t_id = 1
    type_id = 1

    for p in range(0, 3):
        values_list = wsheet[p].get('E20:E63')
        k = len(values_list)

        for i in range(0, k):
            if len(values_list[i]) != 0:
                data = values_list[i][0]
                res = data.split('  ')

                cur.execute("SELECT subject_name FROM subject_test WHERE subject_name = '" + res[0] + "'")
                check = cur.fetchall()
                if len(check) == 0:
                    cur.execute(
                        "INSERT INTO subject_test (id, subject_name) VALUES  (" + str(sub_id) + ", '" + res[0] + "')")
                    sub_id = sub_id + 1

                if len(res) > 1:
                    cur.execute("SELECT type_name FROM type_test WHERE type_name = '" + res[1] + "'")
                    check = cur.fetchall()
                    if len(check) == 0:
                        cur.execute(
                            "INSERT INTO type_test (id, type_name) VALUES  (" + str(type_id) + ", '" + res[1] + "')")
                        type_id = type_id + 1

                    cur.execute("SELECT teacher_name FROM teacher_test WHERE teacher_name = '" + res[2] + "'")
                    check = cur.fetchall()
                    if len(check) == 0:
                        cur.execute(
                            "INSERT INTO teacher_test (id, teacher_name) VALUES  (" + str(t_id) + ", '" + res[2] + "')")
                        t_id = t_id + 1

    r_id = 1
    for p in range(0, 3):
        values_list = wsheet[p].get('F20:F63')
        k = len(values_list)

        for i in range(0, k):
            if len(values_list[i]) != 0:
                data = values_list[i][0]
                res = data.split('  ')

                if len(res) == 2:
                    if res[1] == 'Л':
                        address = 'Львовская, 1В'
                    if res[1] == 'Р':
                        address = 'Родионова, 13б'
                    cur.execute("SELECT classroom_name, classroom_address FROM classroom_test WHERE classroom_name = '" + res[0] + "' AND classroom_address = '" + address + "'")
                    check = cur.fetchall()
                    if len(check) == 0:
                        cur.execute(
                            "INSERT INTO classroom_test (id, classroom_name, classroom_address) VALUES  (" + str(r_id) + ", '" + res[0] + "', '" + address + "')")
                        r_id = r_id + 1
                else:
                    cur.execute("SELECT classroom_name FROM classroom_test WHERE classroom_name = '" + res[0] + "'")
                    check = cur.fetchall()
                    if len(check) == 0:
                        cur.execute(
                            "INSERT INTO classroom_test (id, classroom_name) VALUES  (" + str(
                                r_id) + ", '" + res[0] + "')")
                        r_id = r_id + 1

    # cur.execute("SELECT * FROM class_test")
    # print(cur.fetchall())

    # cur.execute("SELECT * FROM lesson_test")
    # print(cur.fetchall())

    # cur.execute("SELECT * FROM day_test")
    # print(cur.fetchall())
    con.commit()
