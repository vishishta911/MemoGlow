from app.database.db import db

class ConnectionRequest(db.Model):
    __tablename__ = "connection_requests"

    id = db.Column(db.Integer, primary_key=True)

    patient_name = db.Column(db.String(100))

    caregiver_code = db.Column(db.String(20))

    status = db.Column(
        db.String(20),
        default='Pending'
    )