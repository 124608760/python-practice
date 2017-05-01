__author__ = 'xyx'
#按照字典中的键的值进行排序
dict={1:'v1', 4:'k4', 3:'s3', 2:'b2'}
print(sorted(dict.items(),key=lambda k:k[0],reverse=False))