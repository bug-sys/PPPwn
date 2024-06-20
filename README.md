# PPPwn C++ PS4 HEN STB

### instalasi STB :
```sh
sudo apt install git -y
```
```sh
git clone --recursive --depth 1 https://github.com/bug-sys/PPPwn
```
```sh
sudo bash /root/PPPwn/install.all
```

### instalasi goldhen.bin
- Menggunakan PC atau Mac, format drive USB sebagai FAT32 atau exFAT.
- Unduh file PPPwn dan salin goldhen.bin ke drive USB tanpa folder.
- Colokkan drive USB yang berisi file goldhen.bin ke konsol PS4.
- Mulai konsol PS4 dan nyalakan STB, tunggu sampai proses selesai, jika sudah selesai akan ada notif HEN BERHASIL.
- Jika konsol PS4 Anda tidak mengenali file goldhen.bin , periksa apakah file goldhen.bin ada di drive USB.
- Dan jika sudah ada notif HEN BERHASIL kedepan nya tidak memerlukan drive USB dan dapat langsung melanjutkan nyalakan STB untuk aktifasi hen.

### pengaturan config.ini :
- `pppwn`: tentukan lokasi pppwn (default = `/root/PPPwn/pppwn`)
- `interface`: antarmuka jaringan yang terhubung ke PS4 `eth0` ubuntu - debian 12 kebawah , `end0` debian 13 (default = `eth0`)
- `fw`: versi firmware PS4 target 0900 / 1100 (default = `1100`)
- `stage1`: jalur ke payload stage1 (default = `/root/PPPwn/1100/stage1.bin`)
- `stage2`: jalur ke payload stage2 (default = `/root/PPPwn/1100/stage2.bin`)
- `timeout`: batas waktu dalam hitungan detik untuk respon PS4, 0 berarti selalu menunggu (default = `0`)
- `groom_delay`: tunggu 1 md setiap putaran `groom-delay` selama perawatan Heap (default = `4`)

### credit :
- TheOfficialFloW
- xfangfang
- SiSTR0
