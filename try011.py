# 开发作者：crowder Zhuo
# 开发时间：2019/10/9 18:25
# 文件名称： try011
# 开发工具：Python
def fibs (n) :
    if (n==1) :
        return [1]
    if (n==2) :
        return [1,1]
    fibs=[1,1]
    for i in range(0,n,1) :
        fibs.append(fibs[-1]+fibs[-2])
    return fibs
