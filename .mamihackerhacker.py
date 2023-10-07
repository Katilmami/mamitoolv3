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
4) Site admin panel bulucu
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
elif islemno=="4":
        os.system("clear")
        os.system("git clone https://github.com/C4ssif3r/admin-panel-finder")
        os.system("cd admin-panel-finder")
        os.system("cp -r admin-panel-finder $HOME/")
        os.system("clear")
        print("""
        Kuruldu açmak için komutlar:
        cd $HOME/admin-panel-finder
        sonra python admin-finder.py""")

elif islemno=="q" or islemno=="Q":
          quit()

else:
     quit()
