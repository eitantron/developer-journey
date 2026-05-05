total_minutes = 0 
habit_log = ("\n")
habit_list = []
time_list = []
flag = True
while flag:
    print("welcome to our tiny habit tracker")
    print("1) add a new habit")
    print("2) Show total minutes")
    print("3) show habit list")
    print("4) Quit")
    choice = input("Pick 1-4: ")
    if choice == "4":
        print("Goodbye")
        flag = False
    elif choice == "3":
        print("TODO: list next")
    elif choice == "2":
        print(total_minutes)
    elif choice == "1":
        choice_1 = input("What Habbit are you tracking: ")
        choice_1a = int(input("For how long did you do this: "))
        habit_list.append(choice_1)
        time_list.append(choice_1a)
        total_minutes = total_minutes + choice_1a
        habit_log = habit_log + choice_1 + "\n"
        print(habit_list)
        print(time_list)
    else:
        print("Your choice is invalid")
