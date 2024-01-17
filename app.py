import random


def quantity():
    x = 0
    while x == 0 or x == 1:
        try:
            x = int(input('How Many: '))
            if x == 0 or x == 1:
                print(f"You Can't Enter {x}")

        except ValueError:
            print('ONLY enter an Integer')
    return x


def list_fill(quant):
    list0 = []
    x = 0
    for _ in range(quant):
        x += 1
        name = input(f'Enter the name no.{x}: ')
        list0.append(name)
    return list0


number = quantity()
the_list = list_fill(number)

print(f'\n **- The chosen one is {random.choices(the_list)} -**')
