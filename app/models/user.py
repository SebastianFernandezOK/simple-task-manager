from schemas.user import UserBase

class User(UserBase, table=True):
    password: str