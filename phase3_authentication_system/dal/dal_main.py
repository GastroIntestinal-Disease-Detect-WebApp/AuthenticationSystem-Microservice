import motor.motor_asyncio
import os

async def dal_get_user_from_db(login_dict):
    client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
    db_connection = client.users
    users_collection = db_connection.get_collection("users_coll")
    
    email = login_dict["email"]
    user = await users_collection.find_one(
        {"email":email}
    )
    
    client.close()
    return user

# Example of user stored in mongodb : 
# {
#   _id: ObjectId('65f7c8a77ec34b522dd61478'),
#   email: 'rohit.singh@healinghorizons.com',
#   password: 'b912e277689453e2089958e108ddb7d1016e086004e86d05b24e38187cbeebfc',
#   user_type: 'doctor'
# }