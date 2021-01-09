# Face-recognition

For run this project, you have to check the dependencies:

```python
pip install face-recognition
```

Go to file [/face-recognition/blob/main/from-folder/show-recognition.py](/from-folder/show-recognition.py)

To begin, we'll need some samples of faces that we wish to detect and identify. On this repository, we create a directory called *known_faces*, wich will house directories of known identities. Inside of this folder, we add a directory call with the name of the person, on my case *Marsha* and *Francesco*.

Inside of the directory [*Marsha*](/from-folder/known_faces/Marsha) we have the following images:

<img src="/from-folder/known_faces/Marsha/1.png" width="100">

<img src="/from-folder/known_faces/Marsha/2.png" width="100">

<img src="/from-folder/known_faces/Marsha/3.png" width="100">

Inside of the directory [*Francesco*](/from-folder/known_faces/Francesco) we have the following images:

<img src="/from-folder/known_faces/Francesco/1.png" width="100">

<img src="/from-folder/known_faces/Francesco/2.png" width="100">

<img src="/from-folder/known_faces/Francesco/3.png" width="100">

We can then add a new directory called *unknown_faces*. These are faces that we intended to label (if any of the known faces exist in these images). Here are the ones we use:

<img src="/from-folder/unknown_faces/1.png" width="100">

<img src="/from-folder/unknown_faces/2.png" width="100">

<img src="/from-folder/unknown_faces/3.png" width="100">

<img src="/from-folder/unknown_faces/4.png" width="100">

<img src="/from-folder/unknown_faces/5.png" width="100">

<img src="/from-folder/unknown_faces/6.png" width="100">

Example of results:

<img src="/screenshots/1.png" width="300">

<img src="/screenshots/2.png" width="300">

<img src="/screenshots/3.png" width="300">