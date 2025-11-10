staff=[("Amit",16),("Zara",12),("Devansh",22),("Prateek",19)]

for name, age in staff:
    if age>=18:
        print(f"{name} is allowed to mange the staff")
        break

else:
    print(f"No one is elgible to do ")