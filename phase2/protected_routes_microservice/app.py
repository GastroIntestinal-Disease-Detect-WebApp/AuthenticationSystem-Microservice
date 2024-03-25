from fastapi import FastAPI, Depends, Header, HTTPException
from auth.get_payload_of_token import get_payload_of_jwt_token
from dal import insert_logged_out_token_into_db
import uvicorn

app = FastAPI()


@app.get("/protected_route", response_model=dict)
def protected_route(payload_of_jwt_token: dict = Depends(get_payload_of_jwt_token, use_cache=False)):
    # if the below lines are getting executed then the  
    print(payload_of_jwt_token)
    return {"message": "Valid Token"}


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, port=8002)

@app.get("/logout")
async def logout(authorization: str = Header(None)):
    
    if authorization is None:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    
    try:
        scheme, token = authorization.split()
    
        if scheme.lower() != 'bearer':
            raise HTTPException(status_code=401, detail="Invalid token type")
        
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid authorization header format")
    
    response = await insert_logged_out_token_into_db(token)
    
    print(response)