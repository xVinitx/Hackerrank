"""
line = input(" ")
line = line.split(" ")  # a is converted to a list of strings.
# print(line)

line = "-".join(line)
print(line)
"""


def split_and_join(line):
    # write your code here
    line1 = line.split(" ")  # a is converted to a list of strings.
    # print(line)
    
    line1 = "-".join(line1)
    return line1


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
