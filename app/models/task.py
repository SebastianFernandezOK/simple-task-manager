from sqlmodel import SQLModel, field, Optional

class TaskBase(SQLModel):
    id: int | None = field(default=None, primary_key=True)
    title:str
    description: Optional[str]

    