"""C:/Users/vesel/Downloads/Варианты заданий.pdf"""
from termcolor import colored, cprint


def input_control(name_of_p, min_number, max_number=1e8):
    """ проверка корректности входных данных """
    while True:
        input_val = input(
            colored("Input the number: " + name_of_p + " = ", 'green'))

        try:
            input_val = int(input_val)

        except ValueError:
            cprint("This is not an int number", 'red')

        else:
            if input_val < min_number:
                cprint("Number must be greater or equal to " + str(min_number),
                       'red')
            elif input_val > max_number:
                cprint(
                    "Number must be less than M = " + str(int(max_number + 1)),
                    'red')
            else:
                return input_val

        print("try again...")


def syracuse_sequence(n):
    """вычисление сиракузской последовательности

    Args:
        n (int): натуральное число по которому вычисляется последовательность

    Returns:
        list: сиракузская последовательность
    """
    next_n_func = lambda a: a // 2 if a % 2 == 0 else a * 3 + 1
    if next_n_func(n) == 1:
        return [n, 1]
    return [n, *syracuse_sequence(next_n_func(n))]


def syracuse_max(n):
    """нахождение наибольшего числа в сиракузской последовательности

    Args:
        n (int): натуральное число по которому вычисляется последовательность

    Returns:
        int: наибольшее число последоватлельности
    """
    max_func = lambda a, b: a if a > b else b
    next_n_func = lambda a: a // 2 if a % 2 == 0 else a * 3 + 1
    if next_n_func(n) == 1:
        return n
    return max_func(n, syracuse_max(next_n_func(n)))


def syracuse_max2(n):
    """
    то же самое, что и syracuse_max(n)
    """
    sequense = syracuse_sequence(n)
    max_el = n
    for elem in sequense:
        if max_el < elem:
            max_el = elem
    return max_el


def syracuse_max3(n):
    """
    то же самое, что и syracuse_max(n)
    """
    sequence = syracuse_sequence(n)
    sequence.sort()
    return sequence[-1]


def main():
    """main"""
    N = input_control("N", 1)

    mas = syracuse_sequence(N)
    print(mas)

    max_el = syracuse_max(N)  # 130с
    print(max_el)

    # max_el = syracuse_max2(N)  # 175с
    # print(max_el)

    # max_el = syracuse_max3(N)  # 183с
    # print(max_el)


if __name__ == '__main__':
    main()
