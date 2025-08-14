# app/listings/forms.py (Corrected validators for optional fields)

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, SelectField, SubmitField
# Make sure to import Optional from wtforms.validators!
from wtforms.validators import DataRequired, Length, Optional, URL, Email 
from ..models import Category

class ListingForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=120)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=1)])
    category = SelectField('Category', coerce=int, validators=[DataRequired()])
    location = StringField('Location (e.g., "Cuenca - El Centro")', validators=[Optional(), Length(max=120)])
    contact_email = StringField('Contact Email', validators=[Optional(), Email()]) 
    contact_phone = StringField('Contact Phone', validators=[Optional(), Length(max=60)])
    price = FloatField('Price (Optional)', validators=[Optional()])    
    tags = StringField('Tags', render_kw={"placeholder": "e.g., pet-friendly, furnished, new"})
    submit = SubmitField('Submit Listing')

    def __init__(self, *args, **kwargs):
        super(ListingForm, self).__init__(*args, **kwargs)
        self.category.choices = [(c.id, c.name) for c in Category.query.order_by('name').all()]