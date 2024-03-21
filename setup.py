import re
from setuptools import setup

version = ""
with open("chrdb/__init__.py", encoding="utf-8") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("Version is not set")

with open("README.md", encoding="utf-8") as f:
    description = f.read()

setup(
    name="chrdb",
    version=version,
    description="Improved and easy-to-use version of builtin Python's JSON",
    long_description=description,
    long_description_content_type="text/markdown",
    author="das Alex",
    packages=["chrdb"],
    include_package_data=True,
)
