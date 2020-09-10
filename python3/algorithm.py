# 一些基础算法

#递归

def func(x):
    if x > 0:
        print('抱着我', end='')
        func(x-1)
    else:
        print('小夜猫', end='')

# func(5)

# 汉诺塔


def hano(n, a, b, c):

    # n个柱子从a经过b移到c
    if n > 0:
        hano(n-1, a, c, b)
        print(a, '-->', c)
        hano(n-1, b, a, c)


# hano(4, 'a', 'b', 'c')

# 冒泡排序

def bubble_sort(list):
    n = len(list)

    for i in range(n):
        for j in range(n-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]


def select_sort(list):

    n = len(list)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if list[min_index] > list[j]:
                min_index = j

        list[i],list[min_index] = list[min_index],list[i]


list = [7,38,8,90,100,10000]

# bubbleSort(list)
select_sort(list)
for i in range(len(list)):
    print(list[i])