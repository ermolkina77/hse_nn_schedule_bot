import sqlite3 as sq
import gspread
import pandas as pd

with (sq.connect("shedule.db") as con):
    cur = con.cursor()

    gc = gspread.service_account(filename='schedule-401419-d4c2eaafc94d.json')
    sh = gc.open('расписание копия')
    wsheet = [sh.worksheet("2 курс"), sh.worksheet("3 курс"), sh.worksheet("4 курс")]

    group2 = ['E18', 'H18', 'K18']
    day = ['B20', 'B28', 'B33', 'B38', 'B46', 'B55']
    l2 = len(group2)
    ld = len(day)

    for i in range(0, ld):
        res = str(wsheet[0].get(day[i])[0][0])
        cur.execute("SELECT day_name FROM day_test WHERE day_name = '" + res + "'")
        check = cur.fetchall()
        if len(check) == 0:
            cur.execute("INSERT INTO day_test (id, day_name) VALUES  (" + str(i + 1) + ", '" + res + "')")

    for i in range(0, l2):
        res = str(wsheet[0].get(group2[i])[0][0])
        cur.execute('SELECT id FROM class_test WHERE id = ' + str(i + 1))
        check = cur.fetchall()
        if len(check) == 0:
            cur.execute("INSERT INTO class_test (id, class_name) VALUES  (" + str(i + 1) + ", '" + res + "')")

    for i in range(0, l2):
        res = str(wsheet[1].get(group2[i])[0][0])
        cur.execute('SELECT id FROM class_test WHERE id = ' + str(i + 4))
        check = cur.fetchall()
        if len(check) == 0:
            cur.execute("INSERT INTO class_test (id, class_name) VALUES  (" + str(i + 4) + ", '" + res + "')")

    group4 = ['E18', 'H18']
    l4 = len(group4)
    for i in range(0, l4):
        res = str(wsheet[2].get(group4[i])[0][0])
        cur.execute('SELECT id FROM class_test WHERE id = ' + str(i + 7))
        check = cur.fetchall()
        if len(check) == 0:
            cur.execute("INSERT INTO class_test (id, class_name) VALUES  (" + str(i + 7) + ", '" + res + "')")

    time = ['C46', 'C47', 'C48', 'C49', 'C50', 'C51', 'C52', 'C53', 'C28', 'C33']
    tl = len(time)
    for i in range(0, tl):
        res = str(wsheet[0].get(time[i])[0][0])
        cur.execute("SELECT lesson_time FROM lesson_test WHERE lesson_time = '" + res + "'")
        check = cur.fetchall()
        if len(check) == 0:
            cur.execute("INSERT INTO lesson_test (id, lesson_time) VALUES  (" + str(i + 1) + ", '" + res + "')")

    cur.execute("SELECT * FROM class_test")
    print(cur.fetchall())

    cur.execute("SELECT * FROM lesson_test")
    print(cur.fetchall())

    cur.execute("SELECT * FROM day_test")
    print(cur.fetchall())
    con.commit()
