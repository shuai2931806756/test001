# 开发作者：crowder Zhuo
# 开发时间：2019/10/10 19:06
# 文件名称： try019
# 开发工具：Python
from try018 import search
while 1:
    s = input('请输入一个正整数：')
    if s.isdigit() and int(s)>0:
        print(s,'=','*')#*.join(sequence)用*号连接元素序列
    else:
        print('请输入一个正整数：')