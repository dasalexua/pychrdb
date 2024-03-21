import os
import re


def build_quotes(key:str):
	pattern = re.compile("[A-Za-z0-9._-]+")
	match = pattern.fullmatch(key)
	if not match:
		raise Exception("Key must contain only A-Z a-z 0-9 _ - .")
	key = key.replace("\"", "'")
	key = key.replace(".", "\"][\"")
	return "[\"" + key + "\"]"


def check(db):
	if db.autocreate:
		#Create, if file is not exists
		if not os.path.exists(db.file):
			with open(db.file, 'w') as f:
				f.write("{}")
		#Create file, if empty
		with open(db.file, encoding="utf-8") as f: content = f.read()
		if content == "":
			with open(db.file, 'w') as f:
				f.write("{}")
	#Check indent
	try: db.indent = int(db.indent)
	except:
		raise ValueError("Indent can be only 'int'")
	#Check indent size
	if db.indent < 1:
		db.indent = 1
	if db.indent > 10:
		raise Exception("Indent cannot be bigger that 10")