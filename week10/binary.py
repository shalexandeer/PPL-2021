a = [27,36,21,7,4]
def cari(a,key):
    awal = 0
    akhir = len(a)

    for i in range(awal, akhir):
        tengah = int((awal+akhir)/2)
        if(key == a[tengah]):
            print("data ditemukan pada indeks ke ", tengah)
            break
        elif(key < a[tengah]):
            akhir = tengah-1
        else: 
            awal = tengah + 1
a.sort()
print(a)
cari(a,36)