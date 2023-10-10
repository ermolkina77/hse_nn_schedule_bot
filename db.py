import sqlite3 as sq
import gspread

with (sq.connect("shedule.db") as con):
    cur = con.cursor()

    gc = gspread.service_account(filename='schedule-401419-d4c2eaafc94d.json')
    sh = gc.open('расписание копия')
    wsheet = [sh.worksheet("2 курс"), sh.worksheet("3 курс"), sh.worksheet("4 курс")]

    a1 = ['E18', 'H18', 'K18']
    c1 = len(a1)
    for i in range(0, c1):
        res = str(wsheet[0].get(a1[i])[0][0])
        cur.execute('SELECT id FROM class_test WHERE id = ' + str(i + 1))
        check = cur.fetchall()
        if len(check) == 0:
            cur.execute("INSERT INTO class_test (id, class_name) VALUES  (" + str(i + 1) + ", '" + res + "')")

    for i in range(0, c1):
        res = str(wsheet[1].get(a1[i])[0][0])
        cur.execute('SELECT id FROM class_test WHERE id = ' + str(i + 4))
        check = cur.fetchall()
        if len(check) == 0:
            cur.execute("INSERT INTO class_test (id, class_name) VALUES  (" + str(i + 4) + ", '" + res + "')")

    a2 = ['E18', 'H18']
    c2 = len(a2)
    for i in range(0, c2):
        res = str(wsheet[2].get(a2[i])[0][0])
        cur.execute('SELECT id FROM class_test WHERE id = ' + str(i + 7))
        check = cur.fetchall()
        if len(check) == 0:
            cur.execute("INSERT INTO class_test (id, class_name) VALUES  (" + str(i + 7) + ", '" + res + "')")

    cur.execute("SELECT * FROM class_test")
    print(cur.fetchall())

    con.commit()
