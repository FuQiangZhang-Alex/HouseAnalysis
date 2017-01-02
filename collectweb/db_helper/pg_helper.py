from pg import DB


db = DB(dbname='datalab', host='127.0.0.1', port=5432, user='fqzhang', passwd='dont4get')
version = db.query('select version()')
print(version)

def insert(tb_name, row_dict):
	rs = db.insert(table=tb_name, row=row_dict)
	return rs

def  upsert(tb_name, row_dict):
	# if existed
	db.upsert(table=tb_name, row=row_dict)
