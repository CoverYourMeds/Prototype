from CoverYourMeds import db


class User(db.Model):
    __tablename__ = "users"
    username = db.Column(db.VARCHAR(50), primary_key=True, nullable=False, unique=True)
    password = db.Column(db.VARCHAR(50), nullable=False)
    type = db.Column(db.VARCHAR(30), nullable=False)


class Doctor(db.Model):
    __tablename__ = "doctors"
    doc_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    name = db.Column(db.VARCHAR(150), nullable=False)


class Medication(db.Model):
    __tablename__ = "meds"
    med_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    name = db.Column(db.VARCHAR(150), nullable=False)
    pills = db.Column(db.Integer)
    refill_date = db.Column(db.VARCHAR(35))
    doc_id = db.Column(db.Integer, db.ForeignKey("doctors.doc_id"))
    username = db.Column(db.VARCHAR(50))

    doctor = db.relationship(Doctor, backref=db.backref("doctor", uselist=False))

    def __init__(self, name, pills, refill_date, doc_id, username):
        self.name = name
        self.pills = pills
        self.refill_date = refill_date
        self.doc_id = doc_id
        self.username = username


class Times(db.Model):
    __tablename__ = "times"
    time_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    time = db.Column(db.Integer)
    medication = db.Column(db.Integer, db.ForeignKey("meds.med_id"), nullable=False)
    sun = db.Column(db.Boolean)
    mon = db.Column(db.Boolean)
    tues = db.Column(db.Boolean)
    wed = db.Column(db.Boolean)
    thur = db.Column(db.Boolean)
    fri = db.Column(db.Boolean)
    sat = db.Column(db.Boolean)


class MissedMedications(db.Model):
    __tablename__ = "missed_medications"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
