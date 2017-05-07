__author__ = 'Guo'

from movieapp.models import database
from flask_sqlalchemy import SQLAlchemy

userdb = SQLAlchemy.create_engine('sqlite:///../database_user.db')
db = database.DataBase()
userdb.User.query.all()
'''
def updateuser():
    users = User.query.all()
    print(users)

'''
# if __name__ == '__main__':
    # updateuser()