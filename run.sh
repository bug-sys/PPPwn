#!/bin/bash

watermark_name() {
    echo -e "\033[1;35m"
    cat << "EOF"
88                                                                      
88                                                                      
echo88
88,dPPYba,  88       88  ,adPPYb,d8    ,adPPYba, 8b       d8 ,adPPYba,  
88P'    "8a 88       88 a8"    `Y88    I8[    "" `8b     d8' I8[    ""  
88       d8 88       88 8b       88     `"Y8ba,   `8b   d8'   `"Y8ba,   
88b,   ,a8" "8a,   ,a88 "8a,   ,d88    aa    ]8I   `8b,d8'   aa    ]8I  
8Y"Ybbd8"'   `"YbbdP'Y8  `"YbbdP"Y8    `"YbbdP"'     Y88'    `"YbbdP"'  
                         aa,    ,88                  d8'                
                          "Y8bbdP"                  d8'               
EOF
    echo -e "\033[0m"
    echo
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
            sudo shutdown -r now
            sleep 5
        fi
        sleep 1
    done
}

run_pppwn() {
    while true; do
        sudo "$pppwn" --interface "$interface" --fw "$fw" --stage1 "$stage1" --stage2 "$stage2" --timeout "$timeout" --wait-after-pin "$wait_after_pin" --groom-delay "$groom_delay" --buffer-size "$buffer_size" -a &
        pppwn_pid=$!
        check_connection &
        check_pid=$!
        wait $pppwn_pid > /dev/null 2>&1
        kill $check_pid > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            sudo shutdown -h now
            sleep 5
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
            echo -e "\033[91mTIDAK TERHUBUNG... Pastikan koneksi LAN PS4 terhubung dengan STB.\033[0m"
            sleep 1
        fi
    done
}

watermark_name
source config.ini
main_menu

exit 0
