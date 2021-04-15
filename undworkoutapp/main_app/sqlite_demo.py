import sqlite3

conn = sqlite3.connect('workout.db')

c = conn.cursor("""CREATE TABLE Machines (
                    Name text,
                    Type text,
                    Reps integer               

                    )""")

conn.commit()
conn.close()