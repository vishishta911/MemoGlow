from flask import (
    Flask,
    render_template,
    request,
    session,
    redirect
)

from app.database.db import db

from app.routes.auth import (
    caregiver_signup,
    patient_signup,
    caregiver_login,
    patient_login
)

from app.routes.memory import (
    add_memory,
    get_timeline
)

from app.routes.reminder import (
    add_reminder,
    get_reminders,
    complete_reminder
)

from app.routes.assistant import ask_assistant

from app.models.caregiver import Caregiver
from app.models.patient import Patient
from app.models.connection_request import ConnectionRequest
from app.models.memory import Memory

app = Flask(__name__)

app.config['SECRET_KEY'] = 'memoglow_secret_key_2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memoglow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


# ---------------- API ROUTES ----------------

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


# ---------------- WEB PAGES ----------------

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/role")
def role():
    return render_template("role_selection.html")


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

    if "caregiver_id" not in session:
        return redirect("/login")

    patients = Patient.query.filter_by(
        caregiver_id=session["caregiver_id"]
    ).all()

    return render_template(
        "caregiver_dashboard.html",
        caregiver_name=session.get("caregiver_name"),
        patients=patients
    )


@app.route("/patient/dashboard")
def patient_dashboard():

    if "patient_id" not in session:
        return redirect("/login")

    return render_template(
        "patient_dashboard.html",
        patient_name=session.get("patient_name")
    )


@app.route("/assistant")
def assistant_page():
    return render_template("assistant.html")


@app.route("/add-memory/<int:patient_id>")
def add_memory_page(patient_id):

    return render_template(
        "add_memory.html",
        patient_id=patient_id
    )


@app.route("/add-reminder/<int:patient_id>")
def add_reminder_page(patient_id):

    return render_template(
        "add_reminder.html",
        patient_id=patient_id
    )


@app.route("/memory-timeline")
def memory_timeline_page():

    if "patient_id" not in session:
        return redirect("/login")

    memories = Memory.query.filter_by(
        patient_id=session["patient_id"]
    ).order_by(
        Memory.created_at.desc()
    ).all()

    return render_template(
        "memory_timeline.html",
        memories=memories
    )


@app.route("/family-recognition")
def family_recognition():
    return render_template(
        "family_recognition.html"
    )


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")

from app.models.reminder import Reminder
from app.models.caregiver import Caregiver

@app.route("/patient-profile/<int:patient_id>")
def patient_profile(patient_id):

    patient = Patient.query.get_or_404(patient_id)

    caregiver = Caregiver.query.get(
        patient.caregiver_id
    )

    memory_count = Memory.query.filter_by(
        patient_id=patient.id
    ).count()

    reminder_count = Reminder.query.filter_by(
        patient_id=patient.id
    ).count()

    recent_memories = Memory.query.filter_by(
        patient_id=patient.id
    ).order_by(
        Memory.created_at.desc()
    ).limit(5).all()

    return render_template(
        "patient_profile.html",
        patient=patient,
        caregiver=caregiver,
        memory_count=memory_count,
        reminder_count=reminder_count,
        recent_memories=recent_memories
    )
if __name__ == "__main__":
    app.run(debug=True)