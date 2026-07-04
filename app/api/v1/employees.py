from fastapi import APIRouter
from pydantic import BaseModel
router=APIRouter(prefix="/employees",tags=["Employees"])
db={}
class Employee(BaseModel):
 id:int; name:str; department_id:int; salary:float
@router.post("")
def create(e:Employee): db[e.id]=e; return e
@router.get("")
def all(): return list(db.values())