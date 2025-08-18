import sqlite3
from pprint import pprint
import pandas as pd

db_name = "Tennis.db"


with sqlite3.connect(db_name) as conn:
    
    cursor = conn.cursor()
    cursor.execute("""
    delete from Player where id=1;
    """)

    # result = cursor.fetchall()
    # pprint([cd[0] for cd in cursor.description])
    # pprint(result)

    cursor.close()
    conn.commit()
