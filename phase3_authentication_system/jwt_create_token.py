import jwt
import datetime
from cryptography.hazmat.primitives import serialization

# use the below command to generate public and private key:
# ssh-keygen -t rsa -b 4096

# another command that might be useful:
# ssh-keygen -p -o -f <pk_file_name>

def create_token(email,user_type,private_key):
    # Get the current time in UTC and add 60000 seconds to it
    exp_tme = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=60000)
    
    payload_data = {
        "email": email,
        "user_type": user_type,
        "exp" : exp_tme
    }
    
    key = serialization.load_ssh_private_key(private_key.encode(), password=b'')
    
    new_token = jwt.encode(
        payload=payload_data,
        key=key,
        algorithm='RS256'
    )
    
    return new_token