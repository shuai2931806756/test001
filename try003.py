# 开发作者：crowder Zhuo
# 开发时间：2019/10/6 21:25
# 文件名称： try003
# 开发工具：Python
for i in range(1,10,1):
    for j in range(1,i+1,1):
        print(str(i),'*',str(j),'=',str(i*j),'\t',end='') #end=''是为了写在同一行里，\t:制表对齐，易读
    print('') #这里是为了j算完就换行的
