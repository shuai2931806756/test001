# 开发作者：crowder Zhuo
# 开发时间：2019/10/10 19:48
# 文件名称： try021
# 开发工具：Python
import math
qq=0
for i in range(2,1001,1):
    n=-1
    k=[]
    for j in range(1,i):
        if i % j == 0:
            n+=1
            k.append(j)
    t=len(k)
    if i == sum(k):
        qq+=1
        print(i,'= ',end='')
        for p in range(0,t,1):
            if p!=t-1:
                print(k[p],'+ ',end='')
            else :
                print(k[p])
print('一共有',qq,'个完数')