'''
regex.py re模块　功能函数演示
'''
import re

# 目标字符串
s = "Alex:1994,Sunny:1996"
pattern = r"(\w+):(\d+)" #正则表达式
# re 模块调用findall
l = re.findall(pattern,s)
print(l)
# compile 模块调用findall
regex = re.compile(pattern)
l = regex.findall(s,3,5)
print(l)


# 按照正则表达式匹配内容切割字符串
l = re.split(r"[:,]",s)
print(l)

# 替换目标字符串
f = re.subn(r":","-",s,1)
print(f)