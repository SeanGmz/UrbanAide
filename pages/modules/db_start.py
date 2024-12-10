import sqlite3

def initialize_db():
    conn = sqlite3.connect('urban.db')   
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
        post_status VARCHAR(20) NOT NULL,
        post_author INTEGER NOT NULL,
        FOREIGN KEY (post_author) REFERENCES users (user_id)
    )""")

    # cursor.execute("""
    # CREATE TABLE IF NOT EXISTS comment (
    #     cmt_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     cmt_content TEXT NOT NULL,
    #     cmt_date DATE NOT NULL,
    #     cmt_author INTEGER NOT NULL,
    #     cmt_post INTEGER NOT NULL,
    #     FOREIGN KEY (cmt_author) REFERENCES users (user_id),
    #     FOREIGN KEY (cmt_post) REFERENCES posts (post_id)
    # )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS participation (
        part_id INTEGER PRIMARY KEY AUTOINCREMENT,
        part_user INTEGER NOT NULL,
        part_post INTEGER NOT NULL,
        FOREIGN KEY (part_user) REFERENCES users (user_id),
        FOREIGN KEY (part_post) REFERENCES posts (post_id)
    )""")


    cursor.execute("""
    INSERT INTO users (user_fname, user_lname, user_contact, user_email, user_pass, user_role) VALUES
    ('John', 'Doe', '123', 'johnd123@gmail.com', 'john123', 'non_admin'),
    ('ALexa', 'wiw', '124', 'alexa123@gmail.com', 'alexawiw', 'admin')
    """)
    
      
    cursor.execute("""
    INSERT INTO posts (post_name, post_desc, post_from, post_until, post_location, post_landmark, post_part_count, post_status, post_author) 
    SELECT
    'testpost1' AS post_name, 
    'test post desc1' AS post_desc, 
    '2024-06-06 12:00:00' AS post_from, 
    '2024-07-07 12:00:00' AS post_until, 
    'test location1' AS post_location, 
    'test landmark1' AS post_landmark, 
    0 AS post_part_count, 
    'ongoing' AS post_status, 
    user_fname || ' ' || user_lname AS post_author 
    FROM users 
    WHERE user_role = 'admin'
    """)
    
    cursor.execute("""
    INSERT INTO posts (post_name, post_desc, post_from, post_until, post_location, post_landmark, post_part_count, post_status, post_author) 
    SELECT
    'testpost2' AS post_name, 
    'test post desc2' AS post_desc, 
    '2024-04-04 12:00:00' AS post_from, 
    '2024-08-08 12:00:00' AS post_until, 
    'test location2' AS post_location, 
    'test landmark2' AS post_landmark, 
    12 AS post_part_count, 
    'upcoming' AS post_status, 
    user_fname || ' ' || user_lname AS post_author 
    FROM users 
    WHERE user_role = 'admin'
    """)
    
    cursor.execute("""
    INSERT INTO posts (post_name, post_desc, post_from, post_until, post_location, post_landmark, post_part_count, post_status, post_author) 
    SELECT
    'testpost3' AS post_name, 
    'test post desc3' AS post_desc, 
    '2025-04-04 12:00:00' AS post_from, 
    '2025-08-08 12:00:00' AS post_until, 
    'test location3' AS post_location, 
    'test landmark3' AS post_landmark, 
    199 AS post_part_count, 
    'ongoing' AS post_status, 
    user_fname || ' ' || user_lname AS post_author 
    FROM users 
    WHERE user_role = 'admin'
    """)
    
    conn.commit()
    conn.close()
    
initialize_db()