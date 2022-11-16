
import os
import gphoto2 as gp


camera = gp.Camera()
camera.init()

file_path = camera.capture(gp.GP_CAPTURE_IMAGE)
print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
local_path = os.getcwd()
target = os.path.join(local_path, file_path.name)
print('Copying image to', target)
camera_file = camera.file_get(file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
camera_file.save(target)
