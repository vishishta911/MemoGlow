from flask import session
from flask import request, jsonify
from werkzeug.security import generate_password_hash
import random

from app.database.db import db
from app.models.caregiver import Caregiver
from werkzeug.security import check_password_hash

def generate_caregiver_code():
    return f"CG-{random.randint(100000,999999)}"


def caregiver_signup():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    password = data.get("password")

    existing = Caregiver.query.filter_by(email=email).first()

    if existing:
        return jsonify({
            "message": "Email already exists"
        }), 400

    caregiver = Caregiver(
        name=name,
        email=email,
        phone=phone,
        password=generate_password_hash(password),
        caregiver_code=generate_caregiver_code()
    )

    db.session.add(caregiver)
    db.session.commit()

    return jsonify({
        "message": "Registration Successful",
        "caregiver_code": caregiver.caregiver_code
    })

from app.models.patient import Patient
from werkzeug.security import generate_password_hash


def patient_signup():

    data = request.get_json()

    name = data.get("name")
    age = data.get("age")
    password = data.get("password")
    caregiver_code = data.get("caregiver_code")

    caregiver = Caregiver.query.filter_by(
        caregiver_code=caregiver_code
    ).first()

    if not caregiver:
        return jsonify({
            "message": "Invalid Caregiver Code"
        }), 400

    patient = Patient(
        name=name,
        age=age,
        password=generate_password_hash(password),
        caregiver_id=caregiver.id
    )

    db.session.add(patient)
    db.session.commit()

    return jsonify({
        "message": "Patient Registered Successfully"
    })
def caregiver_login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    caregiver = Caregiver.query.filter_by(
        email=email
    ).first()

    if not caregiver:
        return jsonify({
            "message": "Caregiver not found"
        }), 404

    if not check_password_hash(
        caregiver.password,
        password
    ):
        return jsonify({
            "message": "Invalid password"
        }), 401

    session["caregiver_id"] = caregiver.id
    session["caregiver_name"] = caregiver.name

    return jsonify({
        "message": "Login Successful",
        "caregiver_id": caregiver.id,
        "caregiver_code": caregiver.caregiver_code
    })
def patient_login():

    data = request.get_json()

    name = data.get("name")
    password = data.get("password")

    patient = Patient.query.filter_by(
        name=name
    ).first()

    if not patient:
        return jsonify({
            "message": "Patient not found"
        }), 404

    if not check_password_hash(
        patient.password,
        password
    ):
        return jsonify({
            "message": "Invalid password"
        }), 401

    session["patient_id"] = patient.id
    session["patient_name"] = patient.name

    return jsonify({
        "message": "Login Successful",
        "patient_id": patient.id,
        "caregiver_id": patient.caregiver_id
    })