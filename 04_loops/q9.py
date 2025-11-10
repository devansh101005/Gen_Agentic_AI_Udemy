# value=13
# remainder=value%5
# if remainder:
#     print(f"Not Divisible ,remainder is {remainder}")

value =13
if (remainder := value%5):
     print(f"Not Divisible ,remainder is {remainder}")




available_sizes=["Small","Medium","Large"]

if(requested_size := input("Enter your chai cup size:")) in available_sizes:
     print(f"Serving {requested_size} size ki chai ")

else :
     print(f"Size is unavailable -{requested_size}")




flavors=["masala","ginger","mint","lemon"]

print(f"Avaialble flavous : {flavors}")

while(flavor := input("Choose ypur flavours:")) not in flavors:
     print(f"Sorry ,{flavor} is not avaialble")

print(f"This {flavor} is  avaialble and you choosed this  ")


