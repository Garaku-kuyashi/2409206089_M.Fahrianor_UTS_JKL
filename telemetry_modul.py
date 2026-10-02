#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mfahrianor - 2409106089
"""
Nama File : telemetry_modul.py
Tujuan    : Mengklasifikasikan sampel data telemetry cpuUsage.
Pembuat   : mfahrianor - 2409106089
"""

from identitas import nim

DATA_TELEMETRY = {
    "sampel_1": {"timestamp": "2026-09-30T10:00:00", "cpuUsage": int(nim[-2:])},
    "sampel_2": {"timestamp": "2026-09-30T10:00:10", "cpuUsage": int(nim[-4:-2])},
    "sampel_3": {"timestamp": "2026-09-30T10:00:20", "cpuUsage": int(nim[-6:-4])},
    "sampel_4": {"timestamp": "2026-09-30T10:00:30", "cpuUsage": int(nim[-8:-6])},
}


def klasifikasi_telemetry():
    """Return list hasil klasifikasi dan mencetaknya."""
    hasil = []
    for nama, data in DATA_TELEMETRY.items():
        cpu = data["cpuUsage"]
        if cpu > 80:
            status = "KRITIS"
        elif cpu >= 50:
            status = "WASPADA"
        else:
            status = "NORMAL"
        hasil.append((nama, cpu, status))
        print(f"[TELEMETRY] {nama}: cpuUsage={cpu}% -> {status}")
    return hasil
