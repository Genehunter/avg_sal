import sys
import sqlite3
def get_avg_sal(family):
	connection = sqlite3.connect('survey.db')
	cursor = connection.cursor() # This is running the query for you running the record for you which you run back
	
	sql = "SELECT avg(reading) \
			FROM Person JOIN Survey \
			ON Person.ident = Survey.person\
			WHERE Survey.quant = 'sal'\
			AND Person.family = ?" 
			
			## make sql returns you the avg sal;
	
	cursor.execute(sql, [family])	
	results= cursor.fetchall() ## give a list contains a list of tarpels -- rows of results.
	sal = results[0][0] ## You only interested in the first result.
	
	connection.close()
	return sal

for line in sys.stdin:
	family = line.strip()
	sal = get_avg_sal(family)
	print sal, family ## get rid of white lines
