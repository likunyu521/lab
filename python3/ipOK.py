def ip_ok(ip):

    point_index=[] # 用于存放分隔符'.'的下标
    for i in range(len(ip)):
        if ip[i]=='.':
            point_index.append(i)

    if len(point_index) != 3:
        print('分隔符不满足')
        return False

    # 将根据 . 拆分的字符串转换为数字 。（非数字转换为字符时会报错，需要异常处理）
    try:
        print(point_index)
        ip_1 = int(ip[0:point_index[0]])

    except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
        print('非数字错误')
        return False

    try:
        ip_2 = int(ip[(point_index[0] + 1):point_index[1]])
    except ValueError:
        print('非数字错误')
        return False
    try:
        ip_3 = int(ip[(point_index[1] + 1):point_index[2]])
    except ValueError:
        print('非数字错误')
        return False
    try:
        ip_4 = int(ip[(point_index[2] + 1):])
    except ValueError:
        print('非数字错误')
        return False

    if (ip_1>=0 and ip_1<=255 and ip_2>=0 and ip_2<=255
    and ip_3>=0 and ip_3<=255 and ip_4>=0 and ip_4<=255):
        return True

    else:
        print(ip_1, ip_2, ip_3, ip_4)
        print('ip不合法，范围不对')
        return False

ip = '192.163.0.x'

print(ip_ok(ip))














