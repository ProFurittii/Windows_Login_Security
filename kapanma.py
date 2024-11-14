
import os
import time
import sys

# Masaüstü yolunu alalım (Windows için)
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Klasör adı
folder_name = "ben buradayım"
folder_path = os.path.join(desktop_path, folder_name)

# Çıktıyı engellemek için sys.stdout'u null yapalım
sys.stdout = open(os.devnull, 'w')

# 30 saniye boyunca klasörün var olup olmadığını kontrol et
start_time = time.time()
while time.time() - start_time < 30:
    if os.path.exists(folder_path):
        # Klasör bulunduğunda çıktı ver
        sys.stdout = sys.__stdout__  # Çıktıyı geri açıyoruz
        print("Klasör bulundu, bilgisayar kapanmayacak.")  # Klasör bulunduğunda mesaj
        break  # Klasör bulundu, çık
    time.sleep(1)  # Her saniye klasörün olup olmadığını kontrol et

else:
    # Klasör bulunamadı, bilgisayar kapanacak
    time.sleep(3)  # 3 saniye bekleme
    os.system("shutdown /s /f /t 0")  # Windows kapanma komutu
