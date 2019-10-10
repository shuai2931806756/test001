# 开发作者：crowder Zhuo
# 开发时间：2019/10/9 21:27
# 文件名称： try016
# 开发工具：Python
import string
s=input('请输入字符串：')
x0=0
x1=0
x2=0
x3=0
i=0
while i<len(s):
    c=s[i]
    if c.isalpha() :
        x0+=1
    elif c.isdigit():
        x1+=1
    elif c.isspace():
        x2+=1
    else :
        x3+=1
    i+=1
print('一共有',x0,'个字母',x1,'个数字',x2,'个空格',x3,'个其他字符')