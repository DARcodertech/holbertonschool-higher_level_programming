#!/usr/bin/python3
"""
display a value
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
        query = ("SELECT * FROM states WHERE name LIKE BINARY %s "
         "ORDER BY id ASC")
        cursor.execute(query, (sys.argv[4],))
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
