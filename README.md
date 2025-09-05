# Connectinno Notes Backend

FastAPI backend for Connectinno Notes App.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv\Scripts\activate  # use for Mac / Linux: venv/bin/activate

2. Install requirements:
    pip install -r requirements.txt

3. Add Firebase credentials in .env (see .env.example)

4. Run the server:
    uvicorn app.main:app --reload
