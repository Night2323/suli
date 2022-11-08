from random import randrange
from datetime import *
a = randrange(1,30000001)
b = 0
c = randrange(1,2500)
i = 0
print(datetime.now())
while b<101:
    if i%a==0:
        b+=1
    i+=1
print(datetime.now())
print(i,"számig kell számolni ha meg akarjuk keresni a(z)",a,"első",c,"szorzatát")