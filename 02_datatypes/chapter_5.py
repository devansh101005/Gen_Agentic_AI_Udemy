# Real Numbers (Used  for presions in programme)
import sys
from fractions import Fraction # help in calculating fractions
from decimal import Decimal # helps for decimal 

ideal_temp=95.5
current_temp=95.49999999999

print(f"Current temp {current_temp}")
print(f"Ideal temp {ideal_temp}")
print(f"Ideal temp {ideal_temp - current_temp}")

# output

# Current temp 95.49999999999
# Ideal temp 95.5
# Ideal temp 1.000444171950221e-11
# not a very good output

print(sys.float_info) # gives info ki ye hamre system mai kitni calculation karwa skta hai
