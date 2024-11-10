from random import random, randint


def my_avg(num1: int, num2: int) -> float:
    """
    Calculate and returns the average of two integers
    :param num1: int: first number
    :param num2: int: second number
    :return: float: the average of the numbers
    """
    sum_avg = num1 + num2
    result = sum_avg / 2
    print(result)
    return result

def my_avg_nr(num1: int, num2: int) -> None:
    """
    Calculate and returns the average of two integers
    :param num1: int: first number
    :param num2: int: second number
    :return: None
    """
    sum_avg = num1 + num2
    result = sum_avg / 2
    print(result)

def main():
    #avg_9_4: float = my_avg(9, 4)
    #print(my_avg(9, 4))
    my_avg(9, 4)

    print(my_avg_nr(9, 4))
    l1 = [4, 7, -2, 0]
    print(l1.sort())
    print(l1)

    randint(1, 100)
    randint(1, 100)
    randint(1, 100)
    randint(1, 100)

if __name__ == "__main__":
    main()

