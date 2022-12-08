#!/usr/bin/python3
'''./4_cities_states.py root root hbtn_0e_0_usa'''
import MySQLdb
from sys import argv

'''
lists all states with starting name with N
from the database hbtn_0e_0_usa
'''
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
    FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
