#!/bin/bash

# Function to check and reconnect end0
check_end0() {
    if ! ip link show end0 | grep -q "state UP"; then
        sudo ifup end0
    fi
}

# Function to run pppwn.py with retry
run_pppwn() {
    while true; do
        # Run pppwn.py in background
        sudo /root/PPPwn/pppwn --interface end0 --fw 1100 --stage1 "/root/PPPwn/stage1.bin" --stage2 "/root/PPPwn/stage2.bin" &
        # Set a timeout for pppwn.py
        timeout_duration=10
        pppwn_pid=$!
        { sleep "$timeout_duration"; kill -9 $pppwn_pid; } > /dev/null 2>&1 &
        wait $pppwn_pid > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            echo -e "\033[38;5;118m
          _   _ _____ _   _           ____  _____ ____  _   _    _    ____ ___ _             
         | | | | ____| \ | |         | __ )| ____|  _ \| | | |  / \  / ___|_ _| |            
         | |_| |  _| |  \| |  _____  |  _ \|  _| | |_) | |_| | / _ \ \___ \| || |            
  _ _ _ _|  _  | |___| |\  | |_____| | |_) | |___|  _ <|  _  |/ ___ \ ___) | || |___ _ _ _ _ 
 (_|_|_|_)_| |_|_____|_| \_|         |____/|_____|_| \_\_| |_/_/   \_\_🆂🆄🅸🅹🆄🅽🅶__(_|_|_|_)                                                                                                                                                                                
   \033[0m"
            sleep 6
	    sudo shutdown now
        else
            echo -ne "\033[91m[X][X][X][X][X][X][X][X][X][X] 𝗛𝗘𝗡 𝗚𝗔𝗚𝗔𝗟... 𝗠𝗘𝗠𝗨𝗟𝗔𝗜 𝗨𝗟𝗔𝗡𝗚 𝗦𝗧𝗕 ❗❗❗ [X][X][X][X][X][X][X][X][X][X]\033[0m"
	    sleep 6
            sudo reboot
        fi
    done
}

# Main script
# Loop until pppwn.py completes successfully
while true; do
    # Check and reconnect end0
    check_end0
    
    # Check if end0 is connected
    if ip link show end0 | grep -q "state UP"; then
        echo -e "\033[1;34m[+] 🅿🆂4 🆃🅴🆁🅳🅴🆃🅴🅺🆂🅸 ❗❗❗\033[0m"
        echo -e "\033[38;5;226m
              __  __ _____ __  __ _   _ _        _    ___           _   _ _____ _   _         
             |  \/  | ____|  \/  | | | | |      / \  |_ _|         | | | | ____| \ | |        
             | |\/| |  _| | |\/| | | | | |     / _ \  | |   _____  | |_| |  _| |  \| |        
      _ _ _ _| |  | | |___| |  | | |_| | |___ / ___ \ | |  |_____| |  _  | |___| |\  |_ _ _ _ 
     (_|_|_|_)_|  |_|_____|_|  |_|\___/|_____/_/   \_\___|         |_|🆂🆄🅸🅹🆄🅽🅶| \_(_|_|_|_)                                                                                                                                                                                                                                            
     \033[0m"
        # Run pppwn.py with retry
        run_pppwn
        # If pppwn.py fails, it will restart the device
        # So, no need to execute any further commands here
    else
        echo -ne "\033[91m[X] 𝗧𝗜𝗗𝗔𝗞 𝗧𝗘𝗥𝗛𝗨𝗕𝗨𝗡𝗚... 𝗣𝗔𝗦𝗧𝗜𝗞𝗔𝗡 𝗞𝗢𝗡𝗘𝗞𝗦𝗜 𝗟𝗔𝗡 𝗣𝗦𝟰 𝗔𝗡𝗗𝗔 𝗧𝗘𝗥𝗛𝗨𝗕𝗨𝗡𝗚 𝗗𝗘𝗡𝗚𝗔𝗡 𝗦𝗧𝗕... 𝗠𝗘𝗡𝗖𝗢𝗕𝗔 𝗟𝗔𝗚𝗜 ❗❗❗\033[0m"
        sleep 5
    fi
done

exit 0
