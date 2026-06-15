# 🧠 MemoGlow AI

## Supporting Memory. Empowering Care.

MemoGlow AI is an intelligent memory assistance and caregiver support system designed for elderly individuals experiencing memory loss or dementia. The platform helps caregivers manage patient memories and reminders while enabling patients to retrieve important information through an AI-powered conversational assistant.

---

## 📌 Project Overview

Dementia patients often struggle to remember daily events, appointments, family interactions, and important activities. MemoGlow AI provides a personalized memory support system that stores memories and reminders and allows patients to retrieve them through natural language conversations.

The system combines:

* Caregiver-assisted memory management
* Reminder scheduling
* AI-powered memory retrieval
* Retrieval-Augmented Generation (RAG)
* Gemini AI integration

---

## 🎯 Objectives

* Assist dementia patients in recalling important memories.
* Provide caregivers with tools to manage patient information.
* Deliver personalized responses using stored memories.
* Improve patient independence through AI-assisted recall.
* Create an accessible and easy-to-use healthcare support platform.

---

## 🚀 Features

### 👨‍⚕️ Caregiver Module

* Caregiver Registration
* Caregiver Login
* Patient Management
* Add Memories
* Add Reminders
* Dashboard Access

### 🧓 Patient Module

* Patient Registration
* Patient Login
* View Reminders
* Access AI Assistant
* Memory Retrieval Support

### 🧠 Memory Management

* Store patient memories
* Categorize memories
* Timeline-based retrieval
* Personalized memory recall

### ⏰ Reminder System

* Add medication reminders
* Add appointment reminders
* Track reminder status
* Reminder completion management

### 🤖 AI Assistant

* Gemini AI Integration
* Memory-based Question Answering
* Personalized Responses
* Retrieval-Augmented Generation (RAG)

Example:

Question:

Who visited me today?

Stored Memory:

Daughter Ananya visited today and brought fruits.

AI Response:

Your daughter Ananya visited you today and brought fruits.

---

## 🏗️ System Architecture

Caregiver → Memory Storage → Database

Patient → AI Assistant → Memory Retrieval → Gemini AI → Response

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

### Backend

* Python
* Flask

### Database

* SQLite
* SQLAlchemy

### Artificial Intelligence

* Google Gemini API
* Sentence Transformers
* Retrieval-Augmented Generation (RAG)

### Machine Learning Libraries

* Sentence Transformers
* NumPy
* FAISS

---

## 📂 Project Structure

```text
MemoGlow
│
├── app.py
│
├── templates
│   ├── home.html
│   ├── role_selection.html
│   ├── login.html
│   ├── caregiver_dashboard.html
│   ├── patient_dashboard.html
│   ├── assistant.html
│   ├── add_memory.html
│   ├── add_reminder.html
│   └── memory_timeline.html
│
├── app
│   ├── database
│   ├── models
│   ├── routes
│   └── services
│
└── memoglow.db
```

---

## 🔐 Authentication

### Caregiver

* Register using email and password
* Secure password hashing
* Unique caregiver code generation

### Patient

* Register using caregiver code
* Secure login authentication

---

## 📊 Current Implementation Status

### Completed

* Database Design
* Authentication System
* Caregiver Dashboard
* Patient Dashboard
* Memory Management
* Reminder Management
* AI Assistant
* Gemini Integration
* RAG-based Retrieval
* Frontend Navigation
* Face Recognition Module

### In Progress

* Memory Timeline UI
* Dynamic Reminder Display
* User Session Management
* UI Enhancements

### Planned

* Voice Assistant
* Speech-to-Text Integration
* Text-to-Speech Responses
* Mobile Application Support

---

## 🔄 Workflow

1. Caregiver registers and logs in.
2. Patient registers using caregiver code.
3. Caregiver adds memories and reminders.
4. Information is stored in the database.
5. Patient interacts with MemoGlow Assistant.
6. Relevant memories are retrieved.
7. Gemini AI generates personalized responses.

---

## 💡 Future Enhancements

* Voice-enabled interaction
* Family member access
* Calendar integration
* Medical record integration
* Face recognition for family members
* Mobile application deployment

---

## 👨‍💻 Developed By

K. Vishishta Reddy
Mini Project – Artificial Intelligence & Machine Learning

---
