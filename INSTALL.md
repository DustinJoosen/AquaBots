# Installing

The current codebase of AquaBots contains two main parts: the API and the GUI. 

The API is to be run on the raspberry pi, and will be responsible for handling the sensors. Through a Flask API the host laptop will be able to communicate with the raspberry pi.

The GUI is to be run on the host laptop (while possible to run on the raspberry pi, this is highly discouraged due to limited memory). It contains a simple Flask webpage that allows you to enable sensors, and automatically send retrieved data to thingsboard.

To properly install everything, you have to follow four steps:

1. : Clone the repository
2. : Install the pip packages 
3. : Make a firewall exception 
4. : Setup a local thingsboard server

( !! This guide does not walk you through connecting the hardware !! )


## Step 1: clone the repository

A simple step if you have previously worked with GIT.

You have to clone this repository twice. Once on your host laptop and once on your raspberry pi (It is also possible to only clone on the host laptop, and manually move /API/api.exe to the raspberry pi.)

to clone the repository, you first have to open a command prompt. There you can execute the following command:

    git clone https://github.com/DustinJoosen/AquaBots.git

This will create a new directory "AquaBots", where all the code will be in. Check if this directory contains *at least* the following: *requirements.txt*, a *docs* folder, and a *src* folder.


## Step 2: Install the pip packages

Not all python packages used in this project are installed on default. The packages needed for everything to run are found inside the file "requirements.txt" 

To install everything you can execute the following command, both on the raspberry pi and the host computer.

    pip install -r requirements.txt

This will install all required packages, like Flask and grove.py


## Step 3: Make a firewall exception 

Unfortunaletly, for the raspberry pi and the host laptop to be able to communicate, you might need to make an exception on the firewall of the host laptop. This is done for port 5001


The following steps can be followed:

- Open Windows Defender Firewall
- Go to Advanced settings on the left
- In the left pane, right-click on "Inbound Rules," then select "New Rule..."
- Choose "Port" and click "Next."
- Select "TCP" and specify the port 5001.
- Choose "Allow the connection" and click "Next."
- Specify when the rule applies (you can leave the default) and give your rule a name.
- Click "Finish" to create the rule.


## Step 4: Setup a local thingsboard server

This step will not be explained in this guide. You can find it here:

- [PDF version (english)](/docs/Thingsboard%20guide%20English.pdf)
- [PDF version (dutch)](/docs/Thingsboard%20guide%20Dutch.pdf)
