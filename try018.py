# 开发作者：crowder Zhuo
# 开发时间：2019/10/10 18:57
# 文件名称： try018
# 开发工具：Python
 ### 求约数
def search (n) :
    L=[]
    for i in range(2,n+1):
        if n %i ==0:
            n=int(n/i)
            L.append(i)
            break
    return  L
