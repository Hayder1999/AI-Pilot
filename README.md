# AI Pilot

## Table of contents

1. Setup of X-plane
2. Current working file
3. Additional info
4. Currently active

# 1. Check if X Plane is set up corectly:
* Under Data output > General Data output > 
  * Network configuration is turned **ON**
  * IP address  =                   192.168.0.1
  * Port        =                   49000
* Under Data output > Dataref Read/Write >
  * Networked computer is turned    **ON**
  * IP address  =                   192.168.0.1
  * Port        =                   49000

### 1.2 Add XPlane Connect extension
Shut down XPlane

Visit https://github.com/nasa/XPlaneConnect/releases and download **Version 1.2.1**
\
Open folder XPlaneConnect-1.2.1 > Open folder XplPlugin
\
Copy folder XPlaneConnect to Game Install folder > **Resources** > **plugins**

Start XPlane and load a flight.
\
At the top, click on plugins > plugin admin > enable/disable and verify that **X-Plane Connect [Version 1.2.1]** is present. 

# 2. Current working file for recieving data

Folder > xplane

File > xplane4.py

Check the required dependencies which are at the top of the file, before running with your prefered IDE.

~~In order to stop running, simply press 'esc' while the terminal is selected.~~

