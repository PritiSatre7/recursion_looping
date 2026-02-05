
def power(num:int, pow:int) -> int:
    retval = 1
    while num pow > 0:
        retval = num*retval
        pow = pow-1
    return retval

def repeat_str(text:str , num:int) -> str:
    if num<=0:
        return " "
    elif num==1:
        return text
    else:
        return text + repeat_str(text, num-1)


if __name__ == '__main__':


