#list loker
loker = []
for i in range (0,101):
    if (i == 0):
        loker += [0]
    else:
        loker += [0]

#aksi
def aksi (n):
    loker_= []
    for i in range(0,(len(loker))):
        if (i != 0):
            if (i % n == 0):
                if (int(loker[i]) == 1):
                    loker[i] = 0
                else:
                    loker[i] = 1
        loker_ += [loker[i]]
    loker_ = loker
    return loker

#perulangan aksi
for i in range (1,101):
    a = aksi(i)
    if (i == 100):
        b = 0
        for j in a:
            b += j
tertutup = (len(a)-1) - b

print("Pintu yang tertutup adalah", tertutup)
