from threading import *
import time
def wish(name):
    for i in range(10):
        print("good evening", end=' ')
        time.sleep(2)
        print(name)
t1=Thread(target=wish,args={'bhagi'})
t2=Thread(target=wish,args={'valli'})
t1.start()
#t1.join(1)
t2.start()

