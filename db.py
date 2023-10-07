import sqlite3 as sq


with sq.connect("shedule.db") as con:
    cur = con.cursor()


    s = '22ПИ1, Понедельник, Алгоритмы и структуры данных, Лекция'
    q, w, e, r = s.split(', ')
    cur.execute('SELECT class_id FROM class WHERE class_name = "23ПИ1"')
    a = str(cur.fetchone())
    print(a)
    cur.execute('SELECT day_id FROM day WHERE day_name = "Понедельник"')
    b = str(cur.fetchone()[0])
    print(b)
    cur.execute('SELECT subject_id FROM subject WHERE subject_name = "Алгоритмы и структуры данных"')
    c = str(cur.fetchone()[0])
    print(c)
    cur.execute('SELECT type_id FROM type WHERE type_name = "Лекция"')
    d = str(cur.fetchone()[0])
    print(d)
    m = '123'
    cur.execute('UPDATE schedule SET note = ? WHERE class_id = ? AND day_id = ? AND subject_id = ? AND type_id = ?', [m, a, b, c, d])

