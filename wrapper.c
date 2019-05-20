#include <stdlib.h>
#include <unistd.h>
int main(int argc, char* argv){
	//we start the python script, in the script stops we have lost connection, so we make an hotspot to allow users to reconfigure the wireless settings
	system("./camera.py");
	//so we switch to root user
	setuid(0);
	//and we make an hotspot, so the wireless settings can be reconfigured
	system("create_ap -n wlan0 HumanFirewall-reconfigure");
	return 0;
}
