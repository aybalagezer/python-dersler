#küçük harf büyük harf hassasiyetiiçin .lower() yapıyoruz.İkisini de küçük harfe dönüştürür.#
#Döngüler#
#for in range komutu ile (aralık) range(başla,bitir,artış)#
#continue döngüyü başa sarar alt kısma inmez#
"""
tirsayisi=int(input("Tir sayisini giriniz:\n"))
for i in range(1,tirsayisi+1,1):
    print("{}. Tır".format(i))
"""
"""
isim=input("İsminizi Giriniz\n")
sayac=0
for i in isim:
    if(i==" "):
        sayac=sayac+1
print("Cümledeki Boşluk Sayısı:",sayac)
"""
"""
toplam=0
ortalama=0
for i in range(0,10,1):
    yas=input("Sıradaki Öğrencinin Yaşınızı Giriniz\n")
    toplam+=int(yas)
ortalama=toplam/10
print("Öğrencilerin ortalaması:",ortalama)
"""
#ekrana 9 sayısı girince çıktı 10 olur#
#sırayla 9 gir 81 20den büyük başa dön.5 e kadar devam et#
#4 gir tde 4'ü tut, 3 gir 4+3 t de 7 tut, 2 gir tde 9 tut, en son 1 t=10#
"""
t=0
s=int(input("Bir Sayi Giriniz:"))
for i in range(s,0,-1):
    if i**2>20:
        continue
    t+=i
print(t)
"""
#while sonsuz döngü true ile yap ya da koşul koy break yap durdur#
"""
a=1
sayac=0
while(a==1):
    sayac+=1
    print(a)
    if(sayac>20):
        break
    else:
        continue
"""
"""
sayac=0
while(True):
    sayac+=1
    print(sayac)
    if(sayac>20):
        break
    else:
        continue
"""