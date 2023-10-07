#!/usr/bin/env python3

import os

os.system("clear")
os.system("clear")
os.system("figlet MAMI")
print("""
İslemler

1) Güncellemeyi indir (Not Klasörün içine yeni güncelleme dosyasını indirir)
2) ana menüye dön
Q) Cıkış

""")

islemno =input("İslem numarasini giriniz: ")
if islemno=="1":
        os.system("clear")
        os.system("git clone https://github.com/Katilmami/mamitoolv3")
        os.system("clear")
        os.system("figlet mami")
        os.system("cd mamitoolv3")
        os.system("pwd")
        print("Güncelleme Kuruldu")
elif islemno=="2":
        os.system("clear")
        os.system("python mamihacker.py")
elif islemno=="q" or islemno=="Q":
          quit()

else:
     quit()
     