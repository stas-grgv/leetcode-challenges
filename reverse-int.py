def reverse(x: int) -> int:
        str1 = str(abs(x))
        reversed1 = 0
        if x > 0:
            reversed1 = int(str1[::-1])
        elif x == 0:
            reversed1 = 0
        elif x < 0:
            reversed1 = int("-" + str1[::-1])

        if reversed1 not in range((-2**31),(2**31)):
            reversed1 = 0

        return reversed1
