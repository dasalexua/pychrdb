import os
from .utils import build_quotes, check

try:
	import ujson
except ModuleNotFoundError:
	os.system("pip install ujson==5.9.0")
	import ujson


class ChrDB:
	"""
	Create database connection to file.
	
	Attributes
	----------
	path: :class:`str`
	    File path.
	autocreate: Optional[:class:`bool`]
	    Automatically create a file if it doesn't exist.
	indent: Optional[:class:`int`]
	    The number of spaces in the indentation.
	"""

	def __init__(self, path:str, autocreate:bool=True, indent:int=4):
		#Options
		self.file = path
		self.autocreate = autocreate
		self.indent = indent
		#Check
		check(self)


	def find(self, key:str):
		"""
		Find key in the file. You can also use dots in the `key` argument to search in child dictionaries.
		```
		>>> db.find("key")
		>>> db.find("some_dict.key")
		```
		"""
		key = str(key)
		#Open DB
		check(self)
		with open(self.file, encoding="utf-8") as f:
			db = ujson.load(f)
		if not isinstance(db, dict):
			raise TypeError("Contents of the file must be a 'dict' object")
		#Getting
		if key in ('', '.', "None"): return db
		if '.' in key:
			keys = key.split('.')
			for k in keys:
				db = db[k]
		else:
			db = db[key]
		return db


	def full(self):
		"""
		Get the entire file as a `dict`. The same as `db.find(None)``
		"""
		return self.find('')


	def update(self, key:str, value):
		"""
		Change value of a key in the file. You can also use dots in the `key` argument to search in child dictionaries.
		```
		>>> db.update(key="key", value="Hello, World!")
		>>> db.update(key="some_dict.key", value=1234)
		```
		Contents of the file can be completely changed if you specify None in the `key` argument. In this case, the `value` argument must be a `dict`
		```
		>>> db.update(key=None, value={"name": "Hello, World!"})
		```
		"""
		key = str(key)
		#Open DB
		check(self)
		db:dict = self.full()
		#Edit
		if key in ('', '.', "None"):
			if not isinstance(value, dict):
				raise TypeError("Full contents of file can only be replaced with a 'dict' object")
			db = value
		else:
			if not isinstance(db, dict):
				raise TypeError("Contents of the file must be a 'dict' object")
			s = build_quotes(key)
			if isinstance(value, str):
				value = value.replace("\"","'")
				value = f"\"{value}\""
			exec(f"db{s} = {value}")
		#Save DB
		with open(self.file, 'w', encoding="utf-8") as f:
			ujson.dump(db, f, indent=self.indent, ensure_ascii=False)


	def delete(self, key:str):
		"""
		Find and delete key in the file. You can also use dots in the `key` argument to search in child dictionaries.
		```
		>>> db.delete("key")
		>>> db.delete("some_dict.key")
		```
		"""
		key = str(key)
		#Checks
		check(self)
		if key in ('', '.', "None"):
			with open(self.file, 'w') as f:
				return f.write("{}")
		#Open DB
		db:dict = self.full()
		if not isinstance(db, dict):
			raise TypeError("Contents of the file must be a 'dict' object")
		#Edit
		if '.' in key:
			keys = key.split('.')
			s = build_quotes('.'.join(keys[:-1]))
			exec(f"db{s}.pop(\"{key[-1]}\")")
		else:
			db.pop(key)
		#Save DB
		with open(self.file, 'w', encoding="utf-8") as f:
			ujson.dump(db, f, indent=self.indent, ensure_ascii=False)


	def clear(self):
		"""
		Clear the entire database.
		"""
		return self.delete('')