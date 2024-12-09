import sqlite3

def initialize_db():
    conn = sqlite3.connect('urbanaid_db.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_fname VARCHAR(50) NOT NULL,
            user_lname VARCHAR(50) NOT NULL,
            user_contact INTEGER(11) NOT NULL,
            user_email VARCHAR(50) NOT NULL,
            user_pass VARCHAR(20) NOT NULL,
            user_role VARCHAR(20) NOT NULL
        )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        post_id INTEGER PRIMARY KEY AUTOINCREMENT,
        post_name VARCHAR(100) NOT NULL,
        post_desc TEXT NOT NULL,
        post_from DATE NOT NULL,
        post_until DATE NOT NULL,
        post_location TEXT NOT NULL,
        post_landmark TEXT,
        post_part_count INTEGER NOT NULL DEFAULT 0,  
        post_cmt_count INTEGER NOT NULL DEFAULT 0,
        post_status VARCHAR(20) NOT NULL,
        post_author INTEGER NOT NULL,
        FOREIGN KEY (post_author) REFERENCES users (user_id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS comment (
        cmt_id INTEGER PRIMARY KEY AUTOINCREMENT,
        cmt_content TEXT NOT NULL,
        cmt_date DATE NOT NULL,
        cmt_author INTEGER NOT NULL,
        cmt_post INTEGER NOT NULL,
        FOREIGN KEY (cmt_author) REFERENCES users (user_id),
        FOREIGN KEY (cmt_post) REFERENCES posts (post_id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS participation (
        part_id INTEGER PRIMARY KEY AUTOINCREMENT,
        part_user INTEGER NOT NULL,
        part_post INTEGER NOT NULL,
        FOREIGN KEY (part_user) REFERENCES users (user_id),
        FOREIGN KEY (part_post) REFERENCES posts (post_id)
    )""")



    conn.commit()
    conn.close()