pengkali = int(input("Masukkan maskimal pengkali : "))
pengkali +=  1
for i in range(1,pengkali):
    for j in range(1,pengkali):
        print(f'{i} * {j} = {i*j}')