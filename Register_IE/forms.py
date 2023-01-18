from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from datetime import date

class MovementsForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired(message="The date is required")])
    concept = StringField('Concept', validators=[DataRequired("The concept is required"), Length(min=4, message="Text more than 4 characters please")])
    quantity = FloatField('Quantity', validators=[DataRequired(message="Quantity is required, bigger than 0")])

    submit = SubmitField('Accept')

    def validate_date(form, field):
        if field.data > date.today():
            raise ValidationError("The introduced date is not valid")