# python多线程编程，使用threading标准库

import threading
from time import sleep, ctime

loops=[4, 2]


def loop(nloop, nsec):
    print('start loop ' + str(nloop)+' at '+ ctime())
    sleep(nsec)
    print('loop ' + str(nloop)+ ' done at '+ctime())


def main():
    print(' starting at : '+ctime())
    threads = [];
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop,args=(i,loops[i]))   # 创建一个线程，两个参数，函数和元组
        threads.append(t)

    for i in nloops:
        threads[i].start()                                    # 开始一个线程，start方法

    for i in nloops:
        threads[i].join()

    print(' all done at: '+ctime())


main();  #使用多线程编程的一种方式


