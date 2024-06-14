# PPPwn C++ - PS4 HEN FW 9.00 / 9.60 / 10.00 / 10.01 / 11.00

### config.ini :
- `interface`: antarmuka jaringan yang terhubung ke ps4 (default = `eth0`)
- `fw`: versi firmware ps4 target (default = `1100`)
- `stage1`: jalur ke payload stage1 (default = `/root/PPPwn/stage1.bin`)
- `stage2`: jalur ke payload stage2 (default = `/root/PPPwn/stage2.bin`)
- `timeout`: batas waktu dalam hitungan detik untuk respon ps4, 0 berarti selalu menunggu (default = `0`)
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
Credit : 
- TheOfficialFloW
- LightningMods
- SiSTR0
- xfangfang
