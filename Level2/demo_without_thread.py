import time
def double(num):
    for n in num:
        time.sleep(2)
        print(2*n)
def square(num):
    for n in num:
        time.sleep(3)
        print(n*n)
n=[1,2,3,4,5]
bt=time.time() #begin time
#double(n)
#square(n)
#et=time.time() #end time
#print(et-bt)
t1=Thread(target=double,args=(n,))
t2=Thread(target=square,args=(n,))
t1.start()
t1.join() #one by one thread execute
t2.start()
#t2.join()
et=time.time()
print(et-bt,sep=' ')