#!/usr/bin/env python3

import os

os.system("clear")
os.system("clear")
os.system("figlet MAMI")
print("""
İslemler

1) Word List Oluştur
2) zphisher Kur
3) Ana Menüye dön
Q) Cıkış

""")

islemno =input("İslem numarasini giriniz: ")
if islemno=="1":
        os.system("clear")
        os.system("python3 .Mamiworldlist.py -i ")
elif islemno=="2":
        os.system("clear")
        os.system("git clone https://github.com/htr-tech/zphisher")
        os.system("clear")
        print("zphisher kurulumu bitti cd $HOME/zphisher yazarak ulaşabilirsiniz")
        os.system("mv -v zphisher $HOME/ ")
elif islemno=="3":
        os.system("clear")
        os.system("python mamihacker.py")
elif islemno=="q" or islemno=="Q":
          quit()

else:
     quit()
