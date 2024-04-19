import time
for i in range(1000001):
    if i == 0:
        secondDebut = time.time()
    elif i == 1000000 :
        secondFin = time.time()
    print(i)

secondsPasse = secondFin - secondDebut
print(secondsPasse)