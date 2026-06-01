from flask import request, jsonify

from app.database.db import db
from app.models.reminder import Reminder
from app.models.patient import Patient


def add_reminder():

    data = request.get_json()

    patient_id = data.get("patient_id")
    reminder_text = data.get("reminder_text")
    reminder_time = data.get("reminder_time")

    patient = Patient.query.get(patient_id)

    if not patient:
        return jsonify({
            "message": "Patient not found"
        }), 404

    reminder = Reminder(
        patient_id=patient_id,
        reminder_text=reminder_text,
        reminder_time=reminder_time
    )

    db.session.add(reminder)
    db.session.commit()

    return jsonify({
        "message": "Reminder Added Successfully"
    })
def get_reminders(patient_id):

    reminders = Reminder.query.filter_by(
        patient_id=patient_id
    ).all()

    result = []

    for reminder in reminders:
        result.append({
            "id": reminder.id,
            "reminder_text": reminder.reminder_text,
            "reminder_time": reminder.reminder_time,
            "status": reminder.status
        })

    return jsonify(result)
def complete_reminder(reminder_id):

    reminder = Reminder.query.get(reminder_id)

    if not reminder:
        return jsonify({
            "message": "Reminder not found"
        }), 404

    reminder.status = "Completed"

    db.session.commit()

    return jsonify({
        "message": "Reminder Completed"
    })