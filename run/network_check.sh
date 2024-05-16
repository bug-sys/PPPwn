#!/bin/bash

# Fungsi untuk memeriksa dan menyambungkan end0 kembali
check_end0() {
    if ! ip link show end0 | grep -q "state UP"; then
        sudo ifup end0
    fi
}
