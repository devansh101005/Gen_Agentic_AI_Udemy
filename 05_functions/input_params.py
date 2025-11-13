# chai ="Ginger chai"


# def prepare_chai(order):
#     print("Preparing",order)


# prepare_chai(chai)
# print(chai)



chai=[1,2,3]

def edit_chai(cup):
    cup[1] =42

edit_chai(chai)
print(chai)



def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)

make_chai("Darjwwling","yes","low") #positional
make_chai(tea="Green",sugar="Medium",milk="No")



def special_chai(*ingredients,**extras):
    print("Ingredients",ingredients)
    print("Extras",extras)

special_chai("Cinnamon","Card",sweetner="Honey",foam="Yes")

# * iska matlab hai ki arguments pas skarte jao koi bt ni aur ** iska matlab ki baaki arguments with definition bhi pass kiye ja sktye hain baad mai 


def chai_order(order=[]):
    order.append("Masala")
    print(order)

chai_order()
chai_order()

# to avoid upar waali bakchodi what we can do is 

def chai_order2(order=None):
    if order is None:
        order=[]
    print(order)
chai_order2()
chai_order2()