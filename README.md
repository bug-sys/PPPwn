# PPPwn - HEN PS4 11.00 ARM

!!!!  This exploit can only be run on LINUX DEBIAN 12  !!!!

INSTALL :
```sh
sudo apt install git -y
```
```sh
git clone --recursive https://github.com/bug-sys/PPPwn
```
```sh
sudo bash /root/PPPwn/install.all
```
Compile Stage:
```sh
make -C stage1 FW=1100 clean && make -C stage1 FW=1100
```
```sh
make -C stage2 FW=1100 clean && make -C stage2 FW=1100
```
Credit : 
- TheOfficialFloW
- LightningMods
- SiSTR0
- xfangfang
