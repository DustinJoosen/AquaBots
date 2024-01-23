# AquaBots

Turn your raspberry-pi into a full-fledged aquatic drone!


## Installing

Before anything else, you have to install everything. This process is described [here](/INSTALL.md)

## Connect the hardware

```
Moisture: 		port A2
IMU:    		port IC2

Location command: cat /dev/ttyAMA0
```

## Running the API

On the raspberry pi, run one of the following files:

- src/API/api.exe
- src/API/api.py

The first is an executable of the second file. It *shouldn't* matter which one you pick.

## Running the GUI

On the host laptop, run one of the following files:

- src/GUI/gui.exe
- src/GUI/gui.py

The first is an executable of the second file. It *shouldn't* matter which one you pick.

When this file is running, visit the webpage on http://127.0.0.1:5000/ 

Here you can specify the access code of the thingsboard device. (If you do not have an access code, follow *this* guide). When this is done, you can set a pin and interval for a specific sensor, and enable it. It will automatically send all data to the thingsboard of the specified accesscode.
