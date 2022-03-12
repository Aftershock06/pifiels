UPDATE - 12/Mar/2022 

I am relaunching this project to get it working in my new space. 

#pifiles

I followed these commands to update the system to stop running the scrolltest.py

systemd

1. Create a Bash script /usr/local/sbin/run_on_shutdown.sh with the following contents:

#!/bin/bash
REBOOT=$( systemctl list-jobs | egrep -q 'reboot.target.*start' && echo "rebooting" || echo "not_rebooting" )
if [ $REBOOT = "not_rebooting" ]; then
    ########################################################################
    # Put Bash commands here to be executed on shutdown but not on reboot. #
    # For example, backup home directories to an external USB HDD.         #
    ########################################################################
fi
2. Create a unit file /etc/systemd/system/run_on_shutdown.service with the following contents:

[Unit]
Description=Run a Bash script at shutdown
DefaultDependencies=no
Before=shutdown.target halt.target
# If your script requires any mounted directories, add them below: 
RequiresMountsFor=/home
 
[Service]
Type=oneshot
ExecStart=/usr/local/sbin/run_on_shutdown.sh
 
[Install]
WantedBy=halt.target shutdown.target

I have assumed the Bash script is to backup /home, so change the directory list in ‘RequiresMountsFor=‘ if the script necessitates that other directories are still mounted – see ‘man systemd.unit‘ for details.

3. Enable the unit file and start the service as follows:

user $ sudo systemctl enable run_on_shutdown.service
user $ sudo reboot

From now on, the script will run to completion when you shutdown the machine, but not when you reboot it.

