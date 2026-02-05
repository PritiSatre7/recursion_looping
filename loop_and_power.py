"""
Repeat String.

Repeat String program using conditions.

"""
def repeat_str(text:str , num:int) -> str:
    if num<=0:
        return " "
    elif num==1:
        return text
    else:
        return text + repeat_str(text, num-1)


if __name__ == '__main__':
    print(repeat_str("Priti", 4))


