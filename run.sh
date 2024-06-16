#!/bin/bash

# Fungsi untuk memastikan skrip pppwn dapat dieksekusi
ensure_pppwn_executable() {
    if [ ! -x "/root/PPPwn/pppwn" ]; then
        sudo chmod +x /root/PPPwn/pppwn
    fi
}

check_interface() {
    if ! ip link show "$interface" | grep -q "state UP"; then
        sudo ifup "$interface" 2>/dev/null
    fi
}

check_connection() {
    while true; do
        if ! ip link show "$interface" | grep -q "state UP"; then
            echo -e "\033[91mKoneksi PS4 terputus! Memulai ulang perangkat...\033[0m"
            sleep 5
            sudo shutdown -r now
        fi
    done
}

run_pppwn() {
    while true; do
        sudo /root/PPPwn/pppwn --interface "$interface" --fw "$fw" --stage1 "$stage1" --stage2 "$stage2" --timeout "$timeout" --groom-delay "$groom_delay" -a &
        pppwn_pid=$!
        check_connection &
        check_pid=$!
        wait $pppwn_pid > /dev/null 2>&1
        kill $check_pid > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            sleep 5
            sudo shutdown -h now
        fi
    done
}

main_menu() {
    ensure_pppwn_executable
    while true; do
        check_interface
        if ip link show "$interface" | grep -q "state UP"; then
            echo -e "\033[94mPS4 TERDETEKSI !!!\033[0m"
            run_pppwn
        else
            echo -e "\033[91mTIDAK TERHUBUNG... Pastikan koneksi LAN PS4 terhubung dengan STB.\033[0m"
            sleep 1
        fi
    done
}

# Sumberkan file konfigurasi
source /root/PPPwn/config.ini

# Titik masuk dari skrip
main_menu

exit 0
