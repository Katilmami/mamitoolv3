#!/usr/bin/env python3

import os

os.system("clear")
os.system("clear")
os.system("figlet MAMI")
print("""
İslemler

1) Bot Oluştur
2) Botu Dahili Depolamaya Tasi
3) Ana Menüye dön
Q) Cıkış

""")

islemno =input("İslem numarasini giriniz: ")

if islemno=="1":
        os.system("clear")
        os.system("git clone https://github.com/EmirhanSarac/discord-altyapi-bot")
        os.system("clear") 
        print("Bot Yapma İslemi Bitmistir cd discord-altyapi-bot Yazma-niz Yeterlidir")
elif islemno=="2":
          os.system("clear")
          os.system("mv -v discord-altyapi-bot /sdcard")
          os.system("clear")
          print("Botunuz Dahili Depolamaya Tasindi discord-altyapi-bot İsmindeki Klasore Girerek Botun Dosyalarina Ulasabilirsiniz")
elif islemno=="3":
        os.system("clear")
        os.system("python mamihacker.py")
elif islemno=="q" or islemno=="Q":
          quit()

else:
     quit()
