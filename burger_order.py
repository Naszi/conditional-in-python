print("Welcome to Burger Shop!")
size = input("What size Burger do you want? M, N or L ")
add_mushroom = input("Do you want mushroom? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "M":
    bill += 5
    if add_mushroom == "Y":
        bill += 1
elif size == "N":
    bill = 8
    if add_mushroom == "Y":
        bill += 1
else:
    bill = 10
    if add_mushroom == "Y":
        bill += 2
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")
