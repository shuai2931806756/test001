# 开发作者：crowder Zhuo
# 开发时间：2019/10/10 19:13
# 文件名称： try020
# 开发工具：Python
while 1:
    n = int(input('请输入一个整数：'))
    print(n,'=',end='')
    while n>1:
        for i in range(2,n+1):
            if n%i==0:
                n=int(n/i)
                if n==1:  # 这里是到了最后一个数，不写*
                    print(i,end='')
                else:
                    print(i,'* ',end='')
                break
    print() #这里起换行作用