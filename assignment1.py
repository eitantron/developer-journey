name = input("Enter your name: ")
budget = input("Enter your budget: ")
spent = input("Enter how much you have spent today: ")
print(f"hello {name}! I hope you are having a good day")
if int(budget) - int(spent) > 0:
    print(f"you have this amount of money left over: {int(budget) - int(spent)}")
else:
    print(f"You have gone over your budget by this much today: {int(budget) - int(spent)}")