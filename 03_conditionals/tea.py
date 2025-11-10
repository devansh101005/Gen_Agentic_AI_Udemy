user_input=input("Enter your preferred cup size(small/medium/large):").lower()

if user_input=="small":
    print(f"Price is 10 rupees")
elif user_input=="medium":
    print(f"Price is 15 rupees")
elif user_input=="large":
    print("Price is 20 rupees")
else:
    print("Unknown cup size")
