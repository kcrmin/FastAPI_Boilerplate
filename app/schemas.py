# Pydantic Schemas
from pydantic import BaseModel

# Optional Imports
from pydantic import EmailStr
from datetime import datetime
from typing import Optional, Literal

# JWT Token
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: int

# Samples (edit from here)
class SampleBase(BaseModel):
    field1: str
    field2: int
    field3: datetime
    field4: Optional[bool] = True
    field5: EmailStr
    field6: Literal[0,1] # 0 or 1

class SampleCreate(SampleBase):
    field6: str
    field7: str

class SampleUpdate(SampleBase):
    field6: str
    field7: str

class SampleResponse(BaseModel):
    field1: SampleBase
    field2: int

# Base
# Create
# Update
# Read
