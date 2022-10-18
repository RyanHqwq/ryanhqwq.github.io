import os #导入模块
filename = 'C:\\Users\\ASUSPC\\Documents\\GitHub\\ryanhqwq.github.io\\init\\image' #文件地址
list_path = os.listdir(filename)  #读取文件夹里面的名字
x=0
for index in list_path:
    x+=1                       #list_path返回的是一个列表   通过for循环遍历提取元素
    name = index.split('.')[0]   #split字符串分割的方法 , 分割之后是返回的列表 索引取第一个元素[0]
    kid = index.split('.')[-1]   #[-1] 取最后一个
    path = filename + '\\' + index
    new_path = filename + '\\'  + str(x) + '.' + kid
    os.rename(path, new_path) #重新命名
print('修改完成')