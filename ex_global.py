
# Exercise:
# set counter = 10 (in global scope)

# create a function called inc_counter()
#    which add 1 to global counter
# create a function called dec_counter()
#    which subtract 1 to global counter
# create a function called print_counter()
#    which prints the global counter
#    do we need the global definition here?
# create a function called inc_local_counter()
#    create a local variable called also counter in this function
#    set its value to 20
# call inc_counter 3 times
# call dec_counter 2 times
# call print_counter
# call inc_local_counter
# call print_counter, what was the output?

counter: int = 10

def inc_counter():
    global counter
    counter += 1

def dec_counter():
    global counter
    counter -= 1

def print_counter():
    print(counter)  # global read only

def inc_local_counter():
    counter : int = 20  # local counter
    print()

inc_counter()  # 11
inc_counter()  # 12
inc_counter()  # 13

dec_counter()  # 12
dec_counter()  # 11

print_counter()  # 11
inc_local_counter()  # 11
print_counter()  # 11

# correct
def inc_counter_correct(counter: int) -> int:
    counter += 1
    return counter

counter = inc_counter_correct(counter)

def dec_counter_correct(counter: int):
    counter -= 1
    return counter

counter = dec_counter_correct(counter)

def print_counter_correct(counter: int):
    print(counter)

print_counter_correct(counter)