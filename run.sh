#!/bin/bash

# Function to check and reconnect eth0
check_eth0() {
    if ! ip link show eth0 | grep -q "state UP"; then
        sudo ifup eth0
    fi
}

# Function to run pppwn.py with retry
run_pppwn() {
    while true; do
        # Run pppwn.py in background
        sudo /root/PPPwn/pppwn --interface eth0 --fw 1100 --stage1 "/root/PPPwn/stage1.bin" --stage2 "/root/PPPwn/stage2.bin" &
        # Set a timeout for pppwn.py
        timeout_duration=90
        pppwn_pid=$!
        { sleep "$timeout_duration"; kill -9 $pppwn_pid; } > /dev/null 2>&1 &
        wait $pppwn_pid > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            echo -e "\033[38;5;118m
          _   _ _____ _   _           ____  _____ ____  _   _    _    ____ ___ _             
         | | | | ____| \ | |         | __ )| ____|  _ \| | | |  / \  / ___|_ _| |            
         | |_| |  _| |  \| |  _____  |  _ \|  _| | |_) | |_| | / _ \ \___ \| || |            
  _ _ _ _|  _  | |___| |\  | |_____| | |_) | |___|  _ <|  _  |/ ___ \ ___) | || |___ _ _ _ _ 
 (_|_|_|_)_| |_|_____|_| \_|         |____/|_____|_| \_\_| |_/_/   \_\_____SUIJUNG__(_|_|_|_)                                                                                                                                                                                
   \033[0m"
            sleep 6
	    sudo shutdown now
        else
            echo -ne "\033[91m[X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X] HEN GAGAL... MEMULAI ULANG STB !!! [X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X][X]\033[0m"
	    sleep 6
            sudo reboot
        fi
    done
}

# Main script
# Loop until pppwn.py completes successfully
while true; do
    # Check and reconnect eth0
    check_eth0
    
    # Check if eth0 is connected
    if ip link show eth0 | grep -q "state UP"; then
        echo -e "\033[1;34m[+] PS4 TERDETEKSI !!!\033[0m"
        echo -e "\033[38;5;226m
              __  __ _____ __  __ _   _ _        _    ___           _   _ _____ _   _         
             |  \/  | ____|  \/  | | | | |      / \  |_ _|         | | | | ____| \ | |        
             | |\/| |  _| | |\/| | | | | |     / _ \  | |   _____  | |_| |  _| |  \| |        
      _ _ _ _| |  | | |___| |  | | |_| | |___ / ___ \ | |  |_____| |  _  | |___| |\  |_ _ _ _ 
     (_|_|_|_)_|  |_|_____|_|  |_|\___/|_____/_/   \_\___|         |_| |_SUIJUNG_| \_(_|_|_|_)                                                                                                                                                                                                                                           
     \033[0m"
        # Run pppwn.py with retry
        run_pppwn
        # If pppwn.py fails, it will restart the device
        # So, no need to execute any further commands here
    else
        echo -ne "\033[91m[-] TIDAK TERHUBUNG... PASTIKAN KONEKSI LAN PS4 ANDA TERHUBUNG DENGAN STB... MENCOBA LAGI !!!\033[0m"
        sleep 5
    fi
done

exit 0
