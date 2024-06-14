import threading
import configparser
import subprocess
import time

class PPPwn:
    def __init__(self, config_file):
        self.arguments = self.read_arguments(config_file)

    def read_arguments(self, filename):
        config = configparser.ConfigParser()
        config.read(filename)
        return config['SETTINGS']

    def check_and_connect_interface(self, interface):
        subprocess.run(["sudo", "ip", "link", "show", interface], stdout=subprocess.DEVNULL)
        subprocess.run(["sudo", "ifup", interface], stdout=subprocess.DEVNULL)

    def run_hen(self):
        command = [
            "sudo", self.arguments.get('pppwn_path'),
            "-i", self.arguments.get('interface'),
            "--fw", self.arguments.get('fw'),
            "--stage1", self.arguments.get('stage1'),
            "--stage2", self.arguments.get('stage2'),
            "--timeout", self.arguments.get('timeout'),
            "--wait-after-pin", self.arguments.get('wait_after_pin'),
            "--groom-delay", self.arguments.get('groom_delay'),
            "--buffer-size", self.arguments.get('buffer_size'),
            "-a",
        ]
        process = subprocess.run(command)
        if process.returncode == 0:
            subprocess.run(["sudo", "shutdown", "-h", "now"])

    def detect_disconnected_interface(self, interface):
        while True:
            result = subprocess.run(["sudo", "ip", "link", "show", interface], capture_output=True)
            if b"state UP" not in result.stdout:
                print("\033[91mLAN TERPUTUS... Melakukan restart.\033[0m")
                time.sleep(5)
                subprocess.run(["sudo", "reboot"])

    def main(self):
        interface = self.arguments.get('interface')
        if interface:
            self.check_and_connect_interface(interface)
            while True:
                result = subprocess.run(["sudo", "ip", "link", "show", interface], capture_output=True)
                if b"state UP" in result.stdout:
                    print("\033[94mPS4 TERDETEKSI !!!\033[0m")
                    time.sleep(1)
                    pppwn_thread = threading.Thread(target=self.run_hen)
                    pppwn_thread.start()
                    self.detect_disconnected_interface(interface)
                    pppwn_thread.join()
                    break
                else:
                    print("\033[93mTIDAK TERHUBUNG... Pastikan koneksi LAN PS4 terhubung dengan STB.\033[0m")
                    time.sleep(1)

if __name__ == "__main__":
    watermark = "PPPwn C++ - 2024 bug-sys"
    print("\033[96m{}\033[0m".format(watermark))
    pppwn = PPPwn("config.ini")
    pppwn.main()
