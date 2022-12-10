namaMakanan_1, kodeMakanan_1,hargaMakanan_1,estimasiPembuatanMakanan_1, diskonMakanan_1 =	"KupatTahu", 11001, 15000.0, 15 ,2.0
namaMakanan_2, kodeMakanan_2,hargaMakanan_2,estimasiPembuatanMakanan_2, diskonMakanan_2 =	"GadoGado", 11005, 15000.0, 8 ,1.0
namaMinuman_3, kodeMinuman_3,hargaMinuman_3,estimasiPembuatanMinuman_3, diskonMinuman_3 =	"EsTehManis", 12001, 5000.0, 3 ,0.0

repeat = True
list_menu,waktuPesanan = [] , []
import datetime
import math
import pytz
from datetime import datetime,timedelta
while(repeat):
    try:
        pemesanan_makanan = int(input())
        if pemesanan_makanan == kodeMakanan_1:
            jmlh_pesanan = int(input())
            inputUlang = input("Apakah anda ingin menambah pesanan lagi?(y/n)")
            if(jmlh_pesanan > 5 and str(kodeMakanan_1)[:2] == "11"):
                waktuPesanan.append(estimasiPembuatanMakanan_1 + (jmlh_pesanan * 0.5))
                list_menu.append(f'{namaMakanan_1} | {jmlh_pesanan} | {math.floor(estimasiPembuatanMakanan_1 + (jmlh_pesanan * 0.5))} |')
            else: 
                waktuPesanan.append(estimasiPembuatanMakanan_1) 
                list_menu.append(f'{namaMakanan_1} | {jmlh_pesanan} | {math.floor(estimasiPembuatanMakanan_1)} |')
            if inputUlang == "y": repeat = True 
            else: repeat = False
        elif pemesanan_makanan == kodeMakanan_2:
            jmlh_pesanan = int(input())
            inputUlang = input("Apakah anda ingin menambah pesanan lagi?(y/n)")
            if(jmlh_pesanan > 5 and str(kodeMakanan_1)[:2] == "11"):
                waktuPesanan.append(estimasiPembuatanMakanan_2 + (jmlh_pesanan * 0.5))
                list_menu.append(f'{namaMakanan_2} | {jmlh_pesanan} | {math.floor(estimasiPembuatanMakanan_2 + (jmlh_pesanan * 0.5))} |')
            else: 
                waktuPesanan.append(estimasiPembuatanMakanan_2) 
                list_menu.append(f'{namaMakanan_2} | {jmlh_pesanan} | {math.floor(estimasiPembuatanMakanan_2)} |')
            if inputUlang == "y": repeat = True 
            else: repeat = False
        elif pemesanan_makanan == kodeMinuman_3:
            jmlh_pesanan = int(input())
            inputUlang = input("Apakah anda ingin menambah pesanan lagi?(y/n)")
            if(jmlh_pesanan > 5 and str(kodeMakanan_1)[:2] == "11"):
                waktuPesanan.append(estimasiPembuatanMinuman_3 + (jmlh_pesanan * 0.5))
                list_menu.append(f'{namaMinuman_3} | {jmlh_pesanan} | {math.floor(estimasiPembuatanMinuman_3 + (jmlh_pesanan * 0.5))} |')
            else: 
                waktuPesanan.append(estimasiPembuatanMinuman_3) 
                list_menu.append(f'{namaMinuman_3} | {jmlh_pesanan} | {math.floor(estimasiPembuatanMinuman_3)} |')
            if inputUlang == "y": repeat = True 
            else: repeat = False
        else:
            print("Mohon maaf, menu belum tersedia")
    except ValueError:
            print("Mohon maaf, menu belum tersedia")
else:
    print('\n=======================================\nNama Menu | Jml | Estimasi Waktu |')
    for i in range(len(list_menu)):
        print(list_menu[i])
    print('=======================================')
    new_time = (datetime.now(pytz.timezone("Asia/Jakarta")) + timedelta(minutes=sum(waktuPesanan))).strftime('%H:%M')
    print(f'Pesanan anda diperkirakan selesai pukul  {new_time}')
    






    

