#!/bin/bash

# Fungsi utama untuk memeriksa dan menjalankan skrip
main_pppwn() {
    while true; do
        # Periksa dan sambungkan end0
        check_end0
        
        # Periksa apakah end0 terhubung
        if ip link show end0 | grep -q "state UP"; then
            # Menampilkan pesan PS4 terdeteksi
            display_ps4_detected_message
            
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
