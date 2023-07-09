import numpy as np
import multiprocessing
import random

asiiList = [chr(i) for i in range(128)]

def test1():
    for i in range(100):
        print(np.array_str(np.random.choice(asiiList, size=1000)))

def test2():
    for i in range(100):
        print("".join([random.choice(asiiList) for i in range(1000)]))

if __name__ == '__main__':
    for j in range(10):
        multiprocessing.Process(target=test1).start()