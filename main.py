import time

h = int(input())

while True:
    time.sleep(1)
    h -= 1
    print(h)
    if h == 0:
        print("Бум!")
        break