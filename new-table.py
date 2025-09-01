# code to create new table

import sqlite3

# connect to SQLite database
conn = sqlite3.connect("pipeline-data.db")
cursor = conn.cursor()

# if table exists drop it, else create a table
cursor.execute("DROP TABLE IF EXISTS PIPELINE")
cursor.execute("CREATE TABLE IF NOT EXISTS PIPELINE(TIME REAL, FLOW REAL, PRESSURE REAL, LEAKED TEXT)")

# commit changes and close connection
conn.commit()
conn.close()