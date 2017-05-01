__author__ = 'xyx'
#阶乘
def jiecheng(num):
  x=1
  if num<0:
      return ("负数没有阶乘！")
  elif num==0:
      return("1")
  else:
      for i in range(1,num+1):
          x=x*i
      return x

print(jiecheng(int(input("请输入一个数字"))))