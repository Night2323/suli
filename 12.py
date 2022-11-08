from random import randrange
from datetime import *
a = randrange(1,3001)
b = 0
i = 0
print(datetime.now())
while i<=100000000:
    if i%a==0:
        b+=1
    i+=1
print(datetime.now())
print(b,"számú",a,"-val osztható szám van 100000000-ig")