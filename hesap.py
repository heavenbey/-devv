print(""" 

Hoşgeldiniz.
============================================
   
            [1] Toplama            
            [2] Çıkartma           
            [3] Çarpma	       
            [4] Üssünü Alma        
            [5] Bölme           

============================================
	""")

veri = input("İşlem :")

if veri =="1":
	x = input("========İşlem Yapacağınız İlk Sayıyı Giriniz.========:")
	x = float(x)
	y = input("========İşlem Yapacağınız İkinci Sayıyı Giriniz.========:")
	y = float(y)
	print("========Yaptığınız İşlemin Sonucu========:",x + y)

elif veri =="2":
	x = input("========İşlem Yapacağınız İlk Sayıyı Giriniz.========:")
	x = float(x)
	y = input("========İşlem Yapacağınız İkinci Sayıyı Giriniz.========:")
	y = float(y)
	print("========Yaptığınız İşlemin Sonucu========:",x - y)

elif veri == "3":
	x = input("========İşlem Yapacağınız İlk Sayıyı Giriniz.========:")
	x = float(x)
	y = input("========İşlem Yapacağınız İkinci Sayıyı Giriniz.========:")
	y = float(y)
	print("========Yaptığınız İşlemin Sonucu========:",x * y)

elif veri == "4":
	x = input("========İşlem Yapacağınız İlk Sayıyı Giriniz.========:")
	x = float(x)
	y = input ("========İşlem Yapacağınız İkinci Sayıyı Giriniz.========:")
	y = float(y)
	print("========Yaptığınız İşlemin Sonucu========:",x ** y) 

elif veri == "5":
    x = input("========İşlem Yapacağınız İlk Sayıyı Giriniz.========:") 
    x = float(x)
    y = input("========İşlem Yapacağınız İkinci Sayıyı Giriniz.========:")
    y = float(y)
    print("========Yaptığınız İşlemin Sonucu========:",x / y)


else:
	print("Yanlış Seçim :(")
	print("Program Kapanıyor.")
	quit()


    