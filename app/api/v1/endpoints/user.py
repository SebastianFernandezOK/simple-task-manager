from schemas import UserRegister
from cruds import create_user
from fastapi import HTTPException, FastAPI


app = FastAPI()

@app.post("/users/create",
          response_model=UserRegister,
          status_code=status.HTTP_201_CREATED,
          summary="Register a new user",
          )
    create_user()