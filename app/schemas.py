from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# --- Test için kullanıcı oluşturma endpoint ---
class UserCreateRequest(BaseModel):
    email: str
    password: str

# --- Test için kullanıcı girişi endpoint ---
class SignInRequest(BaseModel):
    email: str
    password: str


class NoteCreate(BaseModel):
    id: str 
    title: str
    content: str
    
class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class NoteOut(BaseModel):
    id: str
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
