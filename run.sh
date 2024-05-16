#!/bin/bash

# Fungsi untuk memeriksa dan menyambungkan end0 kembali
check_end0() {
    if ! ip link show end0 | grep -q "state UP"; then
        sudo ifup end0
    fi
}

# Fungsi untuk menjalankan pppwn dengan percobaan ulang
run_pppwn() {
    while true; do
        # Menjalankan pppwn di latar belakang
        sudo /root/PPPwn/pppwn --interface end0 --fw 1100 --stage1 "/root/PPPwn/stage1.bin" --stage2 "/root/PPPwn/stage2.bin" &
        pppwn_pid=$!
        # Menunggu perintah pppwn selesai dengan batasan waktu
        if wait $pppwn_pid; then
            pppwn_success_message
            # Menunggu sebentar sebelum melakukan Shutdown otomatis
            sleep 8 
            # Shutdown otomatis
            sudo shutdown now
        else
            pppwn_failure_message
            # Menunggu sebentar sebelum melakukan restart otomatis
            sleep 8
            # Restart otomatis
            sudo reboot
        fi
    done
}


# Fungsi untuk menampilkan pesan kegagalan koneksi jaringan
network_connection_failure_message() {
    echo -ne "\033[91m[-] TIDAK TERHUBUNG... PASTIKAN KONEKSI LAN PS4 ANDA TERHUBUNG DENGAN STB... MENCOBA LAGI DALAM 5 DETIK !!!\033[0m"
}

# Fungsi untuk menampilkan pesan kegagalan pppwn
pppwn_failure_message() {
    echo -ne "\033[91m[*] HEN GAGAL... MEMULAI ULANG STB DALAM 8 DETIK !!!\033[0m"
}

# Fungsi untuk menampilkan pesan kesuksesan pppwn
pppwn_success_message() {
    echo -e "\033[38;5;118m
          _   _ _____ _   _           ____  _____ ____  _   _    _    ____ ___ _             
         | | | | ____| \ | |         | __ )| ____|  _ \| | | |  / \  / ___|_ _| |            
         | |_| |  _| |  \| |  _____  |  _ \|  _| | |_) | |_| | / _ \ \___ \| || |            
  _ _ _ _|  _  | |___| |\  | |_____| | |_) | |___|  _ <|  _  |/ ___ \ ___) | || |___ _ _ _ _ 
 (_|_|_|_)_| |_|_____|_| \_|         |____/|_____|_| \_\_| |_/_/   \_\____/___|_____(_|_|_|_)                                                                                                                                                                                
   \033[0m"
}

# Fungsi untuk menampilkan pesan PS4 terdeteksi
display_ps4_detected_message() {
    echo -e "\033[1;34m[+] PS4 TERDETEKSI !!!\033[0m"
    echo -e "\033[38;5;226m
              __  __ _____ __  __ _   _ _        _    ___           _   _ _____ _   _         
             |  \/  | ____|  \/  | | | | |      / \  |_ _|         | | | | ____| \ | |        
             | |\/| |  _| | |\/| | | | | |     / _ \  | |   _____  | |_| |  _| |  \| |        
      _ _ _ _| |  | | |___| |  | | |_| | |___ / ___ \ | |  |_____| |  _  | |___| |\  |_ _ _ _ 
     (_|_|_|_)_|  |_|_____|_|  |_|\___/|_____/_/   \_\___|         |_| |_|_____|_| \_(_|_|_|_)                                                                                                                                                                                                                                            
     \033[0m"
}

# Fungsi utama untuk memeriksa dan menjalankan skrip
main_pppwn() {
    while true; do
        # Periksa dan sambungkan end0
        check_end0
        
        # Periksa apakah end0 terhubung
        if ip link show end0 | grep -q "state UP"; then
            # Menampilkan pesan PS4 terdeteksi
            display_ps4_detected_message
            
            # Mencoba restart koneksi Ethernet sampai terhubung
            restart_ethernet_connection
            
            # Jalankan pppwn dengan percobaan ulang
            run_pppwn
            # Jika pppwn gagal, perangkat akan dimulai ulang
            # Jadi, tidak perlu menjalankan perintah lebih lanjut di sini
        else
            network_connection_failure_message
            sleep 5
        fi
    done
}

# Menjalankan skrip utama
main_pppwn
