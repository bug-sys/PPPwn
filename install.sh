#!/bin/bash

# Menambahkan kunci publik untuk paket Python
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 0E98404D386FA1D9

# Memperbarui daftar paket
sudo apt-get update

# Menginstal paket python3-scapy
sudo apt install python3-scapy -y

# Menghapus target bluetooth dan target network-online
sudo rm /lib/systemd/system/bluetooth.target
sudo rm /lib/systemd/system/network-online.target

# Menyunting file /etc/rc.local untuk menghilangkan baris "exit 0" dan menambahkan perintah untuk menjalankan script run.sh
sudo sed -i 's^"exit 0"^"exit"^g' /etc/rc.local
sudo sed -i 's^sudo bash /root/PPPwnAB/run.sh \&^^g' /etc/rc.local
sudo sed -i 's^exit 0^sudo bash /root/PPPwnAB/run.sh \&\n\nexit 0^g' /etc/rc.local

# Pesan untuk menunjukkan bahwa instalasi sudah selesai dan akan melakukan reboot
echo -e '\033[36mInstalasi selesai,\033[33m Restarting\033[0m'
sudo reboot
