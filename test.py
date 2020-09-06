def foo(a):
    a.append('hahaha')


def bar(b):
    b = 101
    print(b)


a = []
b = 100

foo(a)
bar(b)

print(a)
print(b)
