#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mfahrianor - 2409106089
"""
Nama File : netconf_modul.py
Tujuan    : Membangun pesan XML <rpc><edit-config> untuk membuat VLAN.
Pembuat   : mfahrianor - 2409106089
"""

import xml.etree.ElementTree as ET
from identitas import kode_cabang

NS_BASE = "urn:ietf:params:xml:ns:netconf:base:1.0"
NS_VLAN = "http://openconfig.net/yang/vlan"


def buat_pesan_netconf():
    """Membangun string XML edit-config VLAN ID = kode_cabang."""
    vlan_id = int(kode_cabang)

    # === MESSAGES LAYER: elemen <rpc> pembungkus + message-id ===
    rpc = ET.Element("rpc", {"xmlns": NS_BASE, "message-id": "101"})

    # === OPERATIONS LAYER: operasi <edit-config> pada datastore running ===
    edit = ET.SubElement(rpc, "edit-config")
    target = ET.SubElement(edit, "target")
    ET.SubElement(target, "running")

    # === CONTENT LAYER: data konfigurasi (model YANG VLAN) ===
    config = ET.SubElement(edit, "config")
    vlans = ET.SubElement(config, "vlans", {"xmlns": NS_VLAN})
    vlan = ET.SubElement(vlans, "vlan")
    ET.SubElement(vlan, "vlan-id").text = str(vlan_id)
    cfg = ET.SubElement(vlan, "config")
    ET.SubElement(cfg, "vlan-id").text = str(vlan_id)
    ET.SubElement(cfg, "name").text = f"VLAN_{vlan_id}"

    ET.indent(rpc)  # Python 3.9+
    return ET.tostring(rpc, encoding="unicode")


if __name__ == "__main__":
    print(buat_pesan_netconf())
