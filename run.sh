#!/bin/bash

source config.ini

check_interface() {
    if ! ip link show "$interface" | grep -q "state UP"; then
        sudo ifup "$interface"
    fi
}

run_pppwn() {
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

main_menu() {
    while true; do
        check_interface
        if ip link show "$interface" | grep -q "state UP"; then
            echo -e "\033[94mPS4 TERDETEKSI !!!\033[0m"
            run_pppwn
        else
            echo -e "\033[93mTIDAK TERHUBUNG... Pastikan koneksi LAN PS4 terhubung dengan STB.\033[0m"
            sleep 5
        fi
    done
}

main_menu

exit 0
