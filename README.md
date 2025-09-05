# Connectinno Notes Backend

FastAPI backend for Connectinno Notes App.

## Firebase Setup

1. Go to https://console.firebase.google.com/ and create a new project (e.g., "Connectinno Notes Backend").
2. Create a Firestore database (start in test mode for development).
3. Go to Project Settings → Service Accounts → Generate new private key.
4. Save the downloaded JSON file in the project: app/firebase_key.json
5. Copy .env.example to .env and set the path to your Firebase key:

   FIREBASE_CREDENTIALS_JSON=app/firebase_key.json

### Firebase Authentication Setup

1. In the Firebase Console, go to **Authentication → Sign-in method**.
2. Enable **Email/Password** sign-in.
3. (Optional) Enable **Google** sign-in if you plan to use Google login in the frontend.
4. Make sure the backend is configured to verify Firebase ID tokens using `firebase_key.json`.
5. When calling secured endpoints (`/notes`), include the `Authorization: Bearer <ID token>` header obtained from the frontend after login.

## Setup

1. Create a virtual environment:
```bash
    python -m venv venv
```
    # Windows
```bash
    venv\Scripts\activate
```
    # Mac/Linux
```bash
    source venv/bin/activate
```

    

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Add Firebase credentials in .env (see .env.example)

4. Run the server:
```bash
    uvicorn app.main:app --reload
```

## API Documentation

- Swagger UI is accessible at `/docs`.
- There is no Authorization button; when calling the endpoints, you must include the header: Authorization: Bearer <ID token>


⚠️ **TEST NOTE FOR Swager UI**

- The `/test/create_user` and `/test/signin` endpoints are **for testing purposes only**.
- These endpoints are provided to create test users without a frontend.
- In the actual application, user registration, login, and logout are handled through the frontend.

