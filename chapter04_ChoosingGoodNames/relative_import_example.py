# you can run this module directly, or run chapter1.import_test.py

# it will work when you run it directly. but when you import this module from another place,
# it will raise error, this type of importing module shouldn't appear in a package.
# import litte_package
# print(litte_package)

from . import how_to_name
print(how_to_name)

from .litte_package import print_b
print(print_b)

from chapter04_ChoosingGoodNames.litte_package import print_b
print(print_b)