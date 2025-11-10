# Tuples

# ()
# immutable 

masala_spices=("card","cloves","cinamon")

(spice1,spice2,spice3)=masala_spices

print(f"Main masala spices: {spice1},{spice2},{spice3}")

ginger_ratio ,card_ratio=2,1
print(f"Ratio is G: {ginger_ratio} and C: {card_ratio}")

ginger_ratio ,card_ratio=card_ratio,ginger_ratio
print(f"Ratio is G: {ginger_ratio} and C: {card_ratio}")

# member ship

print(f"Is ginger in masala spices ? {'ginger' in masala_spices}")

