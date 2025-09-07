from fastapi import FastAPI, HTTPException, Depends, Header, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from app import crud, schemas
from app.firebase import auth

app = FastAPI()

bearer_scheme = HTTPBearer()

with open("description.txt", "r", encoding="utf-8") as f:
    description = f.read()

app = FastAPI(
    title="Not Uygulaması API",
    description=description,
    version="1.0.0"
)

def get_current_user(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid auth header")
    id_token = authorization.split(" ")[1]
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token.get("sub") or decoded_token.get("uid")
        if not uid:
            raise HTTPException(status_code=401, detail="No user ID in token")
        return uid
    except Exception as e:
        import os
        if os.getenv("DEBUG", "False").lower() == "true":
            raise HTTPException(status_code=401, detail=f"Token validation failed: {str(e)}")
        else:
            raise HTTPException(status_code=401, detail="Invalid Firebase token")

# --- Test için create user endpoint ---
@app.post("/test/create_user")
def create_test_user(req: schemas.UserCreateRequest):
    try:
        user = auth.create_user(email=req.email, password=req.password)
        custom_token = auth.get_user(user.uid)
        return {"uid": user.uid, "custom_token": custom_token.decode()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# --- Test için signin endpoint ---
@app.post("/test/signin")
def signin_user(req: schemas.SignInRequest):
    try:
        user = auth.get_user_by_email(req.email)
        custom_token = auth.create_custom_token(user.uid)
        return {"custom_token": custom_token.decode()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# --- Notes endpoints ---
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
