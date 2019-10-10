# 开发作者：crowder Zhuo
# 开发时间：2019/10/8 20:15
# 文件名称： try007
# 开发工具：Python
for i in range(1,5,1):
    for j in range(1,5,1):
        for k in range(1,5,1):
            if (i!=j) and (j!=k) and (i!=k):
                print(str(i)+str(j)+str(k))