# 开发作者：crowder Zhuo
# 开发时间：2019/10/9 19:39
# 文件名称： try014
# 开发工具：Python
# from math import sqrt
# h=0
# for m in range(101,201):
#     leap=1
#     k = int(sqrt(m))        #返回数字的平方根
#     for i in range(2,k+1):#K+1，表示从2循环到K(包含k)
#         if m % i==0: # 如果能被整除说明不是素数
#             leap=0
#             break
#     if leap==1:
#         print(m)
#         h+=1
# print('The total is ',h)
# t=0
# # for i in range(101,201):
# #     for j in range(2,i):
# #         if i%j==0:break
# #     else:    # 核心就在这个else是for else用法
# #         print(i,'是质数')
# #         t+=1
# # print ('一共',t,'个素数')
t=0
for i in range(101,201):
    a=2
    while a<i:
        if i%a==0:break
        else:a=a+1
    if a==i:
        print(i)
        t+=1
print('一共',t,'个素数')