##########################
#   Bjir Ngapain Bang    #
##########################

"""
Pointdns
Via Sekrip Piton3
By Kgyya
"""

"""
Ketik: git pull
"""

GR = '\x1b[90m'
R = '\x1b[91m'
G = '\x1b[92m'
Y = '\x1b[93m'
B = '\x1b[94m'
P = '\x1b[95m'
C = '\x1b[96m'
W = '\x1b[37m'
FL = '\x1b[47;30m'
O = '\x1b[m'
BO = '\033[1m'

import os
import requests as req

def pointdns_pw():
 try:
  host = input("NAMA SUBDOMAIN: ")
  ip = input("IP: ")
  ses = req.Session()
  url = "https://www.pointdns.net/create-dns"
  data = { "hostname":host,
          "ipaddress":ip,
          "domain":"pointdns.pw",
          "submit":"Create"
         }
  post = ses.post(url, data=data).text
  if "success" in post:
   print(f"""{BO}
{P}==================================
{G}DNS BERHASIL DIBUAT

{G}DOMAIN        : {B}{host}.pointdns.pw
{G}TERPOINTING KE: {B}{ip}
{G}STATUS        : {B}SUKSES TERPOINTING
{P}==================================
JOIN US       : t.me/tempatconfig
              : t.me/bebas_berinternet
{P}==================================
{R}NOTE!

{W}RESET SETIAP JUM'AT & SABTU
JADI JIKA DNS KAMU SUKSES TERBUAT
TAPI TIDAK TERJADI APA²
SILAHKAN BUAT LAGI PADA HARI JUMAT
ATAU SABTU...
{P}==================================
{R}ATAU!

{W}NAMA DNS KAMU SUDAH DIPAKAI
ORANG LAIN...
{P}=================================={O}
""")
  else:
   print(f"""{BO}
{P}==================================
{R}DNS GAGAL DIBUAT
{P}==================================
{W}SILAHKAN KEMBALI LAGI PADA HARI RESET
YAITU HARI JUM'AT & SABTU...
{P}==================================
{R}ATAU!

{W}NAMA DNS KAMU SUDAH DIPAKAI
ORANG LAIN...
{P}==================================
""")
 except requests.exceptions.ConnectionError:
  print(f"""{BO}
{P}==================================
{R}GAGAL, TIDAK ADA KONEKSI INTERNET..
{P}==================================
""")

def pointdns_pro():
 try:
  host = input("NAMA SUBDOMAIN: ")
  ip = input("IP: ")
  ses = req.Session()
  url = "https://www.pointdns.net/create-dns"
  data = { "hostname":host,
          "ipaddress":ip,
          "domain":"pointdns.pro",
          "submit":"Create"
         }
  post = ses.post(url, data=data).text
  if "success" in post:
   print(f"""{BO}
{P}==================================
{G}DNS BERHASIL DIBUAT

{G}DOMAIN        : {B}{host}.pointdns.pro
{G}TERPOINTING KE: {B}{ip}
{G}STATUS        : {B}SUKSES TERPOINTING
{P}==================================
JOIN US       : t.me/tempatconfig
              : t.me/bebas_berinternet
{P}==================================
{R}NOTE!

{W}RESET SETIAP JUM'AT & SABTU
JADI JIKA DNS KAMU SUKSES TERBUAT
TAPI TIDAK TERJADI APA²
SILAHKAN BUAT LAGI PADA HARI JUMAT
ATAU SABTU...
{P}==================================
{R}ATAU!

{W}NAMA DNS KAMU SUDAH DIPAKAI
ORANG LAIN...
{P}=================================={O}
""")
  else:
   print(f"""{BO}
{P}==================================
{R}DNS GAGAL DIBUAT
{P}==================================
{W}SILAHKAN KEMBALI LAGI PADA HARI RESET
YAITU HARI JUM'AT & SABTU...
{P}==================================
{R}ATAU!

{W}NAMA DNS KAMU SUDAH DIPAKAI
ORANG LAIN...
{P}==================================
""")
 except requests.exceptions.ConnectionError:
  print(f"""{BO}
{P}==================================
{R}GAGAL, TIDAK ADA KONEKSI INTERNET..
{P}==================================
""")

