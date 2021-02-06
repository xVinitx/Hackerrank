def is_leap(year1):
    leap = False

    if year1 % 4 == 0:
        leap = True
        if year1 % 100 == 0:
            leap = False
        if year1 % 100 == 0 and year1 % 400 == 0:
            leap = True
    return leap


year = int(input())
print(is_leap(year))
