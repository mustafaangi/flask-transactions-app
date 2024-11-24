from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, DateField
from wtforms.validators import DataRequired

class TransactionForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')