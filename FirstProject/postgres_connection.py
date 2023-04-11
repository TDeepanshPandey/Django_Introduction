import psycopg2

conn = psycopg2.connect(host='localhost', dbname='test', user='postgres', password='shree420', port=5432)

cur = conn.cursor()

cur.execute('CREATE TABLE person (id INT primary key, name VARCHAR(255) )')

conn.commit()
cur.close()
conn.close()