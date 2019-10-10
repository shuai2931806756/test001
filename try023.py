# 开发作者：crowder Zhuo
# 开发时间：2019/10/10 20:57
# 文件名称： try023
# 开发工具：Python
site = {"name": "菜鸟教程", "url": "www.runoob.com",'ff':'tt'}
## {}：字典{‘key’：‘value’，。。。。}，【】；list（常用，里面的值可修改），（）：tuple（里面的值不可修改）
print("网站名：{name}, 地址:{url},哈哈:{ff}".format(**site)) #行吧，format用在字典里必须**