"""
多线程
"""
import threading
import time
from concurrent.futures import ThreadPoolExecutor


def increase(num):
    time.sleep(2)
    result = num + 1
    print(threading.current_thread().name + ": %s + 1 = %s" % (num, result))
    return result


def do_with_thread():
    thread_list = []
    for i in range(10):
        thread = threading.Thread(target=increase, args=(i,))
        thread_list.append(thread)
    print("执行所有线程...")
    for thread in thread_list:
        thread.start()
    print("等待所有线程全部执行完...")
    for thread in thread_list:
        thread.join()
    print("所有线程执行结束！")


def do_with_thread_pool():
    executor = ThreadPoolExecutor(max_workers=10)
    future_list = []
    print("提交所有任务到线程池")
    for i in range(10):
        future = executor.submit(increase, i)
        future_list.append(future)
    print("等待所有线程全部执行完...")
    result_list = []
    for future in future_list:
        result = future.result()
        result_list.append(result)
    print("所有线程执行结束，result=", result_list)


if __name__ == '__main__':
    do_with_thread()
    print("==================")
    do_with_thread_pool()
