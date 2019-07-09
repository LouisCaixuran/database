import sqlite3

conn = sqlite3.connect('student.db')

print "Opened database successfully";
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS student")

c.execute('''CREATE TABLE student    
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT     NOT NULL,
       AGE            INT      NOT NULL,
       sexual         TEXT     NOT NULL)''')
print "Table created successfully";
conn.commit()

conn.close()

	
