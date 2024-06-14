#!/bin/bash

# Load configuration from config.ini
source config.ini

check_interface() {
    if ! ip link show "$interface" | grep -q "state UP"; then
        sudo ifup "$interface"
    fi
}

run_hen() {
    while true; do
        pppwn_pid=
        /root/PPPwn/pppwn --interface "$interface" --fw "$fw" --stage1 "$stage1" --stage2 "$stage2" --timeout "$timeout" --wait-after-pin "$wait_after_pin" --groom-delay "$groom_delay" --buffer-size "$buffer_size" --auto-retry
        pppwn_pid=$!
        wait $pppwn_pid > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            sleep 5
            sudo shutdown now
        fi
    done
}

main() {
    while true; do
        check_interface
        if ip link show "$interface" | grep -q "state UP"; then
            echo -e "\033[1;34m[+] PS4 TERDETEKSI !!!\033[0m"
            run_hen
        else
            echo -ne "\033[91m[-] TIDAK TERHUBUNG... PASTIKAN KONEKSI LAN PS4 ANDA TERHUBUNG DENGAN STB... MENCOBA LAGI !!!\033[0m"
            sleep 5
        fi
    done
}

main

exit 0
