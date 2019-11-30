session_history_table_create = """
    CREATE TABLE IF NOT EXISTS session_history 
    (session_id INT, session_item INT, artist TEXT, song TEXT, length FLOAT, 
    PRIMARY KEY(session_id, session_item))
"""

user_history_table_create = """
    CREATE TABLE IF NOT EXISTS user_history
    (user_id INT, session_id INT, session_item INT, artist TEXT, song TEXT, user TEXT, 
    PRIMARY KEY((user_id), session_id, session_item))
"""

song_history_table_create = """
    CREATE TABLE IF NOT EXISTS song_history
    (song TEXT, user TEXT,
    PRIMARY KEY(song, user))
"""

music_app_keyspace_create = """
    CREATE KEYSPACE IF NOT EXISTS music_app
    WITH REPLICATION =
    { 'class': 'SimpleStrategy', 'replication_factor' : 1}
"""

session_history_insert = """
    INSERT INTO session_history (session_id, session_item, artist, song, length)
    VALUES(%s, %s, %s, %s, %s)
"""

user_history_insert = """
    INSERT INTO user_history (user_id, session_id, session_item, artist, song, user)
    VALUES(%s, %s, %s, %s, %s, %s)
"""

song_history_insert = """
    INSERT INTO song_history (song, user)
    VALUES(%s, %s)
"""

create_table_queries = [session_history_table_create, user_history_table_create, song_history_table_create]
