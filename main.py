#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mfahrianor - 2409106089
"""
Nama File : main.py
Tujuan    : Integrasi semua modul dan mencetak laporan cabang gabungan.
Pembuat   : mfahrianor - 2409106089
"""

import identitas
import ssh_modul
import snmp_modul
import netconf_modul
import telemetry_modul


class LaporanCabang:
    def __init__(self, nama, nim, kode_cabang):
        self.nama = nama
        self.nim = nim
        self.kode_cabang = kode_cabang

    def tampilkan_laporan(self, hasil_ssh, hasil_snmp, pesan_netconf, hasil_telemetry):
        garis = "=" * 60
        print(f"\n{garis}\nLAPORAN AKHIR CABANG {self.kode_cabang}")
        print(f"{self.nama} - {self.nim}\n{garis}")
        print(f"ID Perangkat : {identitas.buat_id_perangkat('router', 1)}")
        print(f"\n[SSH]  Status : {hasil_ssh['status']}")
        for cmd, out in hasil_ssh["hasil"].items():
            print(f"       $ {cmd} -> {out.splitlines()[0] if out else '-'}")
        print(f"\n[SNMP] Status : {hasil_snmp['status']}")
        print(f"       sysName: {hasil_snmp.get('sysName', hasil_snmp.get('error'))}")
        print("\n[NETCONF] Pesan edit-config yang dibuat:")
        print(pesan_netconf)
        print("\n[TELEMETRY] Klasifikasi cpuUsage:")
        for nama, cpu, status in hasil_telemetry:
            print(f"       {nama}: {cpu}% -> {status}")
        print(garis)


def main():
    hasil_ssh = ssh_modul.cek_ssh()
    hasil_snmp = snmp_modul.cek_snmp()
    pesan = netconf_modul.buat_pesan_netconf()
    hasil_tele = telemetry_modul.klasifikasi_telemetry()
    LaporanCabang(identitas.nama, identitas.nim, identitas.kode_cabang) \
        .tampilkan_laporan(hasil_ssh, hasil_snmp, pesan, hasil_tele)


if __name__ == "__main__":
    main()
