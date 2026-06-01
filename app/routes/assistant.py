from flask import request, jsonify

from app.models.memory import Memory
from app.services.gemini_service import ask_gemini


def ask_assistant():

    data = request.get_json()

    patient_id = data.get("patient_id")
    question = data.get("question")

    memories = Memory.query.filter_by(
        patient_id=patient_id
    ).all()

    context = "\n".join(
        [memory.memory_text for memory in memories]
    )

    answer = ask_gemini(
        context,
        question
    )

    return jsonify({
        "answer": answer
    })