# PPPwn C++ - PS4 HEN STB

### config.ini :
- `pppwn`: tentukan lokasi pppwn (default = `/root/PPPwn/pppwn`)
- `interface`: antarmuka jaringan yang terhubung ke PS4 `eth0` ubuntu - debian 12 kebawah , `end0` debian 13 (default = `eth0`)
- `fw`: versi firmware PS4 target 0900 / 1100 (default = `1100`)
- `stage1`: jalur ke payload stage1 (default = `/root/PPPwn/1100/stage1.bin`)
- `stage2`: jalur ke payload stage2 (default = `/root/PPPwn/1100/stage2.bin`)
- `timeout`: batas waktu dalam hitungan detik untuk respon PS4, 0 berarti selalu menunggu (default = `0`)
- `wait_after_pin`: waktu tunggu dalam hitungan detik setelah penyematan CPU putaran pertama (default = `1`)
- `groom_delay`: tunggu 1 md setiap putaran `groom-delay` selama perawatan Heap (default = `4`)
- `buffer_size`: Ukuran buffer PCAP dalam byte, kurang dari 100 menunjukkan nilai default (biasanya 2MB) (default = `0`)

### INSTALL :
```sh
sudo apt install git -y
```
```sh
git clone --recursive --depth 1 https://github.com/bug-sys/PPPwn
```
```sh
sudo bash /root/PPPwn/install.all
```
***Credit :*** 

- _TheOfficialFloW
- LightningMods
- SiSTR0_
