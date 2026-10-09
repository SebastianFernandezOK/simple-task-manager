from sqlmodel import SQLModel, Field, Optional
from pydantic import EmailStr
class UserBase(SQLModel):
    name: str
    surname: str
    dni: Optional[str] = Field(default=None, unique=True)
    email: EmailStr = Field(index=True, unique=True)

class UserRegister(UserBase):
    password: str

    

class UserLogin(SQLModel):
    email: str
    password: str