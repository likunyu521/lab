with open('data.txt') as f: # 默认模式为‘r’，只读模式
    contents = f.read() # 读取文件全部内容
    print(contents) # 输出时在最后会多出一行（read()函数到达文件末会返回一个空字符，显示出空字符就是一个空行）
    print('------------')
    print(contents.rstrip()) # rstrip()函数用于删除字符串末的空白