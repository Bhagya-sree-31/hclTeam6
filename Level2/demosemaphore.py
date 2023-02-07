from threading import *
import time
s=Semaphore(2) #it takes only 2 threads
def wish(name):
    s.acquire()
    for i in range(10):
        print("good evening",end=' ')
        time.sleep(2)
        print(name)
    s.release()
t1=Thread(target=wish,args={'bhagi'})
t2=Thread(target=wish,args={'valli'})
t3=Thread(target=wish,args={'sisi'})
t4=Thread(target=wish,args={'bhashya'})
t5=Thread(target=wish,args={'bhavika'})
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

