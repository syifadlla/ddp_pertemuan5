#match case menghitung luas bangun datar

input_angka= int(input('Pilih angka 1-3 untuk mengetahui luas bangun datar:\n 1. Luas Persegi\n 2. Luas Lingkaran\n 3. Luas Segitiga\n Masukkan angka:'))

match input_angka:
    case 1:
        print('Ini adalah Operasi Luas Persegi')
        sisi= int(input('Masukkan angka untuk dihitung:'))
        luas_persegi= sisi*sisi
        print(f'Luas persegi =', sisi,"cm *", sisi, "cm =", luas_persegi,'cm2')

    case 2:
        print('Ini adalah Operasi Luas Lingkaran')
        jari_jari= int(input('Masukkan jari-jari yang kelipatan 7 untuk dihitung:'))
        𝝅=22/7
        luas_lingkaran=int(𝝅*jari_jari*jari_jari)
        print(f'Luas lingkaran = 𝝅 *', jari_jari,"cm *", jari_jari, "cm =", luas_lingkaran, 'cm2')        
    case 3: 
        print('Ini adalah Operasi Luas Segitiga')
        alas= int(input('Masukkan alas:'))
        tinggi= int(input('Masukkan tinggi:'))

        luas_segitiga= int(1/2*alas*tinggi)
        print(f'Luas segitiga = 1/2 *', alas,"cm *", tinggi, "cm =", luas_segitiga, 'cm2')    
        
    case _:
        print('salah pilih')

