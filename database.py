import sqlite3



def create_table():
    con = sqlite3.connect("user_info.db")
    cur = con.cursor()
    cur.execute("""
    DROP TABLE IF EXISTS user_table
    """)
    cur.execute("""
    CREATE TABLE user_table (
        first_name VARCHAR(30),
        last_name VARCHAR(30),
        title VARCHAR(40),
        age INT,
        nationality VARCHAR(40),
        number_of_courses INT,
        number_of_semesters INT,
        status VARCHAR(40)
    )
    """)
   

    con.commit()# you need to commit the changes
    con.close() #it is a good practice to close a database after using it


def insert_data(first_name, last_name, title, age, nationality, number_of_courses, number_of_semesters, status):
    con = sqlite3.connect("user_info.db")
    cur = con.cursor()
    cur.execute("""
    INSERT INTO user_table(first_name, last_name, title, age, nationality, number_of_courses, number_of_semesters, status)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)

    """,
    (first_name, last_name, title, age, nationality,  number_of_courses, number_of_semesters, status)) 
    
    print(cur.execute("SELECT * FROM user_table").fetchall())
    
    con.commit()
    con.close()
