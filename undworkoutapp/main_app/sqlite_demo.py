#import sqlite3

#conn = sqlite3.connect('workout.db')

#c = conn.cursor("""CREATE TABLE Machines (
#                    Name text,
#                    Type text,
#                    Sets integer,
#                    Reps integer
#                    )""")

# USE THIS EXECTURE TO CREATE TABLES WITHIN THE DATABASE
# DO NOT USE THE WEBSITE AS IT STRUCTURES IT DIFFERENTLY WITH ITS API
#
#c.execute("INSERT INTO Machines VALUES('NAME_TEST','TYPE_TEST',3,10)")


# HERE IS THE COMMAND FOR FINDING CERTAIN ITEMS WITHIN
# THE TERMINAL, SIMILAR TO PULLING DJANGO MODLES
#
#c.execute("SELECT * FROM Machines WHERE Reps = 3")
#c.execute("SELECT * FROM Machines WHERE Name = 'INSERT_WORKOUT_NAME'")

# this returns the NEXT row after results
#c.fetchone()

# this will return the next rows of N after results as a list
#c.fetchmany(N)

# this will return ALL the rows after results as a list
#c.fetchall()

### this is a test strictly for the in app terminal ###

#print(c.fetchmany(5))
# result is 6 rows, first workout followed by the next 5


#conn.commit()
#conn.close()