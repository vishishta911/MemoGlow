from flask import request, jsonify, session
from app.models.memory import Memory
from app.services.gemini_service import ask_gemini
from app.services.rag_service import create_embeddings
import numpy as np


def ask_assistant():

    if "patient_id" not in session:
        return jsonify({
            "answer": "Please login first."
        }), 401

    data = request.get_json()

    patient_id = session["patient_id"]
    question = data.get("question")

    memories = Memory.query.filter_by(
        patient_id=patient_id
    ).all()

    memory_texts = [
        memory.memory_text
        for memory in memories
    ]

    if not memory_texts:
        return jsonify({
            "answer": "No memories found."
        })

    memory_embeddings = create_embeddings(
        memory_texts
    )

    question_embedding = create_embeddings(
        [question]
    )[0]

    similarities = np.dot(
        memory_embeddings,
        question_embedding
    )

    best_match_index = np.argmax(
        similarities
    )

    relevant_memory = memory_texts[
        best_match_index
    ]

    answer = ask_gemini(
        relevant_memory,
        question
    )

    return jsonify({
        "retrieved_memory": relevant_memory,
        "answer": answer
    })