import firebase_admin
from firebase_admin import credentials, firestore, auth
import os

cred = credentials.Certificate(os.getenv("FIREBASE_CREDENTIALS_JSON"))
firebase_admin.initialize_app(cred)
db = firestore.client()
