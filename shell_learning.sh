#!/bin/bash
#shell脚本学习

# 变量定义和使用
name="likunyu"
echo ${name}

# 参数传递,$0代表文件路径 $1 $2表示对应传入参数
echo $0
echo $1
echo $2

# 数组定义 define array

student=('likunyu' 'fengtang' 'wangxiaobo')

#表达式, 原声shell不支持数学运算，需要expr
ab=`expr 1 + 1`
echo ${ab}

#常用命令
# echo
# printf
# test 检测某个条件是否成立

# 函数