def pointdns_club():
 try:
  host = input("NAMA SUBDOMAIN: ")
  ip = input("IP: ")
  ses = req.Session()
  url = "https://www.pointdns.net/create-dns"
  data = { "hostname":host,
          "ipaddress":ip,
          "domain":"pointdns.club",
          "submit":"Create"
         }
  post = ses.post(url, data=data).text
  if "success" in post:
   print(f"""{BO}
{P}==================================
{G}DNS BERHASIL DIBUAT

{G}DOMAIN        : {B}{host}.pointdns.club
{G}TERPOINTING KE: {B}{ip}
{G}STATUS        : {B}SUKSES TERPOINTING
{P}==================================
JOIN US       : t.me/tempatconfig
              : t.me/bebas_berinternet
{P}==================================
{R}NOTE!

{W}RESET SETIAP JUM'AT & SABTU
JADI JIKA DNS KAMU SUKSES TERBUAT
TAPI TIDAK TERJADI APA²
SILAHKAN BUAT LAGI PADA HARI JUMAT
ATAU SABTU...
{P}==================================
{R}ATAU!

{W}NAMA DNS KAMU SUDAH DIPAKAI
ORANG LAIN...
{P}=================================={O}
""")
  else:
   print(f"""{BO}
{P}==================================
{R}DNS GAGAL DIBUAT
{P}==================================
{W}SILAHKAN KEMBALI LAGI PADA HARI RESET
YAITU HARI JUM'AT & SABTU...
{P}==================================
{R}ATAU!

{W}NAMA DNS KAMU SUDAH DIPAKAI
ORANG LAIN...
{P}==================================
""")
 except requests.exceptions.ConnectionError:
  print(f"""{BO}
{P}==================================
{R}GAGAL, TIDAK ADA KONEKSI INTERNET..
{P}==================================
""")

def pointdns_xyz():
 try:
  host = input("NAMA SUBDOMAIN: ")
  ip = input("IP: ")
  ses = req.Session()
  url = "https://www.pointdns.net/create-dns"
  data = { "hostname":host,
          "ipaddress":ip,
          "domain":"pointdns.xyz",
          "submit":"Create"
         }
  post = ses.post(url, data=data).text
  if "success" in post:
   print(f"""{BO}
{P}==================================
{G}DNS BERHASIL DIBUAT

{G}DOMAIN        : {B}{host}.pointdns.xyz
{G}TERPOINTING KE: {B}{ip}
{G}STATUS        : {B}SUKSES TERPOINTING
{P}==================================
JOIN US       : t.me/tempatconfig
              : t.me/bebas_berinternet
{P}==================================
{R}NOTE!

{W}RESET SETIAP JUM'AT & SABTU
JADI JIKA DNS KAMU SUKSES TERBUAT
TAPI TIDAK TERJADI APA²
SILAHKAN BUAT LAGI PADA HARI JUMAT
ATAU SABTU...
{P}==================================
{R}ATAU!

{W}NAMA DNS KAMU SUDAH DIPAKAI
ORANG LAIN...
{P}=================================={O}
""")
  else:
   print(f"""{BO}
{P}==================================
{R}DNS GAGAL DIBUAT
{P}==================================
{W}SILAHKAN KEMBALI LAGI PADA HARI RESET
YAITU HARI JUM'AT & SABTU...
{P}==================================
{R}ATAU!

{W}NAMA DNS KAMU SUDAH DIPAKAI
ORANG LAIN...
{P}==================================
""")
 except requests.exceptions.ConnectionError:
  print(f"""{BO}
{P}==================================
{R}GAGAL, TIDAK ADA KONEKSI INTERNET..
{P}==================================
""")

