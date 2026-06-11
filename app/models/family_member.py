from app.database.db import db

class FamilyMember(db.Model):

    __tablename__ = "family_members"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    patient_id = db.Column(
        db.Integer,
        db.ForeignKey("patients.id"),
        nullable=False
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    relationship = db.Column(
        db.String(100),
        nullable=False
    )

    photo_path = db.Column(
        db.String(255)
    )