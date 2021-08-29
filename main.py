# Update of the code, Aug 29

def ssum(*args):

    sum_args = 0
    for i in args:
        if type(i) == int or type(i) == float:
            sum_args += i

    return print("The sum of numeric arguments in our list is: ", sum_args)

ssum("q", "a", 5, 5, 3.0)

# Calculati sumele de la 0 la n, respectiv ale numerelor pare si impare

my_number = int(input("Enter here your number, please: "))

def my_summ(my_number):
    # First, calculate the sum of numbers from zero to mine:

    summ = 0
    for i in range(my_number+1):
        summ += i
    print("The sum of the numbers from zero to mine is: ", summ)

    # Second, calculate the sum of even numbers in our series from zero to my_number:

    def even_sum(my_number):
        even_sum = 0
        for i in range(my_number+1):
            if i % 2 == 0:
                even_sum += i
        print("The sum of even numbers from zero to my_number is: ", even_sum)

    even_sum(my_number)

    # Third, calculate the sum of odd numbers in our series from zero to my_number:

    def odd_sum(my_number):
        odd_sum = 0
        for i in range(my_number + 1):
            if i % 2 != 0:
                odd_sum += i

        print("The sum of odd numbers from zero to my_number is: ", odd_sum)

    odd_sum(my_number)

my_summ(my_number)

# Sa se scrie o functie care citeste de la tastatura si returneaza valoarea daca aceasta este un nr intreg,
# altfel returneaza valoarea 0.


def func_input():

    try:
        entered_value = int(input("Type in something, please: "))
        print(entered_value)

    except ValueError:
        print(0)

func_input()


