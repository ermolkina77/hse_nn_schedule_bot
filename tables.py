import sqlite3 as sq

with (sq.connect("shedule.db") as con):
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS day_test(
       id INT PRIMARY KEY,
       day_name TEXT);
    """)
    con.commit()

    cur.execute("""CREATE TABLE IF NOT EXISTS lesson_test(
           id INT PRIMARY KEY,
           lesson_time TEXT);
        """)
    con.commit()

    cur.execute("""CREATE TABLE IF NOT EXISTS subject_test(
           id INT PRIMARY KEY,
           subject_name TEXT);
        """)
    con.commit()

    cur.execute("""CREATE TABLE IF NOT EXISTS type_test(
               id INT PRIMARY KEY,
               type_name TEXT);
            """)
    con.commit()

    cur.execute("""CREATE TABLE IF NOT EXISTS teacher_test(
               id INT PRIMARY KEY,
               teacher_name TEXT);
            """)
    con.commit()

    cur.execute("""CREATE TABLE IF NOT EXISTS classroom_test(
               id INT PRIMARY KEY,
               classroom_name TEXT,
               classroom_address TEXT);
            """)
    cur.execute("""DELETE FROM classroom_test""")
    con.commit()
