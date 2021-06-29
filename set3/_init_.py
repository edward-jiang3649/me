def loop_ranger(start, stop=None, step=1):
    list_of_numbers = []

    for i in range(start, stop, step):
        list_of_numbers.append(i)
    return list_of_numbers


def lone_ranger(start, stop, step):
    list_of_numbers = []

    for i in range(start, stop, step):
        list_of_numbers.append(i)
    return list_of_numbers


def two_step_ranger(start, stop, step=2):
    list = []

    for i in range(start, stop, step):
        list.append(i)
    return list


def stubborn_asker(low, high):
    numbers = range(low, high)
    while True:
        Enter_a_number = int(input("Enter a Number HERE: "))
        while Enter_a_number in numbers:
            return Enter_a_number


def not_number_rejector(message):
    num = input("Please input an integer: ")
    while type(num) != int:
        num = input("Error. Please input an INTEGER: ")
    return num


def super_asker(low, high):
    numbers = range(low, high)
    num = input("Please input an integer: ")
    while type(num) != int:
        num = input("Error. Please input an INTEGER: ")
        while num in numbers:
            return num + "is an integer"
    else:
        return "false"
