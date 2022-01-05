import threading
import time


def print_num(num):
    time.sleep(3)
    print(threading.current_thread().name + ": " + str(num))


if __name__ == '__main__':
    threads = []
    for i in range(10):
        t = threading.Thread(target=print_num, args=(i,))
        threads.append(t)
    for t in threads:
        t.start()
    # 阻塞所有线程
    for t in threads:
        t.join()
    print("所有线程执行完毕")
