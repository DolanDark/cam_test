Nikon Coolpix S9100 (PTP mode) -- Image Capture, Configuration

Nikon DSC D7000 (PTP mode)	   -- Image Capture, Trigger Capture, Liveview, Configuration

Nikon DSC D7100	(PTP mode)     -- Image Capture, Trigger Capture, Liveview, Configuration


<!--
[-?|--help]
[--usage] 
[--debug] 
[--debug-loglevel=STRING] 
[--debug-logfile=FILENAME] 
[-q|--quiet]

[--hook-script=FILENAME] 
[--stdout] 
[--stdout-size]
[--list-cameras] 
[--manual] 
[--about]  
[--shell] 
[-v|--version]
[--reset]
[--keep]
[--keep-raw] 
[--no-keep]
[--show-exif=STRING] 
[--show-info=STRING] 
[--port=FILENAME] 
[--speed=SPEED]
[--camera=MODEL]
[--usbid=USBIDs] 
[-B|--bulb=SECONDS]
[-F|--frames=COUNT] 
[-I|--interval=SECONDS] 
[--reset-interval] -->


sudo pip3 install gphoto2 --only-binary :all:

sudo apt install libexif12 libgphoto2-6 libgphoto2-port12 libltdl7

sudo pip3 install gphoto2


[--auto-detect]
[--summary]
[--storage-info]
[--list-ports] 
[-a|--abilities]
[--config] 
[--list-config]
<!-- [--list-all-config] -->
[--wait-event=COUNT, SECONDS, MILLISECONDS or MATCHSTRING]
[--wait-event-and-download=COUNT, SECONDS, MILLISECONDS or MATCHSTRING]
[--capture-preview]
[--show-preview]
[--capture-image]
[--trigger-capture]
[--capture-image-and-download]
[--capture-sound]
[--capture-movie=COUNT or SECONDS]
[--capture-tethered=COUNT, SECONDS, MILLISECONDS or MATCHSTRING]
[-l|--list-folders]
[-L|--list-files]
[-m|--mkdir=DIRNAME]
[-r|--rmdir=DIRNAME]
[-n|--num-files]
[-p|--get-file=RANGE]
[-P|--get-all-files]
[-t|--get-thumbnail=RANGE]
[-T|--get-all-thumbnails]
[--get-metadata=RANGE]
[--get-all-metadata]
[--upload-metadata=STRING]
[--get-raw-data=RANGE]
[--get-all-raw-data]
[--get-audio-data=RANGE]
[--get-all-audio-data]
[-d|--delete-file=RANGE]
[-D|--delete-all-files]
[-u|--upload-file=FILENAME] 
[--filename=FILENAME_PATTERN] 
[-f|--folder=FOLDER] 
[-R|--recurse] 
[--no-recurse] 
[--new]
[--force-overwrite] 
[--skip-existing]



[--get-config=STRING]
[--set-config=STRING]
[--set-config-index=STRING]
[--set-config-value=STRING]



ps aux | grep gphoto



#### To test after setconfig capturetarget

gphoto2 --list-ports
gphoto2 --auto-detect
gphoto2 --summary
gphoto2 --list-files
<!-- gphoto2 --get-all-files -->
gphoto2 --list-config
gphoto2 --get-config shutterspeed
gphoto2 --set-config shutterspeed=1
gphoto2 --capture-image
gphoto2 --trigger-capture
gphoto2 --capture-image-and-download
gphoto2 --capture-image-and-download --filename "myphoto.jpg"
gphoto2 --capture-image-and-download --filename "%Y%m%d%H%M%S.jpg"

gphoto2 --set-config capturetarget=0            #important

gphoto2 --capture-tethered
gphoto2 --capture-tethered=10s

gphoto2 --trigger-capture "--camera=Canon EOS 600D"