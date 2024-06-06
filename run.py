import subprocess
import time
import threading

# Fungsi untuk mencetak pesan dengan warna kuning
def print_yellow(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    formatted_message = f"[DEBUG] {timestamp} - {message}"
    print("\033[93m" + formatted_message + "\033[0m")

# Fungsi untuk memeriksa dan menyambungkan eth0
def periksa_eth0():
    print_yellow("Memeriksa dan menyambungkan eth0...")
    subprocess.run(["sudo", "ip", "link", "show", "eth0"])
    subprocess.run(["sudo", "ifup", "eth0"])

# Fungsi untuk menjalankan pppwn
def jalankan_pppwn():
    while True:
        print_yellow("Menjalankan PPPwn...")
        result = subprocess.run([
            "sudo", "/root/PPPwn/pppwn",
            "-i", "eth0",
            "--fw", "1100",
            "-s1", "/root/PPPwn/stage1.bin",
            "-s2", "/root/PPPwn/stage2.bin",
            "-t", "10",
            "-a",
            "-wap", "1",
            "-gd", "8",
            "-bs", "20480",
            "-nw",
            "-rs"
        ])
        if result.returncode == 0:
            print_yellow("PPPwn berhasil dilakukan.")
            subprocess.run(["sudo", "shutdown", "now"])
            break  # Keluar dari loop jika PPPwn berhasil
        else:
            print_yellow("PPPwn gagal dilakukan. Akan mencoba lagi.")

# Fungsi untuk mendeteksi jika koneksi terputus
def deteksi_macet():
    print_yellow("Memulai deteksi koneksi...")
    while True:
        result = subprocess.run(["sudo", "ip", "link", "show", "eth0"], capture_output=True)
        if b"state UP" not in result.stdout:
            print_yellow("Koneksi eth0 terputus saat PPPwn sedang berjalan. Melakukan restart...")
            subprocess.run(["sudo", "reboot"])
        else:
            print_yellow("Koneksi eth0 masih terhubung.")
        time.sleep(1)

# Skrip utama
if __name__ == "__main__":
    print_yellow("Memulai skrip...")
    while True:
        periksa_eth0()
        result = subprocess.run(["sudo", "ip", "link", "show", "eth0"], capture_output=True)
        if b"state UP" in result.stdout:
            print_yellow("PS4 TERDETEKSI !!!")
            print_yellow("PS4 terdeteksi. Melakukan PPPwn...")
            pppwn_thread = threading.Thread(target=jalankan_pppwn)
            pppwn_thread.start()
            deteksi_macet()
            pppwn_thread.join()  # Pastikan proses PPPwn selesai sebelum lanjut ke iterasi berikutnya
        else:
            print_yellow("TIDAK TERHUBUNG... Pastikan koneksi LAN PS4 terhubung dengan STB... Mencoba lagi.")
            time.sleep(5)
