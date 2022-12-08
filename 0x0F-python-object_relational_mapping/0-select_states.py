#!/usr/bin/python3

import MySQLdb
from sys import argv
'''
a script that lists all states
from the database
'''

if __name__ == "__main__":
    '''select all states'''
    con = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        passwd=argv[2], db=argv[3])
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    db = cursor.fetchall()
    for row in db:
        print(row)
    cursor.close()
    con.close()
