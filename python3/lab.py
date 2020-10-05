a=3
print(id(a))
b=3
print(id(b))
a=a+3
print(id(a))

s = "ajldjlajfdljfddd"
s=set(s)
s=list(s)
s.sort(reverse = False)
print(s)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [x for x in a if x%2==1]
print(list2)