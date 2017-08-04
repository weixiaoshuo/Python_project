import threading
from time import sleep, ctime

loops = [4, 2]


class MyThread(threading.Thread):                # 派生Thread类，
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)          # 先调用构造方法
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


def loop(nloop, nsec):                            # 线程要执行的函数块
    print(' start loop ' + str(nloop) + ' at ' + ctime())
    sleep(nsec)
    print(' loop ' + str(nloop) + ' done at ' + ctime())


def main():
    print(' starting at : ' + ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)   # 线程的创建方式
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print(' all have done ' + ctime())


main()
