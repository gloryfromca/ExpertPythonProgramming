#how to use module and package
import chapter04_ChoosingGoodNames
from chapter04_ChoosingGoodNames import litte_package
from chapter04_ChoosingGoodNames.litte_package import print_b
from chapter04_ChoosingGoodNames.litte_package import print_a
from chapter04_ChoosingGoodNames.litte_package.print_a import print_a as print_a_func
print(chapter04_ChoosingGoodNames)
print(litte_package)
print(print_b)
print(print_a)
print(print_a_func)
print_b()
print_a_func()

