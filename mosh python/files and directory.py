# https://docs.python.org/3/py-modindex.html pathlib
# Absolute path (from the root of the hard disk)
# c:\Program files\Microsoft
# /user/local/bin
# Relative path (starting from the current directory)

from pathlib import Path

path = Path("ecommerce")
print(path.exists())
fakepath = Path("ecommerce2")
print(fakepath.exists())

# path = Path("emails")
# print(path.rmdir())
#
# path = Path("emails")
# print(path.mkdir())

path = Path()
# * = everything, *.* only in current directory, *.py, *.xls
print(path.glob('*.py'))

for file in path.glob('*.py'):
    print(file)