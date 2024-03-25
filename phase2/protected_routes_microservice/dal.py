import motor.motor_asyncio
import os

async def insert_logged_out_token_into_db(token_to_insert):
    client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
    db_connection = client.logged_out_tokens
    logged_out_tokens_collection = db_connection.get_collection("logged_out_tokens_coll")
        
    response = await logged_out_tokens_collection.insert_one(
        {"access_token":token_to_insert}
    )
    
    client.close()
    return response


# {
#     "access_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJvaGl0LnNpbmdoQGhlYWxpbmdob3Jpem9ucy5jb20iLCJ1c2VyX3R5cGUiOiJkb2N0b3IiLCJleHAiOjE3MTE0MDIyMzV9.h9uWvpdx64XlWGzhTeNKx1BoRU5zVmuKflkkVKsTNt-vFzlOu-qTrAgCkNKylFSsyZkLdRl1dfrUzk19It9b0ZXTPj1qvRqdc20rSy5pc01jHFQerVG82beJwQX7rYbS43OAPgKhwuJ_nfPc0mUl74f6U0Q5wmstS1cg-XeTZ7TE9lWPQ4gQPuOnENvPHH45ngodmabT0XXr8Y5hQaU-Q9dDPEGRKPOm3ddNn46UZGIt4umAmVnLsnaIaHtY5pOPIakkpW_VLIdWReO1msAhSUpcX66jii7HhpLebc6WN6NPzLR2co-nZ10oaFJvqeR-YnMLM7N2j752b8Hay5UC1B9D2PyO-vKQg996Dp3Nz6H-ILc0QokqaINDyPYeVJzcsCDqrN4RbCLTbsj8v602wSJMnDDjBiDv_YggDZYXCO8grlGCZY7bQK6K1ChNBXnUTwk9PcL4ZrN80xOCg_5pQIZrF4l8DhNO04NqgkgmS1qlDc5HqMH032p4sxdCiQHfIvBYFPnX13MPwBlGpHdMFdJeNkP_PTbY7ym6dSb1kQKlnzNcDENCoRL_QoF1dpiaU88dTlp9y6bzBxAG79QKqlJme6D69r05Yr-LeEE_JUWDzfF7OdVLD3qm_55GP9pqM0Hk2Z9Vq-sEDI96ay6VG3HF87r_5OUU7z-X1fwtnmQ"
# }