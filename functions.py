num = 10

def print_name():
    print('Nate')

def print_favorite_movie():
    print('Back to the Future')

def set_num():
    num = 5
    letter = 'a'
    print(letter)

def two_plus_two():
    val = 2 + 2
    return val

def add_two_numbers(num1, num2):
    val = num1 + num2
    return val

def packer(*args):
    for val in args:
        print(val)

def calculate_total(*args):
    total = sum(args)
    print(total)

print_favorite_movie()
print(num)

#sum = two_plus_two()

#print(sum + two_plus_two())

print(add_two_numbers(5, 10))

packer('hi', 'i', 'love', 'python')

calculate_total(20, 25, 50, 100)
