import os
import gphoto2 as gp

def save_img_using_event():
    camera = gp.Camera()
    camera.init()
    timeout = 4000
    event_type, event_data = camera.wait_for_event(timeout)
    # print("EVENTTYPE -- ", event_type, "EVENTDATA -- ", event_data)
    if event_type == gp.GP_EVENT_FILE_ADDED:
        cam_file = camera.file_get(event_data.folder, event_data.name, gp.GP_FILE_TYPE_NORMAL)
        target_path = os.path.join( event_data.name)
        cam_file.save(target_path)

