#!/bin/bash

if [ -n "$1" ]&&[ -n "$2" ]; then
   cd /Users/haroldrain/project/$1
#   echo `pwd`
   git add .
   git commit -m "$2"
   git pull
   git status
   git push origin master
   echo "$1项目已更新到Github，更新内容：$2"
else
    echo "填写项目名称和提交备注"
fi