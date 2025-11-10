flavours=['Gingers',"Out of stock","Lemon","Discontinued","Tulsi"]

for flavour in flavours:
    if flavour=="Out of stock":
        continue
    if flavour =="Discontinued":
        break
    print(f"{flavour} item found")

print("Out of loop")