#listeler ve demetler (list) (tuple)
#manipülasyonu engellemek için demet kullan
"""
liste=["öge1","öge2","öge3",1,2,3]
print(type(liste))
"""
"""
liste=["Ahmet","Mehmet",12,34,3,4]
print(liste) 
print(type(liste))
for i in liste: 
    print("{} elamanın veri tipi {} dir.".format(i,type(i)))
"""
"""
range ile üsttekini yapma   
for i in range(len(liste)):  
    print("{} elamanın veri tipi {} dir.".format(liste[i]))) 
"""
"""
DersAdi="Algoritma ve Programlama Dersi" 
veri=DersAdi.split()
print(veri)
print(veri[0]) ilk veriyi çıktılayacak Algoritma 
print(type(veri[0])) ilk verinin tipini yazdırıcak str
uzunluk=len(veri[0]) algoritma kelimesinde kaç kelime olduğu bulur yazdırır 9
orta=int(uzunluk/2)  4 bulur yani 5. harfi çağıracağız
print(orta)
print(veri[0][orta])  çıktı=r
"""
#SORU kullanıcının girdiği sayıları listeye al ortalamasını bul
"""
liste=[]
for i in range(4):
    sayi=int(input("Bir Sayi Giriniz\n"))   
    liste+=[sayi] 

toplam=0  
for i in liste: 
    toplam+=int(i) 
ortalama=toplam/4 
print(ortalama) 
"""
#del liste[silmek istediğimiz eleman] elaman çıkarır
