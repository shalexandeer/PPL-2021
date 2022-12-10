p1 = input()
p2 = input()

# array = ['gunting','kertas','batu']

# print(p1[0:2])

if(p1 == p2):
    print('pertandingan seri')
elif(p1 == 'gunting' and p2 == 'kertas'):
    print('gunting menang')
elif(p1 == 'kertas' and p2 == 'gunting'):
    print('gunting menang')
elif(p1 == 'batu' and p2 == 'gunting'):
    print('batu menang')
elif(p1 == 'gunting' and p2 == 'batu'):
    print('batu menang')
elif(p1 == 'batu' and p2 == 'kertas'):
    print('kertas menang')
elif(p1 == 'kertas' and p2 == 'batu'):
    print('kertas menang')


