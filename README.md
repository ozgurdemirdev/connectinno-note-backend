# Connectinno Notes Backend

FastAPI backend for Connectinno Notes App.

## Firebase Setup

1. Go to https://console.firebase.google.com/ and create a new project (e.g., "Connectinno Notes Backend").
2. Create a Firestore database (start in test mode for development).
3. Go to Project Settings → Service Accounts → Generate new private key.
4. Save the downloaded JSON file in the project: app/firebase_key.json
5. Copy .env.example to .env and set the path to your Firebase key:

   FIREBASE_CREDENTIALS_JSON=app/firebase_key.json

## Setup

1. Create a virtual environment:
```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
```
    

2. Install requirements:
```
pip install -r requirements.txt
```

3. Add Firebase credentials in .env (see .env.example)

4. Run the server:
```
    uvicorn app.main:app --reload
```
