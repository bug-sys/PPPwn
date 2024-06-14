import subprocess
import time
import threading
import configparser

class PPPwn:
    def __init__(self, config_file):
        self.arguments = self.read_arguments(config_file)

    def read_arguments(self, filename):
        config = configparser.ConfigParser()
        config.read(filename)
        return config['SETTINGS']

    def check_and_connect_interface(self, interface):
        subprocess.run(["sudo", "ip", "link", "show", interface])
        subprocess.run(["sudo", "ifup", interface])

    def run_hen(self):
        command = [
            "sudo", self.arguments['pppwn_path'],
            "-i", self.arguments['interface'],
            "--fw", self.arguments['fw'],
            "--stage1", self.arguments['stage1'],
            "--stage2", self.arguments['stage2'],
            "--timeout", self.arguments['timeout'],
            "--wait-after-pin", self.arguments['wait_after_pin'],
            "--groom-delay", self.arguments['groom_delay'],
            "--buffer-size", self.arguments['buffer_size'],
            "-a", self.arguments['auto_retry'],
            "-nw", self.arguments['no_wait_padi'],
            "-rs", self.arguments['real_sleep'],
        ]
        subprocess.run(command)

    def detect_disconnected_interface(self, interface):
        while True:
            result = subprocess.run(["sudo", "ip", "link", "show", interface], capture_output=True)
            if b"state UP" not in result.stdout:
                print("LAN TERPUTUS... Melakukan restart.")
                subprocess.run(["sudo", "reboot"])
            time.sleep(1)

    def main(self):
        interface = self.arguments.get('interface')
        if interface:
            self.check_and_connect_interface(interface)
            while True:
                result = subprocess.run(["sudo", "ip", "link", "show", interface], capture_output=True)
                if b"state UP" in result.stdout:
                    pppwn_thread = threading.Thread(target=self.run_hen)
                    pppwn_thread.start()
                    self.detect_disconnected_interface(interface)
                    pppwn_thread.join()
                    break
                else:
                    print("TIDAK TERHUBUNG... Pastikan koneksi LAN PS4 terhubung dengan STB.")
                    time.sleep(1)

if __name__ == "__main__":
    pppwn = PPPwn("config.ini")
    pppwn.main()
