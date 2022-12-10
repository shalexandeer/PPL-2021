repeat = True;
jumlah = int(input("Masukkan Jumlah : "))
while(repeat):
    list1 = []
    
    for i in range(jumlah):
        nilaiKe = int(input("Masukkan Nilai : "))
        list1.append(nilaiKe)
    print(f'Hasil inputan: {list1} ')

    dicari = int(input("Masukkan data yang dicari: "))
    print(list1.index(dicari))
    


