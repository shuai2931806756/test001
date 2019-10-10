# 开发作者：crowder Zhuo
# 开发时间：2019/10/8 18:14
# 文件名称： try006
# 开发工具：Python
import time
tic=time.localtime(time.time())
print('当前时间是'+str(tic.tm_year)+'年'+str(tic.tm_mon)+'月'+str(tic.tm_mday)+'日'+str(tic.tm_hour)+'点'+str(tic.tm_min)+'分')
# + ‘：’用于string格式直接拼接，中间没有自带的空格，‘，’： 可以直接print连接int，float，string。但是会自带空格