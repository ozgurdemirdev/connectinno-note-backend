from fastapi import FastAPI, Depends, HTTPException
from app import crud, schemas

app = FastAPI()

# Dummy user_id, ileride auth ile değişecek
def get_current_user():
    return "user_123"

@app.post("/notes", response_model=schemas.NoteOut)
def create_note(note: schemas.NoteCreate, user_id: str = Depends(get_current_user)):
    return crud.create_note(user_id, note)

@app.get("/notes", response_model=list[schemas.NoteOut])
def list_notes(user_id: str = Depends(get_current_user)):
    return crud.get_notes(user_id)

@app.put("/notes/{note_id}", response_model=schemas.NoteOut)
def update_note(note_id: str, note: schemas.NoteUpdate, user_id: str = Depends(get_current_user)):
    updated = crud.update_note(user_id, note_id, note)
    if not updated:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated

@app.delete("/notes/{note_id}")
def delete_note(note_id: str, user_id: str = Depends(get_current_user)):
    success = crud.delete_note(user_id, note_id)
    if not success:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"detail": "Note deleted"}
