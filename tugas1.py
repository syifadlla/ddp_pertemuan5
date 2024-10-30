#a. buat variable list dengan value:[nama kendaraan, jenis kendaraan, cckendaraan, warna kendaraan, roda kendaraan]
#b. tambahkan dibelakang dengan value[harga kendaraan, tipe kendaraan]
#c. setelah jenis kendaraan tambahkan dengan value [merk kendaraan]

#a 
list_kendaraan= ['honda beat', 'sepeda motor', 120, 'merah', 2]
print('Kendaraan saya:')
print(list_kendaraan)

#b
list_kendaraan.append(24500000)
list_kendaraan.append('matic')
list_kendaraan.extend([20000000, 'matic']) #cara cepat
print('Tambahannya:')
print(list_kendaraan)

#c
list_kendaraan.insert(2,'Honda')
print('Menyisipkan:') #shift+alt jika mau atur"
print(list_kendaraan)