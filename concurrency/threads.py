import threading
import time


def print_numbers():
    for i in range(10):
        time.sleep(1)
        print(i)


def print_letters():
    for letter in "abcdefghi":
        time.sleep(1.5)
        print(letter)


t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()
