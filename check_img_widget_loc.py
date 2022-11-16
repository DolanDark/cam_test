import gphoto2 as gp


camera = gp.Camera()
camera.init()

# gp.GP_WIDGET_SECTION -> 1
# gp.GP_WIDGET_TEXT -> 2
# gp.GP_WIDGET_RANGE -> 3
# gp.GP_WIDGET_TOGGLE -> 4
# gp.GP_WIDGET_RADIO -> 5

camera_config = camera.get_config()

# print(camera_config.get_label())
# print(camera_config.get_readonly())
# print(camera_config.count_children())

for child in camera_config.get_children():
    print(f"Label - {child.get_label()}, Name - {child.get_name()}")
    ## child.get_type() for <built-in method get_type of gphoto2.widget.CameraWidget object at 0x7f5d21e54db0>
    child_type = child.get_type()
    if child_type == gp.GP_WIDGET_SECTION:
        print(f"WidgetSec - {child.get_label()}")
    elif child_type == gp.GP_WIDGET_TEXT:
        print(f"WidgetTxt - {child.get_label()}")
        print(child.get_value())
    elif child_type == gp.GP_WIDGET_RANGE:
        print(f"WidgetRange - {child.get_label()}")
    elif child_type == gp.GP_WIDGET_TOGGLE:
        print(f'WidgetToggle - {child.get_label()}')
    elif child_type == gp.GP_WIDGET_RADIO:
        print(f"WidgetRadio - {child.get_label()}")
    elif child_type == gp.GP_WIDGET_MENU:
        print(f"WidgetMenu - {child.get_label()}")
    elif child_type == gp.GP_WIDGET_DATE:
        print(f"WidgetDate - {child.get_label()}")
    else:
        print(f"InvalidWidgetType - {child.get_label()}")    

    

