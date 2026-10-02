# UTS Jaringan Komputer Lanjut - Integration Network with Python

Nama : mfahrianor
NIM  : 2409106089
Kelas B 2024 - Program Studi Informatika

## Struktur Project
```
.
├── identitas.py        # Identitas cabang + buat_id_perangkat()
├── ssh_modul.py        # cek_ssh()  - SSH/Paramiko
├── snmp_modul.py       # cek_snmp() - SNMPv2c/PySNMP (sysName)
├── netconf_modul.py    # buat_pesan_netconf() - XML <rpc><edit-config> VLAN
├── telemetry_modul.py  # klasifikasi_telemetry() - cpuUsage KRITIS/WASPADA/NORMAL
├── main.py             # Integrasi + class LaporanCabang
├── requirements.txt
├── .gitignore
└── README.md
```

## Cara Menjalankan
```bash
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Kredensial & alamat target dibaca dari environment variable (tidak disimpan di kode)
export SSH_HOST=<ip-vm>
export SNMP_HOST=<ip-vm>
export SSH_PASSWORD='<password-user-ssh>'

python3 main.py
```
Jika SSH/SNMP gagal (target mati/salah kredensial), program tetap berjalan
dan statusnya ditampilkan sebagai GAGAL di laporan akhir.

## Ringkasan Personalisasi
- Kode cabang  : 3 digit terakhir NIM (`nim[-3:]`)
- Username SSH : `admin_<kode_cabang>`
- SNMP         : SNMPv2c, community `comm_<kode_cabang>`, OID sysName `1.3.6.1.2.1.1.5.0`
- NETCONF      : VLAN ID = angka dari kode_cabang (`int(kode_cabang)`)
- Telemetry    : 4 sampel cpuUsage dari pasangan digit NIM, dibaca dari belakang
  (2 digit terakhir, 2 digit sebelumnya, dst.)
  - di atas 80 = KRITIS, 50-80 = WASPADA, di bawah 50 = NORMAL
