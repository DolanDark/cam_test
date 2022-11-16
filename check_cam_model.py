import gphoto2 as gp

def get_camera_model(camera_config):
    OK, camera_model = gp.gp_widget_get_child_by_name(camera_config, 'cameramodel')
    print("OK -- ", OK)
    print("Camera Model -- ",camera_model)
    print("gp.GP_OK", gp.GP_OK)
    if OK < gp.GP_OK:
        OK, camera_model = gp.gp_widget_get_child_by_name(camera_config, 'model')
    if OK >= gp.GP_OK:
        camera_model = camera_model.get_value()
    else:
        camera_model = ''
    return camera_model



camera = gp.Camera()
camera.init()
camera_config = camera.get_config()
print(camera_config.get_value)
# camera_model = get_camera_model(camera_config)

# print(camera_model)
# print(cfg.__dir__())
# print("LABEL",)