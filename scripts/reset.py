from app.db import get_database_connection

conn = get_database_connection()
cursor = conn.cursor()

cursor.execute("DELETE FROM tasks;")
cursor.execute("DELETE FROM users;")

conn.commit()
conn.close()
