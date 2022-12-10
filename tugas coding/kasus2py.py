karakter = input('Masukkan huruf: ')
angka = input('Masukkan angka: ')
array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
try:
    for x in array:
        if(karakter.lower() == x):print(array[array.index(x) + int(angka)]) 
except ValueError: print(angka)
