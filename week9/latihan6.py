def sort(data):
    n = len(data)
    for i in range(n):
        mins = i
        for j in range(i+1,n):
            if data[mins] > data[j]:
                mins = j
        data[i], data[mins] = data[mins], data[i]

data = [ 8,5,28,12,1,7]
sort(data)
print(data)

# intersection sort
def sort(ar):
    for i in range(1, len(ar)):
        while ar[i-1] > ar[i] and i > 0:
            ar[i-1], ar[i] = ar[i], ar[i-1]
            i -= 1

data = [8,5,23,12,1,7]
print(sort(data))