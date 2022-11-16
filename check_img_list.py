import os
import gphoto2 as gp


def list_files(camera,path="/"):
    result = []
    for name, value in camera.folder_list_files(path):
        result.append(os.path.join(path, name))
    folders = []
    for name, value in camera.folder_list_folders(path):
        folders.append(name)
    for name in folders:
        result.extend(list_files(camera, os.path.join(path, name)))
    return result

camera = gp.Camera()
camera.init()
files = list_files(camera)
[print(file) for file in files]
print("IMGCOUNT - ", len(files))