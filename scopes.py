
x: int = 10  # global

def print_x(x: int):
    # x parameter -- locally
    x = x + 1
    print(f"in print_x, local is {x}")

def define_x():
    # x variable -- locally
    x: int = 20
    x = x + 1
    print(f"in define_x, local x is {x}")

def change_x():
    # can use a global variable
    #print(x)  # 10 # DONT!! should not, but works

    # ERROR
    #x = x + 1  # cannot change global. read only

    # DONT!! should not, but works
    global x  # first line in function
    x = x + 1


print_x(x)  # 11
define_x()  # 21
print('global x after print_x, define_x', x)  # 10
change_x()
print('global x after change_x', x)  # 11

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
#    create a local counter in this function
#    set its value to 20
# call inc_counter 3 times
# call dec_counter 2 times
# call print_counter
# call inc_local_counter
# call print_counter, what was the output?



