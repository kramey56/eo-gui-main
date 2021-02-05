# client

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

### Furlough comments by Ken Ramey
The client directory contains all the code for the web front-end to the camera. At this time, only the focusing unit
is implemented in both the client and server code. The interface presents a single pane that shows current status of
the focusing unit, including its current position, temperature, and whether or not it is moving. It also allows the 
user to specify how many steps of 1.04 microns each command sends and how many successive commands to execute.

The front end also sets up an interval timer that requests the focusing unit's status every second in order to update
the status display. All commands are acknowledged by a pop-up on the display that shows that the command was executed
or that there was an error during execution, as appropriate.

There are also buttons at the bottom of the control panel that move the focusing unit to standard locations. There are
buttons for "Home", "Center", and "Zero". Zero takes the focusing unit to its fully retracted position. Center puts the
focusing unit at the middle of its travel range. Home moves the focusing unit to its "0" position and then returns it
to its last commanded position.
