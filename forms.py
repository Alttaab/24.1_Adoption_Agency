"""Forms for our demo Flask app."""

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, IntegerField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length

PET_SPECIES = ['cat','dog','porcupine']
MAX_PET_AGE = 50

class AddPetForm(FlaskForm):
    """Form for adding pets"""
    
    name = StringField("Name",
        validators=[InputRequired()])
    species = SelectField("Species",choices=PET_SPECIES)
    photo_url = StringField("Photo (URL)",
                            validators=[Optional(),URL()])
    age = IntegerField("Age",
                       validators=[Optional(),NumberRange(min=0, max=MAX_PET_AGE)])
    notes = StringField("Additional notes",
                        validators=[Optional(),Length(min=2)])

class EditPetForm(FlaskForm):
    """Form for editing pets"""
    
    photo_url = StringField("Photo (URL)",
                            validators=[Optional(),URL()])
    notes = StringField("Additional notes",
                        validators=[Optional(),Length(min=2)])
    available = BooleanField("Available")
    