def pointdns2_xyz():
 try:
  host = input("NAMA SUBDOMAIN: ")
  ip = input("IP: ")
  ses = req.Session()
  url = "https://www.pointdns.net/create-dns"
  data = { "hostname":host,
          "ipaddress":ip,
          "domain":"pointdns2.xyz",
          "submit":"Create"
         }
  post = ses.post(url, data=data).text
  if "success" in post:
   print(f"""{BO}
{P}==================================
{G}DNS BERHASIL DIBUAT

{G}DOMAIN        : {B}{host}.pointdns2.xyz
{G}TERPOINTING KE: {B}{ip}
{G}STATUS        : {B}SUKSES TERPOINTING
{P}==================================
JOIN US       : t.me/tempatconfig
              : t.me/bebas_berinternet
{P}==================================
{R}NOTE!

{W}RESET SETIAP JUM'AT & SABTU
JADI JIKA DNS KAMU SUKSES TERBUAT
TAPI TIDAK TERJADI APA²
SILAHKAN BUAT LAGI PADA HARI JUMAT
ATAU SABTU...
{P}==================================
{R}ATAU!

{W}NAMA DNS KAMU SUDAH DIPAKAI
ORANG LAIN...
{P}=================================={O}
""")
  else:
   print(f"""{BO}
{P}==================================
{R}DNS GAGAL DIBUAT
{P}==================================
{W}SILAHKAN KEMBALI LAGI PADA HARI RESET
YAITU HARI JUM'AT & SABTU...
{P}==================================
{R}ATAU!

{W}NAMA DNS KAMU SUDAH DIPAKAI
ORANG LAIN...
{P}==================================
""")
 except requests.exceptions.ConnectionError:
  print(f"""{BO}
{P}==================================
{R}GAGAL, TIDAK ADA KONEKSI INTERNET..
{P}==================================
""")

def pointdns3_xyz():
 try:
  host = input("NAMA SUBDOMAIN: ")
  ip = input("IP: ")
  ses = req.Session()
  url = "https://www.pointdns.net/create-dns"
  data = { "hostname":host,
          "ipaddress":ip,
          "domain":"pointdns3.xyz",
          "submit":"Create"
         }
  post = ses.post(url, data=data).text
  if "success" in post:
   print(f"""{BO}
{P}==================================
{G}DNS BERHASIL DIBUAT

{G}DOMAIN        : {B}{host}.pointdns.pw
{G}TERPOINTING KE: {B}{ip}
{G}STATUS        : {B}SUKSES TERPOINTING
{P}==================================
JOIN US       : t.me/tempatconfig
              : t.me/bebas_berinternet
{P}==================================
{R}NOTE!

{W}RESET SETIAP JUM'AT & SABTU
JADI JIKA DNS KAMU SUKSES TERBUAT
TAPI TIDAK TERJADI APA²
SILAHKAN BUAT LAGI PADA HARI JUMAT
ATAU SABTU...
{P}==================================
{R}ATAU!

{W}NAMA DNS KAMU SUDAH DIPAKAI
ORANG LAIN...
{P}=================================={O}
""")
  else:
   print(f"""{BO}
{P}==================================
{R}DNS GAGAL DIBUAT
{P}==================================
{W}SILAHKAN KEMBALI LAGI PADA HARI RESET
YAITU HARI JUM'AT & SABTU...
{P}==================================
{R}ATAU!

{W}NAMA DNS KAMU SUDAH DIPAKAI
ORANG LAIN...
{P}==================================
""")
 except requests.exceptions.ConnectionError:
  print(f"""{BO}
{P}==================================
{R}GAGAL, TIDAK ADA KONEKSI INTERNET..
{P}==================================
""")

def main():
 os.system("clear")
 print(f"""{BO}
{P}==================================
{G}CREATE SUBDOMAIN POINTDNS
{G}PYTHON 3.xx
{G}By Kgyya
{P}==================================
{G}PILIH DOMAIN:
{P}==================================
{B}1) POINTDNS.PW
{B}2) POINTDNS.PRO
{B}3) POINTDNS.CLUB
{B}4) POINTDNS.XYZ
{B}5) POINTDNS2.XYZ
{B}6) POINTDNS3.XYZ
{P}==================================
""")
 sub = input("PILIH NOMOR: ")
 if sub == "1":
  pointdns_pw()
 elif sub == "2":
  pointdns_pro()
 elif sub == "3":
  pointdns_club()
 elif sub == "4":
  pointdns_xyz()
 elif sub == "5":
  pointdns2_xyz()
 elif sub == "6":
  pointdns3_xyz()
 else:
  print("INPUT SALAH")

if __name__ == "__main__":
 main()

