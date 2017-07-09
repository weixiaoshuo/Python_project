# python多线程编程

from multiprocessing import Process

def run_pro(name):
    print('Child process %s (%s) Running ' %(name,os.getgid()))

if __name__ == "__main__":
    # print('Parent process %s ' % os.getgid())
    for i in range(5):
        p= Process(target  = run_pro(),args = (str(i)))
        print('Process will start')
        p.start()
    p.join()
    print('Process is end')



