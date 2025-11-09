essential_price={"card","ginger","cinnamon"}
optional_spices= {"cloves","ginger","black pepper"}

all_spices=essential_price | optional_spices
print(f"All spices:{all_spices}")

common_spices =essential_price & optional_spices
print(f"Common spices: {common_spices}")

only_in_essential=essential_price-optional_spices
print(f"Only in essential:{only_in_essential}")


#Member ship test

print(f"Is 'cloves' in essential spices ? { 'cloves' in optional_spices}")