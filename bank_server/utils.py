import sqlite3 as sq

def fetch_curr_bal(acc):
	con=sq.connect('socGen')
	cur=con.cursor()
	cur.execute('select balance from details where account=(?)',(acc,))
	res=cur.fetchone()
	return res

def fetch_dues(acc):
	con=sq.connect('socGen')
	cur=con.cursor()
	cur.execute('select dues from details where account=(?)',(acc,))
	res=cur.fetchone()
	return res
