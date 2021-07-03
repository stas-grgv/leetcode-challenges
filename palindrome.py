import math
from decimal import Decimal


# Log10(x)
def number_of_digits(x: int):
    if x == 0:
        return 1
    else:
        return (int(math.log10(x)))


def checkPalindrome(x: int) -> bool:
    is_palindrome = False
    if x < 10 and x > 0:
        is_palindrome = True
    elif x < 0:
        is_palindrome = False
    else:
        is_palindrome = False

        numbers = []
        number = 0
        temp = x
        for i in range(0, number_of_digits(x)+1):
            #
            subtraction = 10 ** ((number_of_digits(temp)-i))

            
            # Получаем дробную часть от деления
            # number = (math.modf(temp//subtraction/10)[0])
            number = int((round(Decimal(math.modf(temp//subtraction/10)[0]), 1)) * 10)
            # print(number)
            numbers.append(number)

        # print(numbers[::-1])
        reversed_int = 0
        index = len(numbers) - 1

        for i in numbers[::-1]:
            # print(i * (10 ** index))
            reversed_int += i * (10 ** index)
            index -= 1

        # print(f'reversed int: {reversed_int}')

        if reversed_int == x:
            # print('palindrome')
            is_palindrome = True
        else:
            # print('not palindrome')
            is_palindrome = False

        

    return is_palindrome


print(checkPalindrome(140))