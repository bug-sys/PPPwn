from argparse import ArgumentParser
import psutil
from exploit import *
from offsets import *


def main():
    # Parser argumen untuk pppwn
    global offs
    parser = ArgumentParser('pppwn')
    parser.add_argument('--fw', default='1100')
    parser.add_argument('--interface', default=None)
    parser.add_argument('--stage1', default=None)  # Atur default menjadi None
    parser.add_argument('--stage2', default=None)  # Atur default menjadi None
    args = parser.parse_args()

    print("\033[1;32mPorting by bug-sys - 2024 (c)\033[0m")

    # Tentukan direktori dari main.py
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Tentukan jalur stage1 dan stage2
    if args.stage1 is None:
        args.stage1 = os.path.join(current_dir, 'stage1.bin')
    if args.stage2 is None:
        args.stage2 = os.path.join(current_dir, 'stage2.bin')

    while True:
        with open(args.stage1, mode='rb') as f:
            stage1 = f.read()

        with open(args.stage2, mode='rb') as f:
            stage2 = f.read()

        if args.fw == '1100':
            offs = OffsetsFirmware_1100()

        selected_interface = args.interface

        # Jika interface belum ditentukan secara manual, coba deteksi otomatis
        if not selected_interface:
            adapters = [interface for interface, addrs in psutil.net_if_addrs().items() if
                        any(addr.family == psutil.AF_LINK for addr in addrs)]
            for adapter in adapters:
                if adapter in ['eth0', 'enp0s3', 'end0', 'Ethernet']:
                    selected_interface = adapter
                    break

        if selected_interface:
            print(f"\033[94mLAN Terdeteksi: {selected_interface}\033[0m")
        else:
            print("\033[91mTidak ada LAN yang sesuai dengan yang diharapkan.\033[0m")

        # Buat objek exploit dan jalankan
        exploit = Exploit(offs, selected_interface, stage1, stage2)
        try:
            exploit.run()
        except SystemExit as e:
            if e.code != 1:
                raise
            continue
        break

    return 0


if __name__ == '__main__':
    # Keluar dengan kode keluaran utama
    exit(main())
