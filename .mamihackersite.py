#!/usr/bin/env python3

import os

os.system("clear")
os.system("clear")
os.system("figlet MAMI")
print("""
İslemler

1) Site Site Hakkında Genel Bilgi
2) Site Hızlı Port Taraması
3) Site Versiyon bilgisi
4) ana menüye dön
Q) Cıkış

""")

islemno =input("İslem numarasini giriniz: ")

if islemno=="1":
        hedefip= input("Hedef Site Giriniz: ")
        os.system("whois "+hedefip)
elif islemno=="2":
          hedefip= input("Hedef Site Giriniz: ")
          os.system("nmap "+hedefip)
elif islemno=="3":
          hedefip= input("Hedef Site Giriniz: ")
          os.system("nmap -sV "+hedefip)
elif islemno=="4":
        os.system("clear")
        os.system("python mamihacker.py")
elif islemno=="q" or islemno=="Q":
          quit()

else:
     quit()
