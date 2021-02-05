# eo_gui
Web-based interface for HiRACS camera.

## Purpose
World View plans on implementing its own camera for high-altitude photography from Stratolite balloons. That camera
will be called HiRACS and will be integraated into the flight systems of the balloon. This code is a web interface for
controlling the HiRACS camera. It uses VUE and Javascript to build a sinple, single-page app to access camea functions.

## Progress
At the time the HiRACS project was placed on hold the only function that had been implemented was control of the 
focuser unit for the Wide Field of View camera element. The interface allows a user to move the focuser to its fully
retracted position, fully extended position, home position, and any arbitrary position in-between. The user can also
specify the size of incrmental steps used in all subsequent commands.

## Structure
The eo_gui project is divided into a client and a server. The client produces the GUI used by camear operators. The
server provides a backend that converts commands from the GUI into calls over the internet to the camera daemon which
runs on the payload computer onboard the Stratolite
