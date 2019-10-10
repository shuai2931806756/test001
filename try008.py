# 开发作者：crowder Zhuo
# 开发时间：2019/10/8 20:28
# 文件名称： try008
# 开发工具：Python
import math
profits=abs(float(input('请输入净利润(单位：万元):')))
if (profits<=10) :
    answer=profits*0.1
elif (profits>10) and (profits<=20) :
    answer=(profits-10)*0.075+1
elif (profits>20) and (profits<=40) :
    answer=(profits-20)*0.05+1.75
elif (profits>40) and (profits<=60):
    answer=(profits-40)*0.03+2.75
elif (profits>60) and (profits<=100):
    answer=(profits-60)*0.015+3.35
else :
    answer=(profits-100)*0.01+3.95
print('提成为：'+str(answer))
# 推荐使用列表+for循环来完成，更简单。