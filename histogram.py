#This script returns the number of occurences of each word in the Tweetwordcount table

import psycopg2
import sys
#import matplotlib.pyplot as plt

args = sys.argv[1].split(',')
startCount = args[0]
endCount = args[1]

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

#Select word from table 

cur = conn.cursor()
cur.execute("SELECT word,count from Tweetwordcount where count between "+startCount+" and "+endCount)
result = cur.fetchall()

for item in result:
	print item[0]+':',item[1]

conn.commit()
conn.close()




