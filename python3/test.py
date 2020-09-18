def foo(a):
    a.append('hahaha')


def bar(b):
    b = 101
    # print(b)


a = []
b = 100

foo(a)
bar(b)

x = 10
y = 20
z = 0
p = 0

print(y and x)
print(z or x)
print(not(x or z))
print(z or p)


