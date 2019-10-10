# 开发作者：crowder Zhuo
# 开发时间：2019/10/10 20:44
# 文件名称： try022
# 开发工具：Python
tour = []
height = []

hei = 100.0  # 起始高度
tim = 10  # 次数

for i in range(1, tim + 1):
    # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
    if i == 1:
        tour.append(hei)
    else:
        tour.append(2 * hei)
    hei /= 2
    height.append(hei)

print('总高度：',sum(tour))
print('第10次反弹高度：',height[-1])