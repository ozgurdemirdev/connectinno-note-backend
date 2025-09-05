from app.firebase import db
from datetime import datetime

COLLECTION = "notes"

def create_note(user_id, data):
    doc_ref = db.collection(COLLECTION).document()
    note_data = {
        "title": data.title,
        "content": data.content,
        "user_id": user_id,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    doc_ref.set(note_data)
    return {**note_data, "id": doc_ref.id}

def get_notes(user_id):
    notes = db.collection(COLLECTION).where("user_id", "==", user_id).stream()
    return [{**n.to_dict(), "id": n.id} for n in notes]

def update_note(user_id, note_id, data):
    doc_ref = db.collection(COLLECTION).document(note_id)
    doc = doc_ref.get()
    if not doc.exists or doc.to_dict()["user_id"] != user_id:
        return None
    updated_data = {k: v for k, v in data.dict().items() if v is not None}
    updated_data["updated_at"] = datetime.utcnow()
    doc_ref.update(updated_data)
    return {**doc_ref.get().to_dict(), "id": note_id}

def delete_note(user_id, note_id):
    doc_ref = db.collection(COLLECTION).document(note_id)
    doc = doc_ref.get()
    if not doc.exists or doc.to_dict()["user_id"] != user_id:
        return False
    doc_ref.delete()
    return True
