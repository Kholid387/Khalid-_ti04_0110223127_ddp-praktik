# -*- coding: utf-8 -*-
"""M.Khalid Shafwan

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KTy_QlBqDw7TJuCBcHrDAek1xBtl9OnQ
"""

print('Nomor 1')
kendaraan=['zx25r','motor''249.8','pink','2']
print(kendaraan)
kendaraan.append('125.700.000')
kendaraan.append('manual')
print(kendaraan)
kendaraan.insert(2,'Kawasaki Ninja')
print(kendaraan)

print('Nomor 2')
kuun = input('masukkan sesuai angka')
match kuun:
  case '1' :
        sisi = int(input('masukkan sisi ;'))
        persegi = sisi * sisi
        print('hasil dari  persegi :', persegi)
  case '2':
        v=22/7
        r=int(input('masukan jari-jari ;'))
        luas= v *r*r
        print('hasil luas lingkaran :' ,luas)
  case '3' :
        a=int(input('masukan alas :'))
        t=int(input('masukan tinggi :'))
        luassegi= a*t/2
        print('hasil luas segitiga :',luassegi)
  case _:
        print('masukan sesual')

print('output 3')
a= int(input())
if a % 2== 0:print('bilangan genap')
else: print('bilangan ganjil')