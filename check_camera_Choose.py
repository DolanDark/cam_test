import sys

import gphoto2 as gp

# if len(sys.argv) > 2:
#     print('Usage: {} [port_address]'.format(sys.argv[0]))

# if len(sys.argv) > 1:
#     addr = sys.argv[1]

camera_list = list(gp.Camera.autodetect())
if not camera_list:
    print('No camera detected')
else:
    camera_list.sort(key=lambda x: x[0])

    for index, (name, addr) in enumerate(camera_list):
        print('{:d}:  {:s}  {:s}'.format(index, addr, name))
    choice = input('SELECT CAM ---- ')
    choice = int(choice)
    if choice < 0 or choice >= len(camera_list):
        print('Number out of range')
    else:
        addr = camera_list[choice][1]
        port_info_list = gp.PortInfoList()
        port_info_list.load()
        abilities_list = gp.CameraAbilitiesList()
        abilities_list.load()
        camera_list = abilities_list.detect(port_info_list)
        if len(camera_list) < 1:
            print('No camera detected')
        else:
            camera = gp.Camera()
            idx = port_info_list.lookup_path(addr)
            camera.set_port_info(port_info_list[idx])
            idx = abilities_list.lookup_model(camera_list[0][0])
            camera.set_abilities(abilities_list[idx])

            text = camera.get_summary()
            print('Summaryyy')
            print(str(text))
            # try:
            #     text = camera.get_manual()
            #     print('Manual')
            #     print('=======')
            #     print(str(text))
            # except Exception as ex:
            #     print(str(ex))
            camera.exit()

