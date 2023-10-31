import random

res=[]
def spisok1(lst1):
    for i in lst1:
        print(i)


def spisok2(lst2):
    for j in lst2:
        print(j)


x1=int(input('введите кол-во строк 1-ой матрицы: '))
y1=int(input('введите кол-во столбцов 1-ой матрицы: '))

x2=int(input('введите кол-во строк 2-ой матрицы: '))
y2=int(input('введите кол-во столбцов 2-ой матрицы: '))


matrix1=[[random.randint(0,1000) for i in range(y1)] for i in range(x1)]

matrix2=[[random.randint(0,1000) for j in range(y2)] for j in range(x2)]

spisok1(matrix1)
spisok2(matrix2)


