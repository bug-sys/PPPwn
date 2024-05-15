#!/bin/bash
sudo apt update -y
sudo apt-get install pv -y
sudo apt install python3-scapy -y
sudo apt install python3-tqdm -y
sudo mv -f /root/PPPwn/rc.local /etc/rc.local
sudo chmod +x /etc/rc.local
sudo chmod +x /root/PPPwn/pppwn
echo "*******************************************"
echo -e '\033[36mInstall complete,\033[33m Rebooting\033[0m'
echo "*******************************************"
sleep 5
reboot
