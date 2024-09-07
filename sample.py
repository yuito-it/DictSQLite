import dict_sqlite

db = dict_sqlite.DictSQLite("./sample.db")
db.clear_db()
print(db)
db.create_table("main", schema="(key TEXT PRIMARY KEY, value TEXT)")
db.execute_custom('''
INSERT INTO main (key, value)
VALUES (?, ?)
''', ("John Doe", 30))
print(db)
db.close()
