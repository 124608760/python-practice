#词频统计
import string
path = 'C:/Users/xyx/Desktop/Walden.txt'
with open(path,'r') as text:
    words = [rawword.strip(string.punctuation).lower()  for rawword in text.read().split()] #去掉首尾的标点符号，并把大写转换为小谢
    wordsindex = set(words) #将列表转换为集合，去掉重复元素
    result = {index:words.count(index) for index in wordsindex} #创建一个“单词：频次”的字典
for word in sorted(result, key=lambda x:result[x], reverse= True):
    print('{}:{}'.format(word,result[word]))