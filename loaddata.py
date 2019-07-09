import sqlite3
conn = sqlite3.connect('student.db')
print "Opened database successfully";
c = conn.cursor()
f=open("data.ini",mode="r")
rea=f.readlines()
for re in rea:
        t=re.split(',')
        c.execute("INSERT INTO STUDENT(ID,NAME,AGE,SEXUAL)\
                VALUES(%s,'%s',%s,'%s');"%(int(t[0]),t[1],int(t[2]),t[3]))

conn.commit()
conn.close()
f.close()
