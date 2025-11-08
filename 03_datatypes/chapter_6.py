# Strings 

# Strings are immutable (in memory they always create new refences)

chai_type="Ginger type"

customer_name="Priya"

print(f"Order for :{customer_name}:{chai_type} please")


# indexing
# in indexing last number is not inclusive 
chai_description="Aromatic and bold !"

print(f"First word: {chai_description[0:8]}")
print(f"First word: {chai_description[0:8:2]}")
print(f"First word: {chai_description[:8]}")
print(f"First word: {chai_description[12:]}")
print(f"First word: {chai_description[::-1]}")

# dealing with some special characters

label_text = "Chai Spécial"
ecoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {ecoded_label}")
decoded_label = ecoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")

