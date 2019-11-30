import pandas as pd
from cassandra.cluster import Cluster
from scripts.csql_queries import *


def insert_data(session, query, df, df_columns):
    for i, row in df.iterrows():
        data = tuple([row[col] for col in df_columns])
        session.execute(query, data)


def main():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('music_app')

    file = 'event_datafile_new.csv'
    df = pd.read_csv(file, encoding='utf8')
    df['user'] = df['firstName'] + ' ' + df['lastName']

    insert_data(session, session_history_insert, df, ['sessionId', 'itemInSession', 'artist', 'song', 'length'])

    insert_data(session, user_history_insert, df, ['userId', 'sessionId', 'itemInSession', 'artist', 'song', 'user'])

    insert_data(session, song_history_insert, df, ['song', 'user'])

    print('Data loaded.')


if __name__ == '__main__':
    main()
