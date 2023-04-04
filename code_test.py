# from enum import Enum
#
# class myenum(str, Enum):
#     a = 'a'
#     b = 'b'
#

# UserDB = {"admin": "123456", "grey": "123456"}
# username = "admisdn"
# password = "123456"
#
# if username in UserDB.keys():
#     print("yes")

# 子类父类调试
class Father:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Son(Father):
    def __init__(self, x,y,z):
        super().__init__(x,y)
        self.z = z

xs = Father(1,2)
print(xs.y)

xss = Son(1,2,3)
print(xss.y)