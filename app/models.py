from . import db
from werkzeug.security import generate_password_hash


class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    history=db.Column(db.String(255))
    date_=db.Column(db.DATETIME)
    status=db.Column(db.String(25))
    symptom_id=db.Column(db.Integer,foreign_key=('symptom.id'))
    ailment_id=db.Column(db.Integer,foreign_key=('ailment.id'))

    def __init__(self, first_name, last_name, username, password,history,date_,status,symptom_id,ailment_id):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(
            password, method='pbkdf2:sha256')
        self.history=history
        self.date_=date_
        self.status=status
        self.symptom_id=symptom_id
        self.ailment_id=ailment_id


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)

class Symptoms(db.Model):
    __bind_key__='db2'
    __tablename__='symptoms'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    desc = db.Column(db.String(255))
    types = db.Column(db.String(20))
    priority = db.Column(db.String(40))

    def __init__(self,name,desc,types,priority):
        self.name=name
        self.desc=desc
        self.types=types
        self.priority=priority


class Ailment(db.Model):
    __bind_key__='db3'
    __tablename__='ailment'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    sci_name = db.Column(db.String(80))
    desc = db.Column(db.String(255))
    types = db.Column(db.String(20))
    severity = db.Column(db.String(40))
    symptom_id = db.Column(db.Integer,foreign_key=('symptoms.id'))
    treatment_id = db.Column(db.Integer,foreign_key=('treatments.id'))

    def __init__(self,name,sci_name,desc,types,severity,symptom_id,treatment_id):
        self.name=name
        self.sci_name=sci_name
        self.desc=desc
        self.types=types
        self.severity=severity
        self.symptom_id=symptom_id
        self.treatment_id=treatment_id

class Treatments(db.Model):
    __bind_key__='db4'
    __tablename__='treatments'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    details = db.Column(db.String(255)) 

    def __init__(self,name,details):
        self.name = name
        self.details = details

class Emer_contacts(db.Model):
    __bind_key__='db5'
    __tablename__ = 'emer_contacts'
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    phone = db.Column(db.String(15))
    relationship = db.Column(db.String(15))
    user_id = db.Column(db.Integer,foreign_key=UserProfile.id)
    
    def __init__(self,first_name,last_name,phone,relationship,user_id):
        self.first_name=first_name
        self.last_name=last_name
        self.phone=phone
        self.relationship=relationship
        self.user_id=user_id

