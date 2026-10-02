#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mfahrianor - 2409106089
"""
Nama File : snmp_modul.py
Tujuan    : Mengambil sysName (OID 1.3.6.1.2.1.1.5.0) via SNMPv2c.
Pembuat   : mfahrianor - 2409106089
"""

import os
from identitas import kode_cabang

HOST = os.getenv("SNMP_HOST", "192.168.56.101")   # isi lewat env SNMP_HOST
COMMUNITY = f"comm_{kode_cabang}"
OID_SYSNAME = "1.3.6.1.2.1.1.5.0"


def _get_pysnmp_baru():
    """pysnmp >= 7 (asyncio)."""
    import asyncio
    from pysnmp.hlapi.v3arch.asyncio import (
        SnmpEngine, CommunityData, UdpTransportTarget,
        ContextData, ObjectType, ObjectIdentity, get_cmd)

    async def _run():
        target = await UdpTransportTarget.create((HOST, 161), timeout=2, retries=1)
        return await get_cmd(
            SnmpEngine(), CommunityData(COMMUNITY, mpModel=1), target,
            ContextData(), ObjectType(ObjectIdentity(OID_SYSNAME)))
    return asyncio.run(_run())


def _get_pysnmp_lama():
    """pysnmp 4.x / 6.x (sinkron)."""
    from pysnmp.hlapi import (
        SnmpEngine, CommunityData, UdpTransportTarget,
        ContextData, ObjectType, ObjectIdentity, getCmd)
    return next(getCmd(
        SnmpEngine(), CommunityData(COMMUNITY, mpModel=1),
        UdpTransportTarget((HOST, 161), timeout=2, retries=1),
        ContextData(), ObjectType(ObjectIdentity(OID_SYSNAME))))


def cek_snmp():
    """Return dict: status, sysName / error."""
    try:
        try:
            err_ind, err_stat, _, var_binds = _get_pysnmp_baru()
        except ImportError:
            err_ind, err_stat, _, var_binds = _get_pysnmp_lama()

        if err_ind:
            raise RuntimeError(str(err_ind))
        if err_stat:
            raise RuntimeError(err_stat.prettyPrint())
        nilai = var_binds[0][1].prettyPrint()
        print(f"[SNMP] sysName = {nilai}")
        return {"status": "BERHASIL", "sysName": nilai}
    except Exception as e:
        print(f"[SNMP] Gagal: {e}")
        return {"status": "GAGAL", "error": str(e)}
