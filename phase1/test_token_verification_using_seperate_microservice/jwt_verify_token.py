import jwt
from cryptography.hazmat.primitives import serialization

def verify_token(token, public_key):
    header_data = jwt.get_unverified_header(token)
    
    key = serialization.load_ssh_public_key(public_key.encode())

    # verify token:
    try:
        payload_of_decoded_token = jwt.decode(jwt=token, key=key, algorithms=[header_data['alg']])
    
    except jwt.exceptions.InvalidSignatureError:
        return {"message" : "Invalid Token"}
    
    except jwt.exceptions.ExpiredSignatureError:
        return {"message" : "Token has Expired"}
    
    payload_of_decoded_token["message"] = "Valid Token"
    
    return payload_of_decoded_token