from threading import *
import time
l=Lock()
def wish(name):
    l.acquire()
    for i in range(10):
        print("good evening",end=" ")
        time.sleep(2)
        print(name)
    l.release()
t1=Thread(target=wish,args={'bhagi'})
t2=Thread(target=wish,args={'valli'})
t3=Thread(target=wish,args={'sisi'})
t1.start()
t2.start()
t3.start()