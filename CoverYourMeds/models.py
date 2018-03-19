from CoverYourMeds import db


class Medication(db.Model):
    __tablename__ = "meds"
    med_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    name = db.Column(db.VARCHAR(150), nullable=False)
