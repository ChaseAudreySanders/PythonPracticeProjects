def number_pattern(n):
    if isinstance(n, int) == False:
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    else:
        number_string = ""
        number = 0
        for number in range(1, n + 1):
            number_string += str(number) + ' '
        return number_string.strip()

print(number_pattern(4))