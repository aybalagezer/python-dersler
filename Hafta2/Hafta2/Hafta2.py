#sayilar uzerinde islemler#

sayi1=2
sayi2=3
sayi3=sayi1+sayi2
print("Toplam: ", sayi3)

""" 
print(sayi1,sayi2)
import math as matematics
#print(dir(math))
print(help(matematics))
karekok=int(input("Karakökü alınacak sayiyi gir\n"))
sayi5=matematics.sqrt(karekok)
print(sayi5) 
"""
"""
#if elif else sonlarına : koy suslu parantez yok#
yas=int(input("Yasinizi giriniz\n"))
if(yas>0 and yas<=3):
    print("Yasiniz bebek yas araligindadir")
    print("Suanki yasiniz",yas,"dir")
elif(yas>4 and yas<=10):
    print("Yasiniz cocuk yas araligindadir")
    print("Suanki yasiniz",yas,"dir")   
elif(yas>=11 and yas<=18):
    print("Yasiniz genc yas araligindadir")
    print("Suanki yasiniz",yas,"dir")
else:
    print("Yasiniz yas aralıgımızı uymuyor\n")
"""    
#online bir alışveriş sitesine kayıt için kullanıcı adı ve parola belirlenmesini isteyen bir program yazıyorsunuz.
# Yazacağınız bu programda, belirlenebilecek kullanıcı adı ve parolanın uzunluğu 40 karakteri geçmeyecek.
# süslü parantezle formatla ÇIKTIYI DEĞİŞKENE ATAMAYI UNUTMA#
kullaniciadi=input("Kullanıcı adınızı girin\n")
parola=input("Parolanizi giriniz\n")
toplam=len(kullaniciadi)+len(parola)
if(toplam<=40):
    yazi="karakter uzunluğu {} kadardir."
    yazi=yazi.format(toplam)
    print(yazi,"Gecerlidir\n")
else:
    print("Gecersizdir\n")
    
