# This version return the name of the person found

import face_recognition
import os
import cv2


KNOWN_FACES_DIR = 'known_faces'
UNKNOWN_FACES_DIR = 'unknown_faces'
TOLERANCE = 0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = 'hog'  # default: 'hog', other one can be 'cnn' - CUDA accelerated (if available) deep-learning pretrained model


# Returns (R, G, B) from name
def name_to_color(name):
    # Take 3 first letters, tolower()
    # lowercased character ord() value rage is 97 to 122, substract 97, multiply by 8
    color = [(ord(c.lower())-97)*8 for c in name[:3]]
    return color

known_faces = []
known_names = []

def encode_photos(folder):
    print('Known faces')
    # Each subfolder's name becomes our label (name)
    for name in os.listdir(folder):

        # Next we load every file of faces of known person
        for filename in os.listdir(f'{folder}/{name}'):

            # Load an image
            image = face_recognition.load_image_file(f'{folder}/{name}/{filename}')

            try:
                encoding = face_recognition.face_encodings(image)[0]
                # Append encodings and name
                known_faces.append(encoding)
                known_names.append(name)
                print(f'Known Faces: Filename {filename} \n', end='')

            except Exception as e:
                print(f"Error to encode image: {folder}/{name}/{filename} \n {e}")
                pass

    return known_faces, known_names
        
def face_recognice(image):
    # This time we first grab face locations - we'll need them to draw boxes
    locations = face_recognition.face_locations(image, model=MODEL)

    # Now since we know loctions, we can pass them to face_encodings as second argument
    # Without that it will search for faces once again slowing down whole process
    encodings = face_recognition.face_encodings(image, locations)

    # We passed our image through face_locations and face_encodings, so we can modify it
    # First we need to convert it from RGB to BGR as we are going to work with cv2
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # But this time we assume that there might be more faces in an image - we can find faces of dirrerent people
    print(f', found {len(encodings)} face(s)')
    for face_encoding, face_location in zip(encodings, locations):

        # We use compare_faces (but might use face_distance as well)
        # Returns array of True/False values in order of passed known_faces
        results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)

        # Since order is being preserved, we check if any face was found then grab index
        # then label (name) of first matching known face withing a tolerance
        match = None

        if True in results:  # If at least one is true, get a name of first of found labels
            match = known_names[results.index(True)]
        return match
    
def from_unknown_folder(folder):
    # Now let's loop over a folder of faces we want to label
    for filename in os.listdir(folder):
        # Load image
        print(f'Unknown Faces: Filename {filename}', end='')
        image = face_recognition.load_image_file(f'{folder}/{filename}')
        match = face_recognice(image)
        print(match)

# The first step is call the encode photos function for load all the known faces
encode_photos(KNOWN_FACES_DIR)

# On this step, we call the unknown faces for try to search on our encode data the relation
from_unknown_folder(UNKNOWN_FACES_DIR)
    

            