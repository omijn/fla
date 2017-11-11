import sys
import sqlite3

conn = sqlite3.connect('language/french_words.sqlite')
c = conn.cursor()

genders = {1: "masculine", 2: "feminine", 3: "both masculine and feminine"}

def get_gender(noun):
	n = (noun,)
	c.execute("SELECT gender_id FROM word WHERE word=?", n)
	
	try:
		g = c.fetchone()[0]
		return g
	except Exception as e:
		return 4

if __name__ == '__main__':
	print(get_gender(sys.argv[1]))