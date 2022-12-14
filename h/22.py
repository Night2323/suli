from random import *

list = []
paros = 0
paratlan = 0
for i in range(10):
    list.append(randrange(0,10))
print(list)
for i in range(len(list)):
    if list[i]%2 == 0:
        paros = paros+1
    else:
        paratlan = paratlan+1
print(paros,"db páros szám van.")
print(paratlan,"db páratlan szám van.")
