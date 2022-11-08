from datetime import *
from time import *


alma = 0
while alma<10:
    alma = alma+1
    sleep(2)
    print(alma)
    print(datetime.now().microsecond())

#while alma<10000000:
#    alma = alma+1
#    vek = 67617
#    if alma%vek==0:
#        print(alma,"osztható ",vek,"-el")
#    else:
#       pass

