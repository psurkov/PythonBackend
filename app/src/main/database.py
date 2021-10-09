import psycopg2


def execute(command: str, fetch=False):
    conn = psycopg2.connect(dbname='postgres', user='postgres',
                            password='12345', host='localhost')
    cursor = conn.cursor()
    cursor.execute(command)
    res = None
    if fetch:
        res = cursor.fetchall()
    cursor.close()
    conn.commit()
    return res


def init():
    execute('''
                create table tasks(
                    id varchar(50) constraint id primary key,
                    name varchar(50) not null,
                    description varchar(150) not null,
                    original_score real not null,
                    score_after_soft_deadline real not null
                );''')


def clear():
    execute('drop table tasks')
