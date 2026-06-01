from flask import Flask
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

@app.route('/')
def home():
    return "MemoGlow AI Running Successfully"

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
if __name__ == '__main__':
    app.run(debug=True)