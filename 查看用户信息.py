__author__ = 'xyx'
'''
使用python编写一个命令程序：里面保存了若干用户成员的信息，
用户只有登陆后才能查看这些用户的信息。
即：用户启动python脚本，然后输入用户名密码登陆成功后，使用命令可以查看其他用户信息
'''
userlogininfo={'user1':'password1','user2':'password2','user3':'password3'}
userprofile = {
    'user1':['zhangsan','male',18],
    'user2':['lisi','female',19],
    'user3':['wangwu','male',20]
}
def getinfo():
    print('请输入用户名查看对应用户信息，输入e退出')
    c = input()
    if c =='e':
        return 0
    if c in userprofile:
        print(userprofile[c])
        getinfo()
    else:
        print('该用户不存在')
        getinfo()

def userlogin():
  print('请输入用户名：')
  username = input()
  if username in userlogininfo:
          while(1):
              print('请输入密码：')
              password = input()
              if password == userlogininfo[username]:
                  getinfo()
                  break
              else:
                  print('密码错误,请重新输入')
  else:
      print('没找到用户名')
      userlogin()

userlogin()