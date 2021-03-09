from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class DataInput(FlaskForm):
    house_price = IntegerField('House Price', validators=[DataRequired(), NumberRange(min=0)])

    submit = SubmitField('Calculate Tax')

