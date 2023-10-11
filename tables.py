import sqlite3 as sq

with (sq.connect("shedule.db") as con):
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS day_test(
       id INT PRIMARY KEY,
       day_name TEXT,
       day_code TEXT);
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

    cur.execute("""CREATE TABLE IF NOT EXISTS class_test(
                   id INT PRIMARY KEY,
                   class_name TEXT,
                   class_code TEXT);
                """)

    cur.execute("""CREATE TABLE IF NOT EXISTS schedule_test(
                   id TEXT PRIMARY KEY,
                   class_id INT,
                   day_id INT,
                   lesson_id INT,
                   classroom_id INT,
                   subject_id INT,
                   type_id INT,
                   teacher_id INT,
                   status TEXT,
                   note TEXT);
                """)
    con.commit()


