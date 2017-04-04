__author__ = 'Guo'

from models import database
from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, URL


db = database.DataBase()


class LoginForm(Form):
    username = StringField('Username', [DataRequired(), Length(max=255)])
    password = PasswordField('Password', [DataRequired()])

    def validate(self):
        check_validate = super(LoginForm, self).validate()

        # 如果验证没有通过
        if not check_validate:
            return False

        # 检查是否存在拥有该用户名的用户
        is_user = db.find_user_name(self.username.data)
        if not is_user:
            self.username.errors.append(
                'Invalid username or password'
            )
            return False

        is_pass = db.check_pass(self.username.data, self.password.data)
        if not is_pass:
            self.username.errors.append('Invalid username or password')
            return False

        return True




if __name__ == '__main__':
    f = LoginForm()