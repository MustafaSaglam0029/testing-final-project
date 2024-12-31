import psycopg2

db_config = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "1234",
    "host": "127.0.0.1",
    "port": "5432",
}


def conn():
    connection = psycopg2.connect(**db_config)
    return connection

def select():
    con = conn()
    cur = con.cursor()
    cur.execute("select business_partner_id from mandate where mandate_id = '7' ")
    row = cur.fetchall()
    return row

