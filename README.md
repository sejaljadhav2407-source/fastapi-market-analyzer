# 🚀 AI Market Analyzer API

An AI-powered API that analyzes **Indian market sectors** and provides **trends and business opportunities** using **Google Gemini AI**.

Built using **FastAPI**, this project allows users to analyze different sectors like technology, finance, healthcare, etc.

---

# 📌 Features

- AI-powered market analysis
- FastAPI REST API
- Google Gemini AI integration
- JWT authentication support
- Market news data collector
- Modular and clean project structure

---

# 📂 Project Structure

```
AI-Market-Analyzer
│
├── main.py              # FastAPI application
├── ai_analysis.py       # AI analysis logic
├── data_collector.py    # Collects market news/data
├── auth.py              # JWT authentication logic
├── model.py             # Pydantic request models
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/ai-market-analyzer.git
cd ai-market-analyzer
```

---

## 2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3️⃣ Install dependencies

```bash
pip install fastapi uvicorn python-jose requests google-genai
```

---

# ▶️ Run the API

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# 🌐 API Endpoints

## Home Endpoint

```
GET /
```

Response

```json
{
  "message": "AI Market Analyzer API running"
}
```

---

## Analyze Market Sector

```
GET /analyze/{sector}
```

Example request:

```
/analyze/technology
```

Example response:

```json
{
  "sector": "technology",
  "analysis": "AI generated trends and opportunities for the sector..."
}
```

---

# 🛠 Technologies Used

- Python
- FastAPI
- Google Gemini AI
- Pydantic
- JWT Authentication
- Requests

---

# 🔒 Security Note

Do **NOT expose API keys in public repositories**.

Use environment variables instead:

```python
import os

API_KEY = os.getenv("GEMINI_API_KEY")
```

---

# 🚧 Future Improvements

- Real-time market data integration
- News scraping system
- Web dashboard
- Database for storing analysis history
- Full authentication system

---

# 👨‍💻 Author

Developed by **sejal jadhav**
