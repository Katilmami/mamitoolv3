#!/usr/bin/env python3

import os

os.system("clear")
os.system("clear")
os.system("figlet MAMI")
print("""
İslemler

1) Site İslemleri
2) Hacker İslemleri
3) discord bot islemleri
4) Toolu Güncelle
Q) Cıkış

""")

islemno =input("İslem numarasini giriniz: ")

if islemno=="1":
        os.system("clear")
        os.system("python3 .mamihackersite.py")
elif islemno=="2":
          os.system("clear")
          os.system("python3 .mamihackerhacker.py")
elif islemno=="4":
          os.system("clear")
          os.system("python3 .updater.py")
elif islemno=="3":
          os.system("clear")
          os.system("python3 .botekrani.py")
elif islemno=="q" or islemno=="Q":
          quit()

else:
     quit()
