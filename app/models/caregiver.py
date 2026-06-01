from app.database.db import db

class Caregiver(db.Model):
    __tablename__ = "caregivers"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    phone = db.Column(db.String(20))

    password = db.Column(db.String(255), nullable=False)

    caregiver_code = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )