from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pitches= db.relationship('Pitch',backref='user',lazy="dynamic")

    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User{self.username}'

class Pitch(db.Model):
    __tablename__='pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer)
    pitch_title = db.Column(db.String)
    pitch_body = db.Column(db.String)
    category= db.Column(db.String)
    like = db.Column(db.Integer)
    dislike = db.Column(db.Integer)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.filter_by(pitch_id=id).all()
        return pitches

class Review(db.Model):

    __tablename__ ='reviews'

    id = db.Column(db.Integer,primary_key = True)
    review = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"Review('{self.review}', '{self.posted}')"

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref='role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'