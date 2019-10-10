# 开发作者：crowder Zhuo
# 开发时间：2019/10/8 21:31
# 文件名称： try010
# 开发工具：Python
x=float(input('Please input numbervalue of x :'))
y=float(input('Please input numbervalue of y :'))
z=float(input('Please input numbervalue of z :'))
tt=max(x,y,z)
qq=min(x,y,z)
if (qq<x<tt):
    print('从小到大排列:',qq,x,tt)
elif (qq<y<tt):
    print('从小到大排列:',qq,y,tt)
else:
    print('从小到大排列:',qq,z,tt)

##`~~~~~~~~~~~~~~
# l = []
# for i in range(3):
#     x = int(raw_input('integer:\n'))
#     l.append(x) # 在list末尾添加新对象
# l.sort() # 对list进行排序
# print l
