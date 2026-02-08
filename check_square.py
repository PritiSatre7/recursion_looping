"""
Perfect square

Function checks if the input is a perfect square, if not it falls back to the previous perfect square.

"""


def perfect_square(num:int) -> int:
    if num < 0:
        return " "
    i = 0
    while i * i <= num:
        i = i + 1
    if i * i > num:
        i = i - 1
    return "." * i

if __name__ == "__main__":
    print(perfect_square(0))
    print(perfect_square(1))
    print(perfect_square(4))
    print(perfect_square(9))
    print(perfect_square(16))
    print(perfect_square(-16))
