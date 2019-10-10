# 开发作者：crowder Zhuo
# 开发时间：2019/10/8 21:04
# 文件名称： try009
# 开发工具：Python
year =int(input('请输入今夕是何年：'))
month=int(input('请输入今夕是何月:'))
day=int(input('请输入今夕是何日：'))
le=[0,31,59,90,120,151,181,212,243,273,304,334]
if (0<month<=12) and (0<day<=31):
    for i in range(0,month,1):
        tt=le[i]
else:
    print('输入错误')
if ((year % 400==0)and(month>2)) or ((year%4==0)and(year%100!=0)and(month>2)):
    tt=le[i]+1
num=tt+day
print('这是一年的第'+str(num)+'天')