import random


def game():
    print_welcome() #print welcome 
    print_rules()#Print rules
    the_selection = selection()#ask for input
    print(the_selection)#compare
    computer_selection()#let them know wheather they have won or not
    #ask them to play game


def print_welcome():
    input("Welcome to the classic game of rock paper and scissors. Click Enter to continue: ")


def print_rules():
    input("""These are the rules... you choose either rock paper or scissor
    , Rock will always beat scissor. Scissor will always beat paper. 
    Paper will always beat rock. Click enter if you understand the rules:""")

def selection():
    answer = input("""select from the following:
     \n  1. for rock. 
     \n  2. for paper
     \n  3. for scissors 
    """)
    return answer
    
def computer_selection():
    random_number_generator = random.randint(1,3)
    print(random_number_generator)
    return random_number_generator

def comparison():
    pass
game()
