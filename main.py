
def main():
    import func_without_return

    func_without_return.print_ascending(7, 6)

    from func_without_return import *

    print_ascending(5, 9)

    help(func_without_return.print_ascending)

if __name__ == "__main__":
    main()
