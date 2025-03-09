#!/usr/bin/python3
"""
list a state
"""
import MySQLdb
import sys

if __name__ == "__main__":
    try:

        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE name\
        LIKE BINARY 'N%' ORDER BY id ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()
