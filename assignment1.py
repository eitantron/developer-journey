name = input("Enter your name: ")
budget =float(input("Enter your budget: "))
spent = float(input("Enter how much you have spent today: "))
difference = budget - spent
print(f"hello {name}! I hope you are having a good day")
if budget - spent > 0:
    print(f"you have this amount of money left over: {budget - spent} dollars. Be good!")
elif float(difference) == 0:
    print(f"You are at $0 neither a defficit nor a surplus. You got this keep on tracking!")
else:
    print(f"You have gone over your budget by this much today: {-difference} You got this be better tomorrow.")
print("You will be better tomorrow")