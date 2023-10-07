
import requests
import random
import string
import os


os.system("clear")
print("")
print("")
print("")
os.system("figlet MAMI")
print("")
print("")
print("")
print("")
print("")
print("")

# Kullanıcıdan kaç kez deneme yapmak istediğini alın
iteration_count = int(input("Kaç kez deneme yapmak istersiniz? "))

found_valid_code = False  # Geçerli bir kod bulunup bulunmadığını izlemek için bir bayrak

for _ in range(iteration_count):
    # Rastgele Nitro kodu oluştur
    nitro_code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    print("Rastgele Discord Nitro Kodu:", nitro_code)

    # Discord API'ye istek gönderme
    api_url = f"https://discord.com/api/v10/entitlements/gift-codes/{nitro_code}"
    response = requests.get(api_url)

    if response.status_code == 200:
        print("Bu Nitro kodu geçerli.")
        found_valid_code = True  # Geçerli kod bulunduğunda bayrağı işaretle
        break  # Geçerli bir kod bulunduğunda döngüyü durdur
    else:
        print("Bu Nitro kodu geçersiz.")

if found_valid_code:
    print("Geçerli bir Nitro kodu bulundu.")
else:
    print("Geçerli bir Nitro kodu bulunamadı.")
