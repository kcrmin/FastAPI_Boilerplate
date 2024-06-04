# FastAPI
from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from .. import database, utils, models, schemas, oauth2

# auth
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

# initialize
pool = database.get_pool()
router = APIRouter(
    tags=['Authentication']
)

@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(stxatus_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    # create a token
    access_token = oauth2.create_access_token(data = {"user_id": user.user_id})
    # return token
    return {"access_token": access_token, "token_type": "bearer"}