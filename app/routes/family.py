from flask import request, jsonify
from app.database.db import db
from app.models.family_member import FamilyMember

def add_family_member():

    data = request.get_json()

    member = FamilyMember(
        patient_id=data["patient_id"],
        name=data["name"],
        relationship=data["relationship"]
    )

    db.session.add(member)
    db.session.commit()

    return jsonify({
        "message": "Family Member Added"
    })