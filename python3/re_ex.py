import re
str = '<div class = "name">中国</div>'
res = re.findall(r'<div class = ".*">(.*?)</div>',str)
print(res)

str2 = '<img src="https://static.rongyiju.com/images/debris/d1c0b808c63a80d20d3538696c287208.png" alt="" style="text-align: center">'

re = re.findall(r'https://.*?png',str2)[0]

print(re)