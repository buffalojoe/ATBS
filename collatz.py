def collatz(number):

    try:
        number = int(number)
    except:
        return print('Input must be an integer')

    if number == 1:
        print(number)
    elif number % 2 == 0:
        print(number)
        collatz(number // 2)
    elif number % 2 != 0:
        print(number)
        collatz(3 * number + 1)

number = input()
collatz(number)