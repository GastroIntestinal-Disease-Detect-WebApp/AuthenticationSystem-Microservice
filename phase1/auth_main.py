# this file contains the login route.
# which will check if the user exists.
# if yes then a token is created and returned to the user.
# any subsequent request made by the user (to access protected resources) must contain the valid token in the authorisation header.

from fastapi import FastAPI
from schemas import Login
from dal_main import dal_get_user_from_db
from jwt_create_token import create_token

app = FastAPI()
private_key = open('jwt_id_rsa_key', 'r').read()

@app.post("/login",response_model=dict)
async def login(login_object : Login):
    login_dict = login_object.model_dump()
    user = await dal_get_user_from_db(login_dict)
    
    # user does not exist:
    if user is None:
        return {"message":"Invalid Credentials"}
    
    # correct email and password
    if user["password"] == login_dict["password"]:
        print("Valid Credentials")
        token = create_token(user["email"],user["user_type"],private_key)
        return {"message":"Valid Credentials","access_token":token}
    
    # correct email but incorrect password
    else:
        return {"message":"Invalid Credentials"}


# @app.post("")