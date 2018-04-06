from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    '''
    表单的验证字段，当然除了表单以外其他地方用到验证也可以使用此模块
    '''
    username = StringField(label='Username', validators=[DataRequired(), Length(min=3)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')