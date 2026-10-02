#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mfahrianor - 2409106089
"""
Nama File : ssh_modul.py
Tujuan    : Login SSH ke VM/laptop dan menjalankan perintah diagnostik.
Pembuat   : mfahrianor - 2409106089
"""

import os
import paramiko
from identitas import kode_cabang

HOST = os.getenv("SSH_HOST", "192.168.1.6")   
PORT = int(os.getenv("SSH_PORT", "22"))
USERNAME = f"admin_{kode_cabang}"
PASSWORD = os.getenv("SSH_PASSWORD", "")          
PERINTAH = ["hostname", "uptime", "df -h /"]


def cek_ssh():
    """Return dict: status, hasil (perintah -> output) atau error."""
    hasil = {}
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(HOST, port=PORT, username=USERNAME,
                       password=PASSWORD, timeout=5)
        for cmd in PERINTAH:
            _, stdout, _ = client.exec_command(cmd)
            hasil[cmd] = stdout.read().decode().strip()
            print(f"[SSH] $ {cmd}\n{hasil[cmd]}")
        return {"status": "BERHASIL", "hasil": hasil}
    except Exception as e:
        print(f"[SSH] Gagal: {e}")
        return {"status": "GAGAL", "hasil": hasil, "error": str(e)}
    finally:
        client.close()
