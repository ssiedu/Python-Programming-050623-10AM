import threading
import time
def square(num):
    for n in num:
        time.sleep(2)
        print("Square :",n**2)


def cube(num):
    for n in num:
        time.sleep(2)
        print("cube :",n**3)


l1=[2,3,4,5]
t1=threading.Thread(target=square,args=(l1,))
t2=threading.Thread(target=cube,args=(l1,))
t1.start()

time.sleep(0.5)
t2.start()
t1.join()
t2.join()
print("Finished Process")
