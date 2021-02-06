from collections import OrderedDict

dct = OrderedDict()
for x in range(int(input())):
    i = input().rpartition(" ")
    dct[i[0]] = int(i[-1]) + dct[i[0]] if i[0] in dct else int(i[-1])
for l in dct:
    print(l, dct[l])
