#!/bin/bash

# Pastikan menjalankan skrip sebagai root
if [[ $EUID -ne 0 ]]; then
    echo "Skrip ini harus dijalankan sebagai root" 
    exit 1
fi

# Update sistem
apt update
apt upgrade -y

# Instal dependensi yang diperlukan
apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget

# Unduh sumber Python terbaru
PYTHON_VERSION="3.10.0"  # Ganti dengan versi Python terbaru yang diinginkan
wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz

# Ekstrak arsip Python
tar -xzvf Python-$PYTHON_VERSION.tgz

# Pindah ke direktori Python yang diekstrak
cd Python-$PYTHON_VERSION

# Konfigurasi dan instalasi
./configure --enable-optimizations
make -j$(nproc)
make altinstall

# Hapus arsip yang tidak diperlukan
rm Python-$PYTHON_VERSION.tgz

echo "Python $PYTHON_VERSION telah berhasil diinstal."

# Update Scapy ke versi 2.5.0
pip3.10 install --upgrade scapy==2.5.0

echo "Scapy telah berhasil diperbarui ke versi 2.5.0."
