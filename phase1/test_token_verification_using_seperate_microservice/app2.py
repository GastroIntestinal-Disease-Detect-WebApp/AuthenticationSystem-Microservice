from fastapi import FastAPI, Header, Depends, HTTPException
from jwt_verify_token import verify_token

public_key = open('jwt_id_rsa_key.pub', 'r').read()

app = FastAPI()

def get_payload_of_jwt_token(authorization: str = Header(None)):
    if authorization is None:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    try:
        scheme, token = authorization.split()
        
        if scheme.lower() != 'bearer':
            raise HTTPException(status_code=401, detail="Invalid token type")
        
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid authorization header format")

    response = verify_token(token, public_key)
    
    if response["message"] == "Invalid Token":
        raise HTTPException(status_code=401, detail="Invalid Token")
    
    elif response["message"] == "Token has Expired":
        raise HTTPException(status_code=401, detail="Token has Expired")

    return response  

@app.get("/protected_route", response_model=dict)
def protected_route(payload_of_jwt_token: dict = Depends(get_payload_of_jwt_token,use_cache=False)):
    # if the below lines are getting executed then the  
    print(payload_of_jwt_token)
    return {"message": "Valid Token"}
