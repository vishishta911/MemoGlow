from flask import request, jsonify

from app.database.db import db
from app.models.memory import Memory
from app.models.patient import Patient


def add_memory():

    data = request.get_json()

    patient_id = data.get("patient_id")
    memory_text = data.get("memory_text")
    category = data.get("category")

    patient = Patient.query.get(patient_id)

    if not patient:
        return jsonify({
            "message": "Patient not found"
        }), 404

    memory = Memory(
        patient_id=patient_id,
        memory_text=memory_text,
        category=category
    )

    db.session.add(memory)
    db.session.commit()

    return jsonify({
        "message": "Memory Added Successfully"
    })
def get_timeline(patient_id):

    memories = Memory.query.filter_by(
        patient_id=patient_id
    ).order_by(
        Memory.created_at.desc()
    ).all()

    timeline = []

    for memory in memories:
        timeline.append({
            "id": memory.id,
            "memory": memory.memory_text,
            "category": memory.category,
            "created_at": str(memory.created_at)
        })

    return jsonify(timeline)