import threading as th
import time

step_process = th.Event()

def worker():
    print("Wait until Pressing Button...")

    interrupted = step_process.wait() #아마 wait안에 값 안넣으면 0s 기다리기가 아닌 무한정 기다리기인듯.
    if interrupted:
        print("Button Pressed.")
    else:
        print("????")

t = th.Thread(target=worker)
t.start()

time.sleep(1)
print("Now Press Button!")
step_process.set()