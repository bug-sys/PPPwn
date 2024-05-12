#!/bin/bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 0E98404D386FA1D9
sudo bash /root/PPPwn/update_python.sh
sudo rm /lib/systemd/system/bluetooth.target
sudo rm /lib/systemd/system/network-online.target
sudo mv -f /root/PPPwn/rc.local /etc/rc.local
sudo chmod +x /etc/rc.local
echo -e '\033[36mInstallation complete,\033[33m Restarting\033[0m'
sudo reboot
