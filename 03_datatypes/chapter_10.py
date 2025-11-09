# Dictionary 

chai_order =dict(type="Masala Chai", size="Large",sugar=2)
print(f"Chai Order : {chai_order}")


chai_recipe={}
chai_recipe["base"]="black tea"
chai_recipe["liquid"]="milk"

print(f"Recipe base : {chai_recipe['base']}")

# to deelte a component
del chai_recipe["liquid"]
print(f"Recipe base : {chai_recipe}")

# member ship test
print(f"Is sugar in the order? {'sugar' in chai_order}")

chai_order={"type":"Ginger chai","size":"Medium","sugar":1}

# print(f"Order details (keys): {chai_order.keys()}")
# print(f"Order details (values): {chai_order.values()}")
# print(f"Order details (items): {chai_order.items()}")

last_item =chai_order.popitem()
print(f"Removed Item: {last_item}")

extra_spices={"card":"crushed","ginger":"sliced"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")

customer_note=chai_order.get("note","NO note")
print(f"customer_note is : {customer_note}")






