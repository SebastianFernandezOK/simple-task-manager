from sqlmodel import SQLModel, Field, Optional

class BoardBase(SQLModel):
    id: int |  None = Field(default=None, primary_key=True)
    title: str
    description: Optional[str]
    user_id: int = Field(foreign_key="user.id")

class BoardCreate(BoardBase, table=True):
        pass