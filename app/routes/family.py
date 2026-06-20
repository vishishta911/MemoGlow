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


def get_family_members(patient_id):

    members = FamilyMember.query.filter_by(
        patient_id=patient_id
    ).all()

    result = []

    for member in members:

        result.append({
            "id": member.id,
            "name": member.name,
            "relationship": member.relationship
        })

    return jsonify(result)


def delete_family_member(member_id):

    member = FamilyMember.query.get(member_id)

    if not member:
        return jsonify({
            "message": "Family Member Not Found"
        }), 404

    db.session.delete(member)
    db.session.commit()

    return jsonify({
        "message": "Family Member Deleted"
    })