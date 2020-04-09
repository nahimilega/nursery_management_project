# Import Form and RecaptchaField (optional)
# , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
# BooleanField

# Import Form validators
from wtforms.validators import Required, Email, EqualTo
from wtforms import TextField, Form, BooleanField, StringField, PasswordField, validators, IntegerField, FloatField
from wtforms.fields.core import RadioField, SelectField


# Define the login form (WTForms)

class registerNurseryForm(Form):
    pincode = IntegerField('Pincode', [validators.NumberRange(min=100000, max=999999), validators.DataRequired()])
    city = StringField('City', [validators.Length(min=1, max=100), validators.DataRequired(),])
    country = StringField('Country', [validators.Length(min=1, max=100), validators.DataRequired(),])
    labour = FloatField('Labour Cost', [validators.DataRequired()])
    maintenance = FloatField('Maintenance Cost', [validators.DataRequired()])