def chai_flavor(flavor="Masala"):
    """Return the flovor of chai."""
    chai="ginger"
    return flavor
print(chai_flavor.__doc__)
print(chai_flavor.__name__)




def generate_bill(chai=0,samosa=0):
    """
    Calculate the total bill for chai and samosa

    :param chai :Number of chai cups (10 rupees each)
    :param samosa:Number of samosa (15 rupees each)
    : return :(total amount,thank you mesaage as string)

    
    """

    total =chai*10 +samosa*15
    return total, "Thank you visiting chaicode.com"


print(generate_bill.__doc__)
print(generate_bill.__name__)
print(generate_bill(2, 3))

