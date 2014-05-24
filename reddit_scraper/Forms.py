from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

__author__ = 'dylan'


class UserNameForm(Form):
    user = StringField("Please enter user name", validators=[Required()])
    submit = SubmitField('Find User')
