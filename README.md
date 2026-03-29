# 🎤 Voice Query AI - Speech-to-SQL System

An AI-powered system that converts **voice commands into SQL queries** and fetches results from a database using a local LLM (DeepSeek via Ollama).

---

## 🚀 Features

* 🎤 Speech-to-Text (Google Speech Recognition)
* 🧠 Natural Language → SQL (DeepSeek LLM)
* 🗄 Database Query Execution (SQLite)
* 🌐 Interactive UI (Streamlit)
* ⚡ Fully Local LLM using Ollama

---

## 🧠 Architecture

Voice → Text → LLM → SQL → Database → Results

---

## 🛠 Tech Stack

* Python
* Streamlit
* SpeechRecognition
* Ollama (DeepSeek-R1)
* SQLite
* Pandas

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/voice-to-sql-ai.git
cd voice-to-sql-ai
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Install Ollama & Model

Download Ollama: https://ollama.com

```bash
ollama pull deepseek-r1:1.5
ollama serve
```

---

### 4. Create Database

```bash
python create_db.py
```

---

### 5. Run Application

```bash
streamlit run app.py
```

---

## 🎤 Example Queries

* "Show all employees"
* "List IT department employees"
* "Show employees with salary above 50000"

---

## 📁 Project Structure

```
voice-to-sql-ai/
│── app.py
│── create_db.py
│── db.py
│── llm_to_sql.py
│── speech_to_text.py
│── schema.txt
│── sample_db.sqlite
│── requirements.txt
│── README.md
```

---

## 🧪 Future Improvements

* Multi-table support
* Query validation (security)
* Better UI (charts & analytics)
* Deploy online (Streamlit Cloud)

---

## 👨‍💻 Author

Ganesh B

---

## ⭐ Give a Star

If you like this project, give it a ⭐ on GitHub!
