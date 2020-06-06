# MadLibs - Practice Input and Output
#
# Template:
#   I enjoy practice! I find it helps me to __(verb)__ better.
#   Without practice, my __(noun)__ would probably not even work.
#   My code is getting more __(adjective)__ every single day!


# Prompt the user for parts of speech and store them in variables
madlib_verb = input("Please enter a verb: ")
madlib_noun = input("Please enter a noun: ")
madlib_adjective = input("Please enter an adjective: ")

# Output the template to the screen with the blanks filled out with what the user stated
print("I enjoy practice! I find it helps me to", madlib_verb, "better.")
print("Without practice, my", madlib_noun, "would probably not even work.")
print("My code is getting more", madlib_adjective, "every single day!")
