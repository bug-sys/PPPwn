import subprocess
import time
import threading

class PPPwn:
    def __init__(self, config_file):
        self.arguments = self.read_arguments(config_file)

    def read_arguments(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        argumen = {}
        for line in lines:
            key, value = line.strip().split(': ')
            argumen[key] = value
        return argumen

    def check_and_connect_interface(self, interface):
        subprocess.run(["sudo", "ip", "link", "show", interface])
        subprocess.run(["sudo", "ifup", interface])

    def run_hen(self):
        command = [
            "sudo", self.arguments['pppwn_path'],
            "-i", self.arguments['--interface'],
            "--fw", self.arguments['--fw'],
            "--stage1", self.arguments['--stage1'],
            "--stage2", self.arguments['--stage2'],
            "--timeout", self.arguments['--timeout'],
            "--wait-after-pin", self.arguments['--wait-after-pin'],
            "--groom-delay", self.arguments['--groom-delay'],
            "--buffer-size", self.arguments['--buffer-size'],
            "-a" if self.arguments.get('--auto-retry') == 'true' else '',
            "-nw" if self.arguments.get('--no-wait-padi') == 'true' else '',
            "-rs" if self.arguments.get('--real-sleep') == 'true' else ''
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
        interface = self.arguments.get('--interface')
        if interface:
            self.check_and_connect_interface(interface)
            result = subprocess.run(["sudo", "ip", "link", "show", interface], capture_output=True)
            if b"state UP" in result.stdout:
                pppwn_thread = threading.Thread(target=self.run_hen)
                pppwn_thread.start()
                self.detect_disconnected_interface(interface)
                pppwn_thread.join()
            else:
                print("TIDAK TERHUBUNG... Pastikan koneksi LAN PS4 terhubung dengan STB.")

if __name__ == "__main__":
    pppwn = PPPwn("config.ini")
    pppwn.main()