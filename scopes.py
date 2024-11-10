
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




