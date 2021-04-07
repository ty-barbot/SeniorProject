import sqlite3

conn = sqlite3.connect('workout.db')

c = conn.cursor("""CREATE TABLE Machines (
                    Name text,
                    Type text,
                    Reps interger               

                    )""")

conn.commit()
conn.close()