def make_chai():
    if not kettle_has_water():
        fill_kettle()
    plug_in_kettle()
    boil_water()
    if not is_cup_clean():
        wash_cup()
    add_to_cup("Sugar")
    pour("boiled water")
    stir("cup")
    serve("chai")

make_chai()

# if you know english you can understand python code 

#What is object ?
#In programming its like a thing

#What is properties?

#What are methods?