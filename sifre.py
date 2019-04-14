import random

uzunluk = 15 #paroladak karakter sayısı

harfler = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
sayilar = '0123456789'
karakterler = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

while True:
    cevap_sayi = input('Parolanızda sayı olsun mu? [E/H]: ')
    if cevap_sayi != 'E' and cevap_sayi != 'H':
        print('Hatalı giriş - E veya H girin\n')
        continue

    while True:
        cevap_harf = input('Parolanızda harf olsun mu? [E/H]: ')
        if cevap_harf != 'E' and cevap_harf != 'H':
            print('Hatalı giriş - E veya H girin\n')
            continue
        break
    break
 

if cevap_sayi == 'E':
    liste = karakterler + sayilar
else:
    liste = karakterler

if cevap_harf == 'E':
    liste = liste + harfler

parola = ''

for c in range(uzunluk):
    parola += random.choice(liste)
    
print(parola)