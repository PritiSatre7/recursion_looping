def perfect_square(num:int) -> int:
    i = 0
    while i * i <= num:
        i = i + 1
    if i * i > num:
        i = i - 1
    return "." * i

if __name__ == "__main__":
    print(perfect_square(5))