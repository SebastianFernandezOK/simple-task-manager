from schemas.user import UserBase
from sqlmodel import Field

class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str