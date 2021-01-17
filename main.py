import random
import time
print("""******************
Sayı Tahmin Oyunu
******************""")
rasgele_sayi = random.randint(1,40)
tahmin_hakki = 5
while True:
    tahmin = int(input("Tahmininiz:"))
    if(tahmin<rasgele_sayi):
        print("Sorgulanıyor...")
        time.sleep(1)
        print("Daha büyük bir sayı giriniz")
        tahmin_hakki -=1
    elif(tahmin>rasgele_sayi):
        print("Sorgulanıyor...")
        time.sleep(1)
        print("Daha küçük bir sayı giriniz.")
        tahmin_hakki -=1
    else:
        print("Sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler sayiyi buldunuz : ",rasgele_sayi)
        break
    if(tahmin_hakki == 0):
        print("Tahmin hakkınız bitti.")
        print("Sayımız = ",rasgele_sayi)
        break
