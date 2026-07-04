from datetime import datetime,timedelta
from jose import jwt

SECRET_KEY='change-me'
ALGORITHM='HS256'

def create_access_token(subject:str, minutes:int=30):
    payload={'sub':subject,'exp':datetime.utcnow()+timedelta(minutes=minutes)}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token:str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
