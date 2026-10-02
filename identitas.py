#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mfahrianor - 2409106089
"""
Nama File : identitas.py
Tujuan    : Menyimpan identitas cabang dan pembuat ID perangkat.
Pembuat   : mfahrianor - 2409106089
"""

nim = "2409106089"
nama = "mfahrianor"
kode_cabang = nim[-3:]  


def buat_id_perangkat(jenis, nomor):
    """Contoh: buat_id_perangkat('router', 1) -> 'ROUTER-123-01'"""
    return f"{jenis.upper()}-{kode_cabang}-{int(nomor):02d}"


if __name__ == "__main__":
    print(nim, nama, kode_cabang, buat_id_perangkat("router", 1))
