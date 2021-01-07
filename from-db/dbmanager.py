from pymongo import MongoClient
import base64


client = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")
db=client.admin


def create_image(name, image):
    with open(image, "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
    face = {
        'name' : name,
        'image' : str
    }
    try:
        result=db.reviews.insert_one(face)
        print('Created '.format(result.inserted_id))
        return result

    except Exception as e:
        print(f"Error to encode {name}'s face")
        return e
    

def delete_images(name):
    print("delete_images")
    
def get_images():
    print("get_images")