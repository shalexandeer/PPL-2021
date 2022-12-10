baris = int(input("Masukkan baris : "))

for i in range(0,baris):
    for j in range(0,i+1):
        print("* ", end="")
    print("\r")

