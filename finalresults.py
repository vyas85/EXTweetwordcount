#This script returns the number of occurences of each word in the Tweetwordcount table

import psycopg2
import sys
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")


if len(sys.argv)!=2:
	cur = conn.cursor()
	cur.execute("SELECT word,count from Tweetwordcount")
	result = cur.fetchall()
	
	print sorted(result,key = lambda x:x[1])
	conn.commit()
	conn.close()

else:
	inputWord = sys.argv[1]

	#Select word from table 

	cur = conn.cursor()
	cur.execute("SELECT count from Tweetwordcount where word = '"+inputWord+"'")
	result = cur.fetchall()
	print 'Total number of occurences of "'+inputWord+'": '+str(result[0][0])
	conn.commit()
	conn.close()


