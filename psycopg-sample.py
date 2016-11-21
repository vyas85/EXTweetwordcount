#Connecting to the database (if the database doesn't exist, this command will create it)
import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

#Create a Table
#The first step is to create a cursor.
#Next, the cursor executes a create statement to create the appropriate table 

cur = conn.cursor()
cur.execute('''CREATE TABLE Tweetwordcount
       (word TEXT PRIMARY KEY     NOT NULL,
       count INT     NOT NULL);''')
conn.commit()
conn.close()


