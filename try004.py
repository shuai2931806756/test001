# 开发作者：crowder Zhuo
# 开发时间：2019/10/8 15:29
# 文件名称： try004
# 开发工具：Python
tol=99
for number in range(1,100,1):
    if number % 7 ==0 :
        continue
    elif str(number).endswith('7') :
        continue
    tol=tol-1
print('一共拍了',str(tol),'次桌子')