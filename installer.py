#!/usr/bin/env python3


import os



os.system("pkg install nodejs -y")
os.system("pkg install nodejs-lts -y")
os.system("pkg install nmap -y")
os.system("pkg install whois")
os.system("pkg install figlet")
os.system("pkg install git -y")
os.system("clear")
os.system("wget https://raw.githubusercontent.com/Katilmami/mamitoolmamicommand/main/mami")
os.system("mv mami /data/data/com.termux/files/usr/bin")
os.system("chmod +x /data/data/com.termux/files/usr/bin/mami")
print("KURULUM BİTTİ")
os.system("python mamihacker.py")