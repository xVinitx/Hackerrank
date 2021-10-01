size = int(input())
width = ((size - 1) * 2 + (size * 2) - 1)

for i in range(1, size, 1):
    number_of_letter = (i * 2) - 1
    s = ''
    letter_value = 97 + size - 1
    for j in range(0, number_of_letter):
        if j != 0:
            s += '-'
        s += chr(letter_value)
        if j < (number_of_letter - 1) / 2:
            letter_value = letter_value - 1
        else:
            letter_value = letter_value + 1
    print(s.center(width, '-'))

for i in range(size, 0, -1):
    number_of_letter = (i * 2) - 1
    s = ''
    letter_value = 97 + size - 1
    for j in range(0, number_of_letter):
        if j != 0:
            s += '-'
        s += chr(letter_value)
        if j < (number_of_letter - 1) / 2:
            letter_value = letter_value - 1
        else:
            letter_value = letter_value + 1
    print(s.center(width, '-'))
