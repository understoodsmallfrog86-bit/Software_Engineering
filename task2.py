from random import randint
def dice():
    result=randint(1,6)
    print(result)
    if result > 4:
        return ("Вы победили")
    elif result>2:
        dice()
    else:
        return ("Вы проиграли")
print(dice())