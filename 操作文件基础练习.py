__author__ = 'xyx'
#创建一个文件，写入一条信息
def text_create(name, msg):
    desktop_path = 'C:/Users/xyx/Desktop/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path,'w')
    file.write(msg)
    file.close()
text_create('a','bbb')
