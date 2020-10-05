#100道python真题
# 1 求1--100之和
print((range(1,101)))

# 函数内部修改全局变量。需要先声明，再修改，主函数除外（if __name__ == "__main__":）
a = 10
def test1():
    global a
    a = 5
test1()
print('a=%d'%a)


dic1 = {'a':1,'b':2}
print(dic1)
del dic1['a']
print(dic1)

dic2 = {'c':3,'d':4}
dic1.update(dic2)
print(dic1)

list1 = [1,3,3,4,5,4,7,9]
set1 = set(list1)
print(set1)
list2 = [x for x in set1]
print(list2)


