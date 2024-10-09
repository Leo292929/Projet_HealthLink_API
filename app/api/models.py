from app.extensions import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(db.Date)
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    gender = db.Column(db.String(255))
    digitalprint = db.Column(db.String(255))
    eye_color = db.Column(db.String(255))
    photo_identity = db.Column(db.String(255))
    mutual_name = db.Column(db.String(255))
    social_security_number = db.Column(db.String(255))
    additional_infos = db.Column(db.String(255))
    id_address = db.Column(db.Integer, db.ForeignKey('address.id'))

    # Relations
    address = db.relationship('Address', back_populates='user')
    healthfolder = db.relationship('HealthFolder', uselist=False, back_populates='user')
    handicaps = db.relationship('Handicap', back_populates='user')
    treatments = db.relationship('Treatment', back_populates='user')
    vaccinations = db.relationship('Vaccination', back_populates='user')

class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True)
    zip_code = db.Column(db.Integer)
    city = db.Column(db.String(255))
    street = db.Column(db.String(255))
    street_number = db.Column(db.Integer)
    appt_number = db.Column(db.Integer)

    # Relations
    user = db.relationship('User', back_populates='address')
    medical_examinations = db.relationship('MedicalExamination', back_populates='address')

class HealthFolder(db.Model):
    __tablename__ = 'healthfolder'
    id = db.Column(db.Integer, primary_key=True)
    family_medical_history = db.Column(db.String(255))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Relation
    user = db.relationship('User', back_populates='healthfolder')

class Handicap(db.Model):
    __tablename__ = 'handicap'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    is_temporary = db.Column(db.Boolean)
    is_hereditary = db.Column(db.Boolean)
    is_physical = db.Column(db.Boolean)
    is_mental = db.Column(db.Boolean)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Relation
    user = db.relationship('User', back_populates='handicaps')

class Treatment(db.Model):
    __tablename__ = 'treatment'
    id = db.Column(db.Integer, primary_key=True)
    medication_name = db.Column(db.String(255))
    dosage = db.Column(db.String(255))
    prescription_date = db.Column(db.Date)
    duration_day = db.Column(db.Integer)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Relation
    user = db.relationship('User', back_populates='treatments')

class Vaccination(db.Model):
    __tablename__ = 'vaccination'
    id = db.Column(db.Integer, primary_key=True)
    vaccin_name = db.Column(db.String(255))
    date = db.Column(db.Date)
    recall_date = db.Column(db.Date)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Relation
    user = db.relationship('User', back_populates='vaccinations')

class MedicalExamination(db.Model):
    __tablename__ = 'medicalexamination'
    id = db.Column(db.Integer, primary_key=True)
    practice = db.Column(db.String(255))
    date = db.Column(db.Date)
    report = db.Column(db.Text)
    id_address = db.Column(db.Integer, db.ForeignKey('address.id'))
    id_pro = db.Column(db.Integer, db.ForeignKey('pro.id'))
    id_result = db.Column(db.Integer, db.ForeignKey('result.id'))

    # Relations
    address = db.relationship('Address', back_populates='medical_examinations')

class Pro(db.Model):
    __tablename__ = 'pro'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255))
    rpps_number = db.Column(db.Integer)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    password = db.Column(db.String(255))

class Result(db.Model):
    __tablename__ = 'result'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255))
    result = db.Column(db.Boolean)
