# Source code and instructions for the HumanFirewall camera
This repo contains a no longer supported implementation of the project in which the server took care of all the hard-work.

The board sole purpose was to send the photos to the remote server.

I suggest you to check our new [cloud-less implementation](https://github.com/humanfirewall-iot19/).


The required packages for the project are liste in the file *requirements.txt*.  
To setup the hotspot we require the following program to be installed [create_ap](https://github.com/oblique/create_ap).   
This script must be run as root, so we use a wrapper (defined in *wrapper.c*), which will switch to the root user to create the access point to reconfigure the network options.  
To make this works we need to execute these few commands:  

```sh 
sudo chown root:root wrapper
sudo chmod +s wrapper
sudo chmod +x camera.py
```

The name of the network is **HumanFirewall-reconfigure** and the board address is the address of the default gateway (obtainable with *ip route* command) 
Finally make sure that the file called camera.py is in the same folder as the wrapper executable.  
