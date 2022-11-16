import os
import gphoto2 as gp


camera = gp.Camera()
camera.init()
timeout = 5000
while True:
    event_type, event_data = camera.wait_for_event(timeout)
    print("EVENTTYPE -- ", event_type, "  ", "EVENTDATA -- ", event_data)

    if event_type == gp.GP_EVENT_FILE_ADDED:
        cam_file = camera.file_get(event_data.folder, event_data.name, gp.GP_FILE_TYPE_NORMAL)
        target_path = os.path.join(os.getcwd(), event_data.name)
        print("Image saved ", target_path)
        cam_file.save(target_path)

