import threading as th
import time

step_process = th.Event()

def worker():
    print("delay time : 9999s. now starting...")

    interrupted = step_process.wait() #아마 wait안에 값 안넣으면 0s 기다리기가 아닌 무한정 기다리기인듯.
    if interrupted:
        print("processing stepped.")
    else:
        print("9999s passed?")

t = th.Thread(target=worker)
t.start()

time.sleep(1)
print("1s spent. now wake up!")
step_process.set()