#!/bin/bash

# Fungsi untuk menjalankan pppwn dengan percobaan ulang
run_pppwn() {
    while true; do
        # Menjalankan pppwn di latar belakang
        /root/PPPwn/./pppwn --interface end0 --fw 1100 --stage1 "/root/PPPwn/stage1.bin" --stage2 "/root/PPPwn/stage2.bin" &
        # Menetapkan batas waktu untuk pppwn
        timeout_duration=90
        pppwn_pid=$!
        { sleep "$timeout_duration"; kill -9 $pppwn_pid; } & # Menetapkan batas waktu untuk pppwn
        wait $pppwn_pid
        if [ $? -eq 0 ]; then
            pppwn_success_message
            sleep 8 
            sudo shutdown now
        else
            pppwn_failure_message
            sleep 8
            sudo reboot
        fi
    done
}
