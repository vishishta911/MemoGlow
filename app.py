from flask import Flask, render_template, request
from app.database.db import db
from app.routes.auth import (
    caregiver_signup,
    patient_signup,
    caregiver_login,
    patient_login
)
from app.routes.memory import add_memory, get_timeline
app = Flask(__name__)

app.config['SECRET_KEY'] = 'memoglow_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memoglow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from app.models.caregiver import Caregiver
from app.models.patient import Patient
from app.models.connection_request import ConnectionRequest
from app.models.memory import Memory
from app.routes.reminder import (
    add_reminder,
    get_reminders,
    complete_reminder
)
from app.routes.assistant import ask_assistant
with app.app_context():
    db.create_all()

# @app.route('/')
# def home():
#     return "MemoGlow AI Running Successfully"

app.add_url_rule(
    '/caregiver/signup',
    view_func=caregiver_signup,
    methods=['POST']
)
app.add_url_rule(
    '/patient/signup',
    view_func=patient_signup,
    methods=['POST']
)
app.add_url_rule(
    '/caregiver/login',
    view_func=caregiver_login,
    methods=['POST']
)
app.add_url_rule(
    '/patient/login',
    view_func=patient_login,
    methods=['POST']
)
app.add_url_rule(
    '/memory/add',
    view_func=add_memory,
    methods=['POST']
)
app.add_url_rule(
    '/memory/timeline/<int:patient_id>',
    view_func=get_timeline,
    methods=['GET']
)
app.add_url_rule(
    '/reminder/add',
    view_func=add_reminder,
    methods=['POST']
)
app.add_url_rule(
    '/reminder/all/<int:patient_id>',
    view_func=get_reminders,
    methods=['GET']
)
app.add_url_rule(
    '/reminder/complete/<int:reminder_id>',
    view_func=complete_reminder,
    methods=['PUT']
)
app.add_url_rule(
    '/assistant/ask',
    view_func=ask_assistant,
    methods=['POST']
)
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/role")
def role():
    return render_template("role_selection.html")


from flask import request

@app.route("/login")
def login():

    role = request.args.get("role")

    return render_template(
        "login.html",
        role=role
    )

@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/caregiver/dashboard")
def caregiver_dashboard():
    return render_template("caregiver_dashboard.html")


@app.route("/patient/dashboard")
def patient_dashboard():
    return render_template("patient_dashboard.html")


@app.route("/assistant")
def assistant_page():
    return render_template("assistant.html")
@app.route("/add-memory")
def add_memory_page():
    return render_template("add_memory.html")
@app.route("/add-reminder")
def add_reminder_page():
    return render_template("add_reminder.html")
@app.route("/memory-timeline")
def memory_timeline_page():
    return render_template("memory_timeline.html")
@app.route("/family-recognition")
def family_recognition():
    return render_template("family_recognition.html")
if __name__ == '__main__':
    app.run(debug=True)