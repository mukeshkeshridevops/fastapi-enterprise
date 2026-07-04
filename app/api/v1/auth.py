from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
router=APIRouter(prefix="/auth",tags=["Auth"])
class Login(BaseModel):
 username:str
 password:str
@router.post("/login")
def login(d:Login):
 return {"access_token":"demo-token","token_type":"bearer"} if d.username=="admin" and d.password=="admin" else (_ for _ in ()).throw(HTTPException(status_code=401,detail="Invalid credentials"))