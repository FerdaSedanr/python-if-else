# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 16:05:41 2022

@author: User
"""
# if else kullanım örnekleri

#kullanıcı giriş kontrolü
print("******HOŞGELDİNİZ******")
kullanıcı="admin"
sifre=12345
kullanıcı1=input("Kullanıcı Adınızı Girin: ")
sifre1=int(input("Şifrenizi Girin: "))
if(kullanıcı==kullanıcı1 and sifre==sifre1):
    print("***Kullanıcı adı ve şifre doğru.\n***")
else:
    print("***Kullanıcı adı veya şifre yanlış!***")
#%%
#Girilen 3 sayıdan en büyüğünü bulma
print("İstenilen sırayla sayıları giriniz...")
x=int(input("Birinci Sayıyı Giriniz: "))
y=int(input("İkinci Sayıyı Giriniz: "))
z=int(input("Üçüncü Sayıyı Giriniz: "))
if(x>y and y>z):
    print("En büyük sayı {}".format(x))
elif(y>x and y>z):
    print("En büyük sayı {}".format(y))
else:
    print("En büyük sayı {}".format(z))
#%%
#kullanıcıdan vize %40 final%6o notunu alıp geçti kaldı yazdıralım
#final notu 50 den yukarı olmalı yoksa direkt kalır
#final notu 80 den yukarı direk geçer
vize=int(input("Vize notunuzu girin: "))
final=int(input("Final notunuzu girin: "))
def orthesapla(vize,final):
    global ort
    ort=(0.4*vize)+(0.6*final)
    return ort

if(final>=50):
    orthesapla(vize, final)
    if(final>=80):
        print("Final notunuz 80 ve üstü geçtiniz ortalamanız: {}".format(ort))
    elif((final>40 and final<80) and ort>50):
        print("{} ortalama ile geçtiniz tebrikler!!!".format(ort))
    elif(ort<50):
        print("{} ortalama ile kaldınız...".format(ort))
elif(final>=80):
      print("Final notunuz 80 ve üstü olduğu için geçtiniz.")
else:
      
     print("Final notunuz 50'nin altında olduğu için kaldınız...")
#%%
#boy kilo girdilerini kullanarak vücut kitle endeksi hesaplama 
#formül= kilo/(boy*boy)
print("****HOŞGELDİNİZ****\n")
print("İstenilen verileri girin ve vücut kitle endeksiniz hesaplansın\n")
kilo=float(input("Kilonuzu Girin: "))
boy=float (input("Boyunuzu (metre cinsinden girin!) Girin: "))
def endeks(kilo,boy):
     global islem
     islem= kilo/(boy*boy)
     return islem
endeks(kilo,boy)
if(islem<18.4):
    print("Zayıf Kategorisindesiniz")
elif(islem>18.4 and islem<24.9):
        print("Normal Kategorisindesiniz")
elif(islem>24.9 and islem<29.9 ):
            print("Kilolu kategorisindesiniz diyetisyene başvurun...")
else:
            print("Obez kategorisindesiniz hastaneye başvurun!!!")




































