# PPPwn - HEN PS4 11.00

COMMAND INSTALL :
```sh
git clone --recursive https://github.com/SUIJUNG/PPPwn
```
Install external / SDCARD
```sh
sudo bash /root/PPPwn/e
```
Install internal / EMMC
```sh
sudo bash /root/PPPwn/i
```
Hapus semua file yang ada di sdcard lalu copy file linux emmc ke sdcard lalu jalankan :
```sh
sudo mv -f /root/PPPwn/rc.local /etc/rc.local
```
```sh
sudo chmod +x /etc/rc.local
```
```sh
sudo bash /root/PPPwn/emmc
```

Credit : 
- TheOfficialFloW
- LightningMods
- SiSTR0
