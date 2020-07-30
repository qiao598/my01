'''
编写接口函数，从终端输入端口名称获取端口
运行状态中的地址值
思路分析：
1.根据输入的端口名称找到对应的段落
2.在该段落中匹配address
'''
import re
import os

port = input("端口：")
fd= open("exc.txt","r")
data = ''
for line in fd:
    if line == "\n":
        print("======")
    print(line)


# def findall01(data):
#     # requst = fd.read()
#     list_=data.split("\n")
#
#     for i in list_:
#         print(i)
#
#     # re.findall(,target)
# findall01()