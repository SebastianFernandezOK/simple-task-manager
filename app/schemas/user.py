from sqlmodel import SQLModel, Field, Optional
class UserBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    surname: str
    dni: Optional[str] = Field(default=None, unique=True)
    email: str = Field(index=True, unique=True)

class UserRegister(UserBase):
    password: str

    

class UserLogin(SQLModel):
    email: str
    password: str