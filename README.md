### Prerequisites

Python 3.9 or later

Virtualenv

### Getting Started

**Create virtual environment and activate it**
```
python3 -m venv venv
source venv/bin/activate
```

**Install dependencies**
```
pip install -r requirements.txt
```

**Set environment variablesCreate a .env file:**
```
OPENAI_API_KEY=your_openai_key
MONGO_URI=your_mongodb_uri
```

**Run the server**
```
uvicorn app.main:app --reload
```

**Test the API locally**
Visit: http://127.0.0.1:8000/docs

### 🌍 Deployment Notes

Python backend can be deployed on platforms like Render, Railway, or Fly.io.

MongoDB Atlas should allow IP access (be cautious with 0.0.0.0/0 in production).

Ensure App Group and Widget Extension provisioning are set correctly for TestFlight/App Store builds.

### Powered By

🧠 OpenAI (for motivational messaging)

📦 MongoDB Atlas

🐍 FastAPI

📱 Flutter + Swift (WidgetKit)
