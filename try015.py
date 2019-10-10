# 开发作者：crowder Zhuo
# 开发时间：2019/10/9 20:35
# 文件名称： try015
# 开发工具：Python
for i in range (100,1000) :
    a=int(i/100)
    b=int(i/10) % 10
    c=int(i % 10)
    if (a**3+b**3+c**3==i):
        print(i,'是水仙花数')