# this file contains the login route. which will check if the user exists. if yes then a token is created and
# returned to the user. any subsequent request made by the user (to access protected resources) must contain the
# valid token in the authorisation header.

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from schemas.schemas_main import Login
from dal.dal_main import dal_get_user_from_db
from jwt_create_token import create_token
import uvicorn


app = FastAPI()
private_key = open('jwt_id_rsa_key', 'r').read()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/login", response_model=dict)
async def login(login_object: Login):
    login_dict = login_object.model_dump()
    user = await dal_get_user_from_db(login_dict)

    # user does not exist:
    if user is None:
        return {"message": "Invalid Credentials"}

    # correct email and password
    if user["password"] == login_dict["password"]:
        print("Valid Credentials")
        token = create_token(user["email"], user["user_type"], private_key)
        if user["user_type"] == "admin":
            return {"message": "Valid Credentials", "access_token": token, "redirect_link": "http://127.0.0.1:8001/static/admin_home.html"}
        elif user["user_type"] == "doctor":
            return {"message": "Valid Credentials", "access_token": token, "redirect_link": "http://127.0.0.1:8001/static/doctor_home.html?access_token="+token}
        
    
    # correct email but incorrect password
    else:
        return {"message": "Invalid Credentials"}


if __name__ == "__main__":
    uvicorn.run("auth_main:app", reload=True, port=8002)
