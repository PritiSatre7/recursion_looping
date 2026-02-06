

def atarangi(nterm: int) -> int:
    if nterm ==0:
        return 0
    elif nterm == 1 or nterm == 2:
        return 1
    else:
        return 2 * atarangi(nterm-1) - 3 * atarangi(nterm-2) + 4 * atarangi(nterm-3)

if __name__ == "__main__":
    print(atarangi(4))




