import threading
import time

def printer():
    print("hello")

listThreads = []

start_time = time.time()
for x in range(3):
    listThreads.append(threading.Thread(target=printer))
    listThreads[x].start()

print(listThreads)
print("--- %s seconds ---" % (time.time() - start_time))