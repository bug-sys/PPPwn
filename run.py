import subprocess
import time
import logging

# File untuk log debug
DEBUG_LOG = "/root/pppwn.txt"

# Inisialisasi logger
logging.basicConfig(filename=DEBUG_LOG, level=logging.DEBUG)
logger = logging.getLogger()

# Fungsi untuk menuliskan pesan debug ke file log dan terminal dengan warna kuning
def log_debug(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    formatted_message = f"[DEBUG] {timestamp} - {message}"
    print("\033[93m" + formatted_message + "\033[0m")
    logger.debug(formatted_message)

# Fungsi untuk memeriksa dan menyambungkan eth0
def periksa_eth0():
    log_debug("Memeriksa dan menyambungkan eth0...")
    subprocess.run(["sudo", "ip", "link", "show", "eth0"])
    subprocess.run(["sudo", "ifup", "eth0"])

# Fungsi untuk menjalankan pppwn
def jalankan_pppwn():
    log_debug("Menjalankan PPPwn...")
    subprocess.run([
        "sudo", "/root/PPPwn/pppwn",
        "--interface", "eth0",
        "--fw", "1100",
        "--stage1", "/root/PPPwn/stage1.bin",
        "--stage2", "/root/PPPwn/stage2.bin",
        "--auto-retry"
    ])
    if not subprocess.call(["sudo", "echo", "$?"]):
        log_debug("PPPwn berhasil dilakukan.")
        subprocess.run(["sudo", "shutdown", "now"])

# Fungsi untuk mendeteksi jika koneksi terputus
def deteksi_macet():
    log_debug("Memulai deteksi koneksi...")
    while True:
        result = subprocess.run(["sudo", "ip", "link", "show", "eth0"], capture_output=True)
        if b"state UP" not in result.stdout:
            log_debug("Koneksi eth0 terputus saat PPPwn sedang berjalan. Melakukan restart...")
            subprocess.run(["sudo", "reboot"])
        time.sleep(1)

# Skrip utama
if __name__ == "__main__":
    log_debug("Memulai skrip...")
    while True:
        periksa_eth0()
        result = subprocess.run(["sudo", "ip", "link", "show", "eth0"], capture_output=True)
        if b"state UP" in result.stdout:
            log_debug("PS4 TERDETEKSI !!!")
            log_debug("PS4 terdeteksi. Melakukan PPPwn...")
            subprocess.Popen(jalankan_pppwn)
            subprocess.Popen(deteksi_macet)
            time.sleep(1)  # Delay untuk memastikan subprocess telah dimulai
            subprocess.run(["sudo", "wait"])
        else:
            log_debug("TIDAK TERHUBUNG... Pastikan koneksi LAN PS4 terhubung dengan STB... Mencoba lagi.")
            time.sleep(5)
