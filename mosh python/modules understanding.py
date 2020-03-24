# we use modules to better organise our code
# break up code in different modules
# 2 ways to import modules
import weight_converter_module
print(weight_converter_module.kg_to_lbs(70))


# with prefixing
from weight_converter_module import kg_to_lbs
print(kg_to_lbs(120))