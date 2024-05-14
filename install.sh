#!/bin/bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 0E98404D386FA1D9
sudo apt update -y
sudo apt-get install pv -y
sudo apt install python3-scapy -y
sudo apt install python3-tqdm -y
sudo rm /lib/systemd/system/bluetooth.target
sudo rm /lib/systemd/system/network-online.target
sudo mv -f /root/PPPwn/rc.local /etc/rc.local
sudo chmod +x /etc/rc.local
echo "*******************************************"
echo -e '\033[36mInstall complete,\033[33m Rebooting\033[0m'
echo "*******************************************"
sleep 5
reboot
