#!/bin/bash

# Fungsi untuk menampilkan pesan kegagalan koneksi jaringan
network_connection_failure_message() {
    echo -ne "\033[91m[-]TIDAK TERHUBUNG... PASTIKAN KONEKSI LAN PS4 ANDA TERHUBUNG DENGAN STB... MENCOBA LAGI DALAM 5 DETIK !!!\033[0m"
}

# Fungsi untuk menampilkan pesan kegagalan pppwn
pppwn_failure_message() {
    echo -ne "\033[91m[*] HEN GAGAL... MEMULAI ULANG STB !!!\033[0m"
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
    echo -e "\033[1;34m[+]PS4 TERDETEKSI !!!\033[0m"
    echo -e "\033[38;5;226m
              __  __ _____ __  __ _   _ _        _    ___           _   _ _____ _   _         
             |  \/  | ____|  \/  | | | | |      / \  |_ _|         | | | | ____| \ | |        
             | |\/| |  _| | |\/| | | | | |     / _ \  | |   _____  | |_| |  _| |  \| |        
      _ _ _ _| |  | | |___| |  | | |_| | |___ / ___ \ | |  |_____| |  _  | |___| |\  |_ _ _ _ 
     (_|_|_|_)_|  |_|_____|_|  |_|\___/|_____/_/   \_\___|         |_| |_|_____|_| \_(_|_|_|_)
                                                                                                                                                                                                                                             
    \033[0m"
}
