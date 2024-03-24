from pydantic import BaseModel

class ProtectedRouteInput(BaseModel):
    access_token : str