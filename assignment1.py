name = input("Enter your name: ")
budget =float(input("Enter your budget: "))
spent = float(input("Enter how much you have spent today: "))
print(f"hello {name}! I hope you are having a good day")
if float(budget) - float(spent) > 0:
    print(f"you have this amount of money left over: {float(budget) - float(spent)} dollars. You got this!")
else:
    print(f"You have gone over your budget by this much today: {float(budget) - float(spent)}")