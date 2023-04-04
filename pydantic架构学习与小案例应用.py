from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel # 导入BaseModel类


class User(BaseModel):
    id:int
    name = 'Grey'

user = User(id='123')
print(user.id)         # 123
print(type(user.id))   # int
assert user.id==123 # 对user.id进行数据验证
# 上面案例说明在创建user实例时,Pydantic对实例进行了数据模型的验证和解析，'123'被强制转化为123
assert user.id==123

print(user.dict()) # {'id': 123, 'name': 'Grey'} 字典数据结构
print(user.json()) # {"id": 123, "name": "Grey"} json数据格式
print(user.__fields__) # 罗列了数据模型的全部字段（以字典形式展现）
# {'id': ModelField(name='id', type=int, required=True), 'name': ModelField(name='name', type=str, required=False, default='Grey')}