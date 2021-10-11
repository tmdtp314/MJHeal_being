from Models.mysql import conn_mysqlDB
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self,userID,password,phone,gender,addr):
        self.userID=userID
        self.password=password
        self.phone=phone
        self.gender=gender
        self.addr=addr
    def get_id(self):
        return str(self.id)