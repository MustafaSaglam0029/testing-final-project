import psycopg2

db_config = {
    "dbname": "mydb",
    "user": "musti",
    "password": "1234",
    "host": "mydb", # name of docker container
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


