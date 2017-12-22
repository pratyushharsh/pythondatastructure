from stack import Stacks


def binary_string(number):
    s = Stacks()
    while number > 0:
        rem = number % 2
        s.push(rem)
        number = number // 2

    bin_str = ""
    while not s.is_empty():
        bin_str += str(s.pop())

    return bin_str


def conversion(number, factor):
    s = Stacks()
    digits = '0123456789ABCDEF'

    while number > 0:
        rem = number % factor
        s.push(digits[rem])
        number = number // factor

    bin_str = ""
    while not s.is_empty():
        bin_str += str(s.pop())

    return bin_str


print(binary_string(42))
print(conversion(25, 8))
