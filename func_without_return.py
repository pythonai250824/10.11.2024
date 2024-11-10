
def print_ascending(x: int, y: int) -> None:
    """printing the given numbers in ascending order"""
    # 1
    if x > y:
        print (y, x)
    else:
        print (x, y)
    # 2
    print(f"{y} {x}" if x > y else f"{x} {y}")

def main():
    print_ascending(4, 2)

if __name__ == "__main__":
    main()



