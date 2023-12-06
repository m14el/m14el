# def umnozh (a, b):
#     if a < b:
#         return umnozh(b, a)
#     elif b != 0:
#         return (a + umnozh(a, b - 1))
#     else:
#         return 0
#
# a = int(input('введите первое число: '))
# b = int(input('введите второе число: '))
#
# print('результат произведения равен: ', umnozh(a, b))


def mult(a, b):
    if a == 1:
        return b
    else:
        return b + mult(a - 1, b)

a = int(input('введите первое число: '))
b = int(input('введите второе число: '))
print(f' результат умножения равен {mult(a, b)}')


def stepen (a1,b1):
    if b1 == 1:
        return a1
    else:
        b1 != 1
        return (a1 * stepen(a1, b1 - 1))

a1 = int(input('введите первое число: '))
b1 = int(input('введите второе число: '))
print(f'число {a1} в степени {b1} равно {stepen(a1, b1)}')



