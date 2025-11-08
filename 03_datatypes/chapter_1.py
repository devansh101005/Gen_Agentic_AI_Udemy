sugar_amount=2

print(f"Initial sugar: {sugar_amount}")

sugar_amount=12
print(f"Initial second sugar: {sugar_amount}")

# now new value will be printed but number is immutable so how its happening
# basically 12 is also created now the refernce is given to 12

print(f"ID of 2: {id(2)}")
print(f"ID of 2: {id(12)}")

