import sys
import hug
import pymysql
from time import time

@hug.get('/data',examples='year=2017&month=January&state=Telangana&product=Carrot')
def dump_data(year: hug.types.text, month: hug.types.text, state: hug.types.text, product: hug.types.text):
	t = time()

	conn = pymysql.connect(host= "localhost",user="username",passwd="password",db="database_Name")
	x = conn.cursor()

	try:
	   x.execute("""INSERT INTO dump_table VALUES (%s,%s,%s,%s)""",(year, month, state, product))
	   conn.commit()
	except:
	   conn.rollback()

	conn.close()

	sys.stderr.write("Time taken:" + str(round(time()-t, 3)) + "s\n")
	return {"Successfully added to Data base"}