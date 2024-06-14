# PPPwn - HEN PS4 11.00 ARM

!!!!  This exploit can only be run on LINUX DEBIAN 12 & UBUNTU 22.04 !!!!

UPDATE:

[SETTINGS]
pppwn_path = /root/PPPwn/pppwn
interface = eth0
fw = 1100
stage1 = /root/PPPwn/stage1.bin
stage2 = /root/PPPwn/stage2.bin
timeout = 0
wait_after_pin = 1
groom_delay = 4
buffer_size = 0

INSTALL :
```sh
sudo apt install git -y
```
```sh
git clone --recursive --depth 1 https://github.com/bug-sys/PPPwn
```
```sh
sudo bash /root/PPPwn/install.all
```
Credit : 
- TheOfficialFloW
- LightningMods
- SiSTR0
- xfangfang
