Chroma Database (ChrDB)
=======
Improved and easy-to-use version of builtin Python's JSON

Key Features
------------

- Simple and easy-to-use syntax.
- It is based on ujson, instead of default json, which speeds up the database.
- You can use dots in the key arguments to search in child dictionaries.

Installing
----------

**Python 3.8 or higher is required.**

```sh
# Linux/macOS
python3 -m pip install pychrdb

# Windows
py -3 -m pip install pychrdb
```

Usage
-----

Print full database to the console:
```py
from chrdb import ChrDB

database = ChrDB("database.json")
print(database.full())
```

Get the key from the database:
```py
from chrdb import ChrDB

database = ChrDB("database.json")
database.find("key")
```

Update key value in the database:
```py
from chrdb import ChrDB

database = ChrDB("database.json")
database.update(key="key", value="Hello, World!")
```

Update full database (value must be `dict`):
```py
from chrdb import ChrDB

database = ChrDB("database.json")
database.update(key=None, value={"key": "Hello, World!"})
```

Delete key from the database:
```py
from chrdb import ChrDB

database = ChrDB("database.json")
database.delete("key")
```