# from enum import Enum
#
# class myenum(str, Enum):
#     a = 'a'
#     b = 'b'
#

UserDB = {"admin": "123456", "grey": "123456"}
username = "admisdn"
password = "123456"

if username in UserDB.keys():
    print("yes")
