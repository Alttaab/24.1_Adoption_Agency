from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, render_template, redirect, flash
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

connect_db(app)

app.config['SECRET_KEY'] = "pass"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route("/")
def show_all_pets():
    """Shows all pets in alphabetical order"""
    pets = Pet.query.order_by('name').all()
    return render_template('index.html',pets=pets)

@app.route("/add", methods=["GET","POST"])
def show_add_form():
    """Add Pet form; Handles showing and adding pets using the AddPetForm()"""
    
    form = AddPetForm()
    
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect(f"/pets/{new_pet.id}")
    
    return render_template("pet_add_form.html",form=form)

@app.route("/pets/<int:pet_id>", methods=["GET","POST"])
def show_pet_details_form(pet_id):
    """Pet Details and Edit Pet form; Handles showing and editing pets using the EditPetForm()"""
    
    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data,
        pet.notes = form.notes.data,
        pet.available = form.available.data
        db.session.commit()
        flash(f"{pet.name} edited.")
        return redirect(f"/pets/{pet.id}")
    
    return render_template("pet_details.html",pet=pet,form=form)