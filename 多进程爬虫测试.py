# Mar, 31th, 5:14 PM, 2018 @ dorm 602
# Python 官方库 multiprocess, 多进程测试

import time
import math
from multiprocessing import Pool

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def outputPrime(n):
    if isPrime(n) == True:
        pass
        # print(n, end=' ')

def main():
    start_1 = time.time()
    # 单进程
    for i in range(8888888):
        outputPrime(i)
    end_1 = time.time()
    print()
    print('单进程:', end_1-start_1, '秒')
    # 双进程
    start_2 = time.time()
    pool = Pool(processes=2)
    pool.map(func=outputPrime, iterable=range(8888888))
    end_2 = time.time()
    print()
    print('双进程:', end_2 - start_2, '秒')
    # 三进程
    start_3 = time.time()
    pool = Pool(processes=3)
    pool.map(func=outputPrime, iterable=range(8888888))
    end_3 = time.time()
    print()
    print('三进程:', end_3 - start_3, '秒')
    # 四进程
    start_4 = time.time()
    pool = Pool(processes=4)
    pool.map(func=outputPrime, iterable=range(8888888))
    end_4 = time.time()
    print()
    print('四进程:', end_4 - start_4, '秒')

if __name__ == '__main__':
    main()