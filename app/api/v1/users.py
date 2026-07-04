from fastapi import APIRouter
from pydantic import BaseModel
router=APIRouter(prefix="/users",tags=["Users"])
db={}
class User(BaseModel):
 id:int; username:str; email:str
@router.post("")
def create(u:User): db[u.id]=u; return u
@router.get("")
def all(): return list(db.values())