# list (mutable)

3 # same as array

ingredients = ["Water","milk","black","tea"]
ingredients.append("sugar")
print(f"Ingrdients are :{ingredients}")

ingredients.remove("Water")
print(f"Ingrdients are :{ingredients}")

spice_options=["ginger","card"]
chai_ingredients=["water","milk"]

chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")
chai_ingredients.insert(2,"black tea")
print(f"chai: {chai_ingredients}")

last_added=chai_ingredients.pop()
print(f"{last_added}")

print(f"chai: {chai_ingredients}")

chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")



# operator overloading 
# when operators are used for doing more than one task

base_liquid=["water","milk"]
extra_flavour=["ginger"]
full_liquid_mix= base_liquid+extra_flavour
print(f"Liquid  mix:{full_liquid_mix}")

strong_brew=["black tea","water"] *3
print(f"String brew:{strong_brew}")



#bytearray
raw_spice_data=bytearray(b"CINNAMON")
print(f"Bytes: {raw_spice_data}")


