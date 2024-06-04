# Hashing
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# HTTP Exceptions
from fastapi import HTTPException, status, Response

def verify_availability(object, object_name: str , id: int):
    if object == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"[{object_name}] with id: {id} does not exist")

def verify_authority(object_owner_id: int, current_user_id: int):
    if object_owner_id != current_user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")
# Samples (Edit from here)