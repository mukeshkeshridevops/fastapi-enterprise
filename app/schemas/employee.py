from pydantic import BaseModel
class EmployeeCreate(BaseModel):
    name:str
    department:str
    salary:float
class EmployeeResponse(EmployeeCreate):
    id:int
    model_config={'from_attributes':True}
