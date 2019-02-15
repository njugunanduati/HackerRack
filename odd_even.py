#An odd number is an integer which is not a multiple of two
#An even number is an integer which is "evenly divisible" by two

def check_number(number):
    if number % 2 != 0:
        solution = 'Weird'
    elif number % 2 == 0  and number in range(2, 5):
        solution = 'Not Wierd'
    elif number % 2 == 0 and number in range(6, 20):
        solution = 'Weird'
    elif number % 2 == 0 and number > 20:
        solution = 'Not Weird'
    return solution


number = int(input('Enter the number: '))
print(check_number(number))
