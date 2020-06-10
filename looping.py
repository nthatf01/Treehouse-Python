name = input("What's your name? ")

def prompt_for_yes_or_no():
    return input("(Enter yes/no) ").lower()

# Ask the user by name if they understand Python while loops

print("{}, do you understand Python while loops? ".format(name))
user_answer = prompt_for_yes_or_no()

# Write a while statement that checks if the user doesn't understand while loops

while user_answer != "yes":

# Since the user doesn't understand while loops, let's explain them.

    print("Ok, {}, while loops in Python repeat as long as a certain Boolean condition is met.".format(name))

# Ask the user again, by name, if they understand while loops.

    print("{}, now do you understand Python while loops?".format(name))
    user_answer = prompt_for_yes_or_no()

# Outside the while loop, congratulate the user for understanding while loops
 
print("That's great, {}.  I'm pleased that you understand while loops now.  That was getting repetitive".format(name))
