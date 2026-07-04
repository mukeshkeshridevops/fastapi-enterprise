from fastapi import APIRouter
from pydantic import BaseModel
router=APIRouter(prefix="/departments",tags=["Departments"])
db={}
class Department(BaseModel):
 id:int; name:str
@router.post("")
def create(d:Department): db[d.id]=d; return d
@router.get("")
def all(): return list(db.values())