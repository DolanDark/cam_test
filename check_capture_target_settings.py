import gphoto2 as gp

camera = gp.check_result(gp.gp_camera_new())
gp.check_result(gp.gp_camera_init(camera))
config = gp.check_result(gp.gp_camera_get_config(camera))

capture_target = gp.check_result(
    gp.gp_widget_get_child_by_name(config, 'capturetarget'))

value = gp.check_result(gp.gp_widget_get_value(capture_target))
print('Current setting:', value)

##listing all settings
for n in range(gp.check_result(gp.gp_widget_count_choices(capture_target))):
    choice = gp.check_result(gp.gp_widget_get_choice(capture_target, n))
    print('Choice:', n, choice)

gp.check_result(gp.gp_camera_exit(camera))