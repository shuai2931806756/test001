# 开发作者：crowder Zhuo
# 开发时间：2019/10/10 18:38
# 文件名称： try017
# 开发工具：Python
import  math
T=0
s=[]
t=0
n=int(input('请输入n值：'))
a=int(input('请输入a值：'))
for i in range(0,n,1) :
    T=T+a
    a=a*10
    s.append(T)
    print(T)
t=sum(s)
print('总值大小：',t)