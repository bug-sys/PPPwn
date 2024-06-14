import subprocess
import time
import threading
import psutil

class PS4HEN:
    def __init__(self):
        self.pppwn_path = "./PPPwn/pppwn"
        self.fw_value = "1100"
        self.stage1_bin = "./PPPwn/stage1.bin"
        self.stage2_bin = "./PPPwn/stage2.bin"

    def print(self, message):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"{timestamp} - {message}"
        print(formatted_message)

    def check_interface(self):
        interfaces = psutil.net_if_addrs().keys()
        if 'eth0' in interfaces:
            self.interface = 'eth0'
        elif 'end0' in interfaces:
            self.interface = 'end0'
        else:
            exit(1)

    def run_pppwn(self):
        while True:
            result = subprocess.run([
                "sudo", self.pppwn_path,
                "-i", self.interface,
                "--fw", self.fw_value,
                "-s1", self.stage1_bin,
                "-s2", self.stage2_bin,
                "-t",
                "-a"
            ])
            if result.returncode == 0:
                subprocess.run(["sudo", "shutdown", "now"])
                break

    def detect_timeout(self):
        while True:
            result = subprocess.run(["sudo", "ip", "link", "show", self.interface], capture_output=True)
            if b"state UP" not in result.stdout:
                self.print("Koneksi LAN terputus. Melakukan restart...")
                subprocess.run(["sudo", "reboot"])
            else:
                time.sleep(1)

def main():
    ps4_hen = PS4HEN()
    ps4_hen.check_interface()
    
    while True:
        result = subprocess.run(["sudo", "ip", "link", "show", ps4_hen.interface], capture_output=True)
        if b"state UP" in result.stdout:
            ps4_hen.print("PS4 TERDETEKSI !!!")
            pppwn_thread = threading.Thread(target=ps4_hen.run_pppwn)
            pppwn_thread.start()
            timeout_thread = threading.Thread(target=ps4_hen.detect_timeout)
            timeout_thread.start()
            pppwn_thread.join()
            timeout_thread.join()
        else:
            ps4_hen.print("TIDAK TERHUBUNG... Pastikan koneksi LAN PS4 terhubung dengan STB... Mencoba lagi.")
            time.sleep(5)

if __name__ == "__main__":
    main()
