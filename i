#!/bin/bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 0E98404D386FA1D9
sudo apt update
sudo apt install python3-scapy -y
sudo rm /lib/systemd/system/bluetooth.target
sudo rm /lib/systemd/system/network-online.target
sudo mv -f /root/PPPwn/rc.local /etc/rc.local
sudo chmod +x /etc/rc.local
sudo mv -f /root/PPPwn/u-boot-default.img /boot/u-boot-default.img
sudo bash /root/PPPwn/emmc.sh
