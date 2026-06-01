from app.database.db import db

class Patient(db.Model):
    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    age = db.Column(db.Integer)

    password = db.Column(db.String(255), nullable=False)

    caregiver_id = db.Column(
        db.Integer,
        db.ForeignKey('caregivers.id')
    )

    dementia_stage = db.Column(
        db.String(20),
        default='Mild'
    )