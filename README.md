# Connectinno Notes App Backend

[Türkçe Versiyon](README.tr.md)

This is a backend service for the Connectinno Notes App developed using **FastAPI**.

---

## 🚀 Project Features

* **Note Management:** Provides Create, Read, Update, and Delete (CRUD) functionalities for notes.
* **Firebase Authentication:** All API endpoints are secured using Firebase ID tokens.
* **Easy Setup:** Quickly gets up and running with minimal setup steps.
* **API Documentation:** Automatically generated interactive API documentation (`/docs`) makes it easy for developers.

---

## 🛠️ Technologies Used

* **FastAPI:** A high-performance and easy-to-use Python web framework.
* **Firebase Admin SDK:** To verify user ID tokens and access the Firestore database.
* **Uvicorn:** As an asynchronous server.
* **Python Decouple:** For managing environment variables.

---

## 🏁 Getting Started

Follow these steps to get the project running on your local machine.

### Firebase Setup

This backend utilizes Firebase Firestore and Firebase Authentication services.

1.  **Firebase Project:** Go to the [Firebase Console](https://console.firebase.google.com/) and create a new project.
2.  **Service Account:** Navigate to Project Settings → Service Accounts and click "Generate new private key."
3.  **Key File:** Save the downloaded JSON file in the project's `app/` directory as **`firebase_key.json`**.
4.  **Authentication:** In the Firebase Console, go to **Authentication** and enable **Email/Password** sign-in.
5.  **Database:** Create a Firestore Database and start it in "test mode" for development.

### Project Setup

1.  Create and activate a virtual environment in the project directory:
```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
```
2.  Install the required Python packages:
```bash
    pip install -r requirements.txt
```
3.  **Environment Variables:** Rename `.env.example` to `**`.env`**` and update the path to your Firebase key file as follows:
```
    FIREBASE_CREDENTIALS_JSON=app/firebase_key.json
```

---

## ▶️ Running the Server

```bash
uvicorn app.main:app --reload
```

⚠️ **TEST NOTE FOR Swager UI**

- The `/test/create_user` and `/test/signin` endpoints are **for testing purposes only**.
- These endpoints are provided to create test users without a frontend.
- In the actual application, user registration, login, and logout are handled through the frontend.

## 📄 API Documentation & Authentication

API documentation is accessible at `**/docs**` when the server is running.

* **Swagger UI:** The interactive API documentation is located at `**/docs**`.
* **Authentication:** To access secured endpoints, you must send an `Authorization: Bearer <ID token>` in the request header.

**⚠️ IMPORTANT: Test Endpoints**
>
> The `**/test/create_user**` and `**/test/signin**` endpoints are **for testing purposes only**. They are provided to create test users without a frontend. In a production environment, user registration, login, and logout should be handled exclusively through the frontend.